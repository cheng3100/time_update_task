---
layout: default
title: "2026-11-07 · DMA-BUF Mapping Types"
parent: "Focus"
ancestor: "GPU Memory / Virtual Memory / Unified Memory"
nav_order: 2
permalink: "/kmd_owner_direction/memory/focus/2026-11-07-dmabuf-mapping-types/"
---

# L3 — DMA-BUF Mapping Types：为什么 `sg_table` 开始不够了

> 对应 Weekly #13 的 B2 Deep Dive。本页暂时保持 Weekly B 章节的组织方式，同时开始把 Focus 页面升级为“机制图 + 关键源码原文 + 直接源码入口”的长期学习页面。

[← Weekly #13 完整网页输出]({{ '/kmd_owner_direction/web-update-archive/2026-11-07-weekly-13/' | relative_url }})

---

## 0. 问题背景

### 0.1 这是一个什么问题？

传统 DMA-BUF 的 attachment mapping 模型可以粗略理解成：

<div class="arch-diagram">
  <div class="arch-title">Legacy DMA-BUF mapping contract</div>
  <div class="arch-flow">
    <div class="arch-node"><strong>Exporter</strong><span>owns backing storage</span></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>dma_buf</strong><span>shared memory object</span></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>Attachment</strong><span>exporter ↔ importer</span></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node arch-accent"><strong>sg_table</strong><span>DMA-mapped scatterlist</span></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>Importer</strong><span>consumes dma_addr_t</span></div>
  </div>
</div>

长期以来，DMA-BUF 的核心假设是：

> exporter 最终可以把共享对象转换成一个 importer 能消费的 `struct sg_table`。

这个假设对 system RAM、普通 DMA mapping 非常自然；但随着 DMA-BUF 开始承载 VRAM、PCIe peer memory、IOMMUFD、vGPU、XGMI 等场景，问题逐渐变成：

> **不同 importer 真正需要的“mapping representation”是否仍然都能用一个 `sg_table + dma_addr_t` 表达？**

v2 patch 对问题的直接描述是：DMA-BUF 当前 attachment map operation 只支持 `struct scatterlist`，而 `dma_addr_t` 本身是一种非常具体、受限的 address type。

**Primary references**

- [DMA-BUF Mapping Types v2/23 — cover letter](https://lists.openwall.net/netdev/2026/11/05/140)
- [[PATCH v2 02/23] dma-buf: Introduce DMA-buf mapping types](https://lists.openwall.net/netdev/2026/11/05/152)
- [Linux `include/linux/dma-buf.h`](https://github.com/torvalds/linux/blob/master/include/linux/dma-buf.h)
- [Linux `drivers/dma-buf/dma-buf.c`](https://github.com/torvalds/linux/blob/master/drivers/dma-buf/dma-buf.c)

---

### 0.2 Legacy API 在代码层面是什么样？

先直接看当前传统接口。

**源码位置**

```text
include/linux/dma-buf.h
└── struct dma_buf_ops
    ├── map_dma_buf()
    └── unmap_dma_buf()
```

[打开 Linux 源码：include/linux/dma-buf.h](https://github.com/torvalds/linux/blob/master/include/linux/dma-buf.h)

关键原文：

```c
struct sg_table *(*map_dma_buf)(struct dma_buf_attachment *,
                                enum dma_data_direction);

void (*unmap_dma_buf)(struct dma_buf_attachment *,
                      struct sg_table *,
                      enum dma_data_direction);
```

这里接口签名本身已经把 representation 固定下来：

```text
map result = struct sg_table *
```

因此 importer/exporter 之间即使底层实际共享的是 VRAM、peer BAR 或其它 device memory，最终也必须先“塞进” SGT 语义里。

---

### 0.3 为什么 `dma_addr_t` 不是“通用物理地址”？

这是理解整个 proposal 最关键的一步。

<div class="arch-diagram">
  <div class="arch-title">同一个 Memory Object 可以拥有不同 address representation</div>
  <div class="arch-columns">
    <div class="arch-column">
      <div class="arch-node arch-accent"><strong>Memory Object</strong><span>logical shared buffer</span></div>
    </div>
    <div class="arch-column arch-stack">
      <div class="arch-node"><strong>CPU PA</strong><span>CPU physical address</span></div>
      <div class="arch-node"><strong>IOVA / dma_addr_t</strong><span>device-visible DMA address</span></div>
      <div class="arch-node"><strong>PCIe BAR / bus addr</strong><span>peer aperture</span></div>
      <div class="arch-node"><strong>GPU PA</strong><span>GPU internal physical address</span></div>
      <div class="arch-node"><strong>IOMMUFD mapping</strong><span>IOAS / HWPT representation</span></div>
    </div>
  </div>
</div>

普通 IOMMU DMA 路径可以是：

<div class="arch-diagram compact">
  <div class="arch-flow">
    <div class="arch-node"><strong>Importer device</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node arch-accent"><strong>IOVA / dma_addr_t</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>IOMMU</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>Physical backing</strong></div>
  </div>
</div>

因此：

```text
dma_addr_t
    ≠ CPU PA
    ≠ GPU PA
    ≠ PCIe peer address
    ≠ generic “memory address”
```

它更准确的语义是：

> **针对某个 DMA consumer，可以实际发起 DMA transaction 的 device-visible address。**

这也是为什么一个只围绕 `dma_addr_t` 构建的共享模型开始碰到边界。

---

### 0.4 v2 到 Weekly #13 时发展到什么程度？

截至 **2026-11-07 / Weekly #13**，v2 series 的重点是：

1. 保留 Mapping Type framework；
2. 把传统 SGT 使用者逐步转换到新 framework；
3. attach 阶段先得到双方兼容的 candidate set；
4. 最终 mapping type 延迟到第一次 pin/map 时由 exporter 选择；
5. 这个选择保持到 exporter 主动 invalidate attachment。

后续计划包括：

```text
IOMMUFD importer type
PCIe P2P independent mapping type
XGMI exclusive mapping type
```

这些在 Week #13 时仍属于后续方向，不应写成已经完成。

---

## 1. Legacy DMA-BUF：为什么原来的模型长期有效？

Legacy 模型本身并不是错误设计。

它针对的典型设备共享场景是：

<div class="arch-diagram">
  <div class="arch-title">Classic DMA-BUF flow</div>
  <div class="arch-flow vertical">
    <div class="arch-node"><strong>Exporter allocates buffer</strong><span>pages / GEM backing</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>dma_buf_export()</strong><span>create struct dma_buf</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Importer attach</strong><span>struct dma_buf_attachment</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node arch-accent"><strong>map_dma_buf()</strong><span>return struct sg_table *</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Importer DMA</strong><span>consume sg_dma_address()</span></div>
  </div>
</div>

在典型 system-memory DMA 场景：

```text
pages
  ↓
scatterlist
  ↓
DMA API mapping
  ↓
dma_addr_t
  ↓
device
```

这个抽象非常合适，因为 importer 真正需要的就是一个“这个设备可以 DMA 的 scatter-gather list”。

### 对应源码对象

```text
struct dma_buf
        │
        ├── attachments
        ├── ops
        └── resv

struct dma_buf_attachment
        │
        ├── dmabuf
        ├── dev
        ├── importer_ops
        └── priv
```

**源码位置**

- [`struct dma_buf_attachment` — include/linux/dma-buf.h](https://github.com/torvalds/linux/blob/master/include/linux/dma-buf.h)
- [attach/map implementation — drivers/dma-buf/dma-buf.c](https://github.com/torvalds/linux/blob/master/drivers/dma-buf/dma-buf.c)

关键原文：

```c
struct dma_buf_attachment {
        struct dma_buf *dmabuf;
        struct device *dev;
        const struct dma_buf_attach_ops *importer_ops;
        void *priv;
};
```

这说明 attachment 本身代表：

```text
一个 shared buffer
        ×
一个 importing device
```

真正的 device-specific mapping 正是在 attachment 上建立。

---

## 2. Legacy 模型的问题：SGT 同时承担了太多语义

当共享对象只是 system RAM 时：

```text
sg_table
≈
backing pages + DMA mapping for importer
```

问题还不明显。

但今天一个 GPU buffer 可能是：

<div class="arch-diagram">
  <div class="arch-title">Modern GPU buffer placement / sharing space</div>
  <div class="arch-grid">
    <div class="arch-node"><strong>System RAM</strong><span>normal DMA / IOVA</span></div>
    <div class="arch-node"><strong>Local VRAM</strong><span>GPU-local address</span></div>
    <div class="arch-node"><strong>PCIe Peer VRAM</strong><span>BAR / bus aperture</span></div>
    <div class="arch-node"><strong>vGPU / VF memory</strong><span>virtualized address model</span></div>
    <div class="arch-node"><strong>IOMMUFD</strong><span>IOAS / HWPT</span></div>
    <div class="arch-node"><strong>XGMI peer memory</strong><span>fabric-specific representation</span></div>
  </div>
</div>

于是同一个逻辑动作：

```text
“把这个 dma-buf 给 importer”
```

可能实际要求完全不同的结果：

```text
SGT with DMA addresses
PCIe P2P aperture
IOMMUFD-specific mapping
XGMI/fabric mapping
driver-specific representation
```

因此问题不再是：

> `sg_table` 能不能装几个地址。

而是：

> **接口是不是把“共享对象”错误地绑定成了“唯一一种 mapping representation”。**

---

## 3. Mapping Types：新 framework 改了什么？

v2 patch 把 mapping 从“固定返回 SGT”提升成一个可以协商的 type。

### 3.1 Importer 先声明自己支持什么

**Patch 位置**

```text
[PATCH v2 02/23]
include/linux/dma-buf-mapping.h
include/linux/dma-buf.h
drivers/dma-buf/dma-buf-mapping.c
```

[打开 v2 patch](https://lists.openwall.net/netdev/2026/11/05/152)

Patch 中 importer 示例的核心原文：

```c
static const struct dma_buf_mapping_match imp_match[] = {
        DMA_BUF_IMAPPING_MY_DRIVER(...),
        DMA_BUF_IMAPPING_SGT(DMA_SGT_NO_P2P),
};
```

attach ops 再声明这个 supported set：

```c
.supported_mapping_types = imp_match,
.nr_supported_mapping_types = ARRAY_SIZE(imp_match),
```

这比旧模型多了一层非常重要的 contract：

```text
Importer:
“我支持这些 representation”
```

而不是默认：

```text
Importer:
“给我一个 SGT 就行”
```

---

### 3.2 Attach 阶段先做 capability negotiation

<div class="arch-diagram">
  <div class="arch-title">Mapping Types — attach phase</div>
  <div class="arch-columns">
    <div class="arch-column arch-stack">
      <div class="arch-node"><strong>Importer</strong></div>
      <div class="arch-node"><span>SGT</span></div>
      <div class="arch-node"><span>Driver-specific Type A</span></div>
    </div>
    <div class="arch-column center">
      <div class="arch-arrow large">→</div>
      <div class="arch-node arch-accent"><strong>Match / Negotiate</strong><span>compatible set</span></div>
      <div class="arch-arrow large">←</div>
    </div>
    <div class="arch-column arch-stack">
      <div class="arch-node"><strong>Exporter</strong></div>
      <div class="arch-node"><span>SGT</span></div>
      <div class="arch-node"><span>Type A</span></div>
      <div class="arch-node"><span>Type B</span></div>
    </div>
  </div>
  <div class="arch-result"><strong>Result:</strong> { SGT, Type A }</div>
</div>

这里输出的首先不是某个 address，而是：

```text
compatible mapping type set
```

这本质上更接近 capability negotiation。

---

### 3.3 第一次 pin/map 才真正选 type

v2 相比早期 RFC 的一个关键变化，是**最终 type 不在 attach 时立即固定**。

<div class="arch-diagram">
  <div class="arch-title">Why selection is deferred</div>
  <div class="arch-flow vertical">
    <div class="arch-node"><strong>Attach</strong><span>match candidate types</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Buffer placement may still change</strong><span>VRAM ↔ System RAM</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node arch-accent"><strong>First pin / map</strong><span>exporter selects actual type</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Mapping active</strong><span>selected type remains stable</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Exporter invalidates</strong><span>selection can be reconsidered</span></div>
  </div>
</div>

原因是 exporter 需要同时考虑：

```text
candidate mapping types
        +
current buffer placement
        +
other attachments
```

这把 **mapping representation selection** 和 **memory placement policy** 正式联系起来。

---

## 4. Legacy 与 Mapping Types 的核心差异

<div class="arch-diagram compare">
  <div class="arch-title">Legacy vs Mapping Types</div>
  <div class="arch-columns">
    <div class="arch-column arch-stack">
      <div class="arch-label">Legacy</div>
      <div class="arch-node"><strong>dma_buf</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node"><strong>Attachment</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node arch-accent"><strong>map_dma_buf()</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node"><strong>sg_table</strong><span>fixed representation</span></div>
    </div>
    <div class="arch-column arch-stack">
      <div class="arch-label">Mapping Types</div>
      <div class="arch-node"><strong>dma_buf</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node"><strong>Attachment</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node arch-accent"><strong>type negotiation</strong></div>
      <div class="arch-arrow">↓</div>
      <div class="arch-node"><strong>selected mapping type</strong><span>SGT / future P2P / IOMMUFD / ...</span></div>
    </div>
  </div>
</div>

可以把抽象变化压缩成：

```text
Legacy:
“Give me the SGT for this buffer.”

Mapping Types:
“Which representation can both sides use
for this buffer at its current placement?”
```

---

## 5. 为什么不能简单增加几个 flag 到 `sg_table`？

如果不同 sharing 场景仅仅是：

```text
SGT + a few attributes
```

那增加 flag 可能足够。

但 Mapping Types 的目标是允许不同 type 拥有不同的：

```text
match semantics
map/unmap callbacks
mapping object
type-specific state
address representation
```

因此它更接近：

```text
abstract mapping interface
```

而不是：

```text
SGT v2
```

这为之后 IOMMUFD、P2P、XGMI 等真正不是普通 SGT semantics 的类型留出空间。

---

## 6. 为什么它和 GPU Memory / UVM 强相关？

从 Memory Owner 的视角，不应只把它看成 DMA-BUF API 重构。

更重要的是建立三层分离：

<div class="arch-diagram">
  <div class="arch-title">Memory Owner view</div>
  <div class="arch-flow vertical">
    <div class="arch-node"><strong>Memory Object</strong><span>“这块共享内存是谁？”</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node arch-accent"><strong>Mapping Representation</strong><span>“以什么形式暴露给 consumer？”</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>Device Accessibility</strong><span>“consumer hardware 真的能访问吗？”</span></div>
  </div>
</div>

这三者不能混为一谈：

```text
Memory Object
      ≠
Mapping Representation
      ≠
Device Accessibility
```

例如一个 GPU VRAM BO：

```text
同一个 BO
  │
  ├── GPU local PA
  ├── CPU-visible BAR mapping
  ├── peer PCIe aperture
  ├── possible IOMMU mapping
  └── future fabric-specific representation
```

这和 UVM 自身的思想很相似：

```text
同一个 logical allocation
  │
  ├── CPU VA/PTE representation
  ├── GPU VA/PTE representation
  ├── system-memory residency
  └── VRAM residency
```

长期设计原则：

> **不要把 memory object、placement、address representation、consumer accessibility 设计成同一个概念。**

---

## 7. 与 PCIe P2P 的接口在哪里？

Mapping Types 解决的是：

```text
应该给 importer 什么 representation？
```

P2P addressability 继续回答：

```text
即使 representation 正确，
importer hardware 真能发出这个地址吗？
```

<div class="arch-diagram">
  <div class="arch-title">B2 → B3: complete sharing path</div>
  <div class="arch-flow">
    <div class="arch-node"><strong>Memory Object</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node arch-accent"><strong>Mapping Type</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>DMA / IOMMU Address</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>Interconnect Route</strong></div>
    <div class="arch-arrow">→</div>
    <div class="arch-node"><strong>HW Addressability</strong></div>
  </div>
</div>

这也是为什么 DMA-BUF / P2P / IOMMU 最终应该作为一套 Memory sharing architecture 来理解。

---

## 8. 源码阅读路径

建议不要顺序阅读整个 DMA-BUF subsystem，而按下面路径：

<div class="arch-diagram compact">
  <div class="arch-flow vertical">
    <div class="arch-node"><strong>v2 cover letter</strong><span>先理解 Why</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>PATCH 02/23</strong><span>mapping type objects / importer capability</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>include/linux/dma-buf.h</strong><span>对照 legacy attachment / ops</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>dma-buf-mapping.h</strong><span>理解新 abstraction</span></div>
    <div class="arch-arrow">↓</div>
    <div class="arch-node"><strong>later SGT conversion patches</strong><span>看现有 driver 如何迁移</span></div>
  </div>
</div>

### 入口索引

- [v2/23 cover letter](https://lists.openwall.net/netdev/2026/11/05/140)
- [PATCH 02/23 — Introduce DMA-buf mapping types](https://lists.openwall.net/netdev/2026/11/05/152)
- [Legacy/current `include/linux/dma-buf.h`](https://github.com/torvalds/linux/blob/master/include/linux/dma-buf.h)
- [Legacy/current `drivers/dma-buf/dma-buf.c`](https://github.com/torvalds/linux/blob/master/drivers/dma-buf/dma-buf.c)

重点对象：

```text
Legacy:
struct dma_buf
struct dma_buf_attachment
struct dma_buf_ops
map_dma_buf()
unmap_dma_buf()

Mapping Types:
struct dma_buf_mapping_match
struct dma_buf_match_args
struct dma_buf_mapping_exp_ops
supported_mapping_types
nr_supported_mapping_types
```

---

## 9. 本节结论

如果只记一个 API change：

```text
dma-buf 新增 mapping type
```

价值其实不大。

更值得长期保存的是：

```text
Memory Object
      ≠
Mapping Representation
```

进一步：

```text
Shared-memory contract
      =
Memory Object
    + Representation Negotiation
    + Placement Constraint
    + Consumer Capability
```

这个模型会直接连接到 PCIe P2P、IOMMU/IOMMUFD、GPU ↔ NPU、GPU ↔ Camera、Multi-GPU 和 device-private memory。
