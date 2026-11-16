# B1. L4 — TLB invalidation completion 为什么属于 BO lifetime

> 本文作为 **GPU KMD Weekly B 模块（Key Topic Detail / Deep Dive）网页输出模板**。
> 
> 目标：对 Memory/UVM L4 主题，从问题背景、upstream 进展、关键实现、代码位置、lifetime/race、自研 KMD 映射、验证方案到长期设计原则形成一套可复用的深入输出结构。

## 0. 问题背景

### 0.1 这是一个什么问题？

这次 upstream 讨论的核心不是普通意义上的：

> “AMDGPU 某处忘记 flush TLB。”

真正的问题是：

> **GPU page-table mapping 已经删除之后，对应的 BO / physical backing memory 到底什么时候才能安全释放和重新使用？**

这个问题出现在 AMDGPU user queue 场景。

简化后的过程如下：

```text
GPU VA
  │
  ▼
GPU PTE
  │
  ▼
Physical Page / BO
```

当 BO 被 unmap 时，KMD 会：

```text
remove PTE
    ↓
issue TLB invalidation
```

但 TLB invalidation 是一个独立的异步硬件操作。

因此存在这样一个时间窗口：

```text
PTE 已经删除
      │
      ▼
TLB invalidate 已发出
      │
      │     ← invalidate 尚未真正完成
      │
      ▼
BO 被 close / free
      │
      ▼
physical page 被重新分配
```

如果 GPU user queue 此时仍然持有旧的 TLB translation：

```text
old VA
  │
  ▼
stale TLB entry
  │
  ▼
old PA
```

那么即使 page table 中已经不存在这个 mapping，GPU 仍然可能继续访问旧 PA。

AMDGPU v2 patch 对 root cause 的描述非常明确：如果该 BO 在 GEM close 之前已经发生 unmap，那么 `clear_freed()` 之前已经执行过，`vm->freed` 可能已经为空；这样 close path 中就没有一个有意义的 fence 能保证之前的 TLB flush 已完成，因此 memory 可能在 TLB flush 完成前被释放，而运行中的 user queue 仍拥有 stale address translation。

参考：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

---

### 0.2 有什么影响？

最简单的影响是 GPU fault，但真正值得关注的是下面这个场景：

```text
                 原始状态

GPU VA X
   │
   ▼
PA Y
   │
   ▼
BO A


                 unmap

GPU Page Table:
VA X → invalid

GPU TLB:
VA X → PA Y        ← 旧 entry 仍存在


                 BO A free

PA Y
   │
   ▼
returned to allocator


                 PA Y reused

PA Y
   │
   ▼
BO B


                 running user queue

VA X
   │
   ▼
stale TLB
   │
   ▼
PA Y
   │
   ▼
BO B
```

这时问题已经从：

```text
“访问了一个已经 unmap 的 VA”
```

升级成：

```text
“使用旧 VA translation
访问了已经属于另一个对象的 physical memory”
```

因此潜在后果包括：

- GPU page fault；
- workload 随机错误；
- silent memory corruption；
- BO A 对 BO B 的 stale access；
- 信息泄漏；
- 如果对象属于不同安全域，可能进一步形成 isolation 问题。

所以这个问题最重要的设计启示是：

```text
Page-table lifetime
        !=
Translation-cache lifetime
        !=
Memory-object lifetime
```

---

### 0.3 当前 upstream 方案和进展

Weekly #13 的时间边界是 **2026-11-07**。

截至这个时间点，当前版本是：

**`[PATCH v2] drm/amdgpu: wait for tlb flush before freeing BO`**

v2 的核心方案是：

```text
track last TLB invalidation fence
             │
             ▼
       vm->last_tlb_inv
             │
             ▼
attach it to BO reservation
             │
             ▼
      BO lifetime waits
        for TLB completion
```

也就是说，把原本属于：

```text
GPU VM / translation lifetime
```

的一个 completion dependency，显式挂到：

```text
BO lifetime
```

上。

v2 同时说明，它已经 rebase 到：

```text
drm/amdgpu: fix TLB invalidation fence handling v4
```

从而获得独立的：

```text
vm->last_tlb_inv
```

并且把 fence attachment 放在 `clear_freed()` 之后，确保等待的是正确的 invalidation。

截至 Weekly #13 可以概括成：

```text
问题确认
  ↓
root cause 明确
  ↓
last_tlb_inv abstraction 已形成
  ↓
v2 把它连接到 BO lifetime
  ↓
review 继续讨论 dma_resv fence reservation 等实现细节
```

11 月 9 日之后已经出现 v3，但那属于 **Weekly #14** 的时间窗口，因此本节不把 v3 当成本期状态。v3 的存在可以作为后续追踪参考。

---

### 0.4 本问题相关 upstream / source 索引

这一部分作为后续自行深入阅读的入口。

#### 1. Weekly #13 核心 patch：v2

**`[PATCH v2] drm/amdgpu: wait for tlb flush before freeing BO`**

这是本节最重要的原始材料。建议首先阅读 commit message，然后只看 `amdgpu_gem_object_close()` 的几行 diff。

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

也可以从完整 thread 阅读前后 revision 和 review：

- https://lore-kernel.gnuweeb.org/amd-gfx/f99b863b-9ad1-4fba-b6e0-b838849d5b1b%40amd.com/T/

---

#### 2. v2 review discussion

Christian König 在 11 月 6 日的 review 中继续讨论 BO reservation fence slot 等 integration 问题。

这部分适合在理解方案以后阅读，因为它展示的是：

```text
architecture idea
      ↓
如何落到 dma_resv / BO fence implementation
```

- https://mail-archive.com/search?f=1&l=amd-gfx%40lists.freedesktop.org&o=newest&q=date%3A20261106
- https://lore-kernel.gnuweeb.org/amd-gfx/f99b863b-9ad1-4fba-b6e0-b838849d5b1b%40amd.com/T/

---

#### 3. 后续 v3，仅用于观察进展

**`[PATCH v3 1/2] drm/amdgpu: wait for tlb flush before freeing BO`**

这是 11 月 9 日的后续版本，不属于 Weekly #13 的正文时间范围。

v3 根据 review 调整了额外 fence reservation 的位置：

```text
reserve extra fence under lock
```

而不再依赖 `amdgpu_bo_fence()` 隐式处理。

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155265.html

---

#### 4. Linux upstream AMDGPU GEM close 代码

本问题直接修改的位置：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c

└── amdgpu_gem_object_close()
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c

建议搜索：

```text
amdgpu_gem_object_close
amdgpu_vm_clear_freed
amdgpu_bo_fence
```

---

#### 5. AMDGPU VM implementation

TLB / VM update 的主要实现入口：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

建议重点搜索：

```text
amdgpu_vm_clear_freed
last_tlb_inv
last_update
```

---

#### 6. AMDGPU VM data structure

VM object 和相关状态定义：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_vm.h
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vm.h

建议重点查看：

```text
struct amdgpu_vm
last_update
last_tlb_inv
```

---

### 推荐阅读顺序

```text
v2 commit message
        ↓
v2 几行 diff
        ↓
review discussion
        ↓
amdgpu_gem_object_close()
        ↓
amdgpu_vm_clear_freed()
        ↓
struct amdgpu_vm
        ↓
last_update / last_tlb_inv
        ↓
再回头理解为什么 BO resv 需要 TLB fence
```

不要一开始顺序阅读整个 `amdgpu_vm.c`。

---

## 1. 为什么 PTE 删除不等于 translation 消失？

先把软件视角和硬件视角分开。

假设：

```text
GPU VA = 0x100000

       │
       │ GPU Page Table
       ▼

PA = 0x80000000

       │
       ▼

BO A
```

GPU 已经访问过这个地址，所以某级 TLB 中可能缓存：

```text
VA 0x100000 → PA 0x80000000
```

现在 KMD 修改 GPU page table：

```text
VA 0x100000 → INVALID
```

软件看到：

```text
GPU Page Table

VA 0x100000
     X
  no mapping
```

但硬件可能仍然看到：

```text
GPU TLB

┌─────────────────────────────┐
│ VA 0x100000 → PA 0x80000000 │
└─────────────────────────────┘
```

原因很简单：

```text
Page Table
```

和：

```text
TLB
```

是两个不同的 state。

---

### 软件 authoritative state

由 KMD 维护：

```text
PDB
 │
 └── PDE
      │
      └── PTE
```

它回答的是：

> **当前正式 mapping 应该是什么？**

---

### GPU cached translation state

可能分布在：

```text
L1 TLB
L2 TLB
per-engine translation cache
page-walk cache
...
```

它回答的是：

> **硬件现在还可能用什么 translation？**

因此：

```text
PTE update
```

只改变 authoritative state。

它本身无法证明：

```text
所有 GPU execution units
已经停止使用旧 translation
```

---

## 2. 一个 GPU unmap 实际上至少包含四个不同阶段

很多 driver 代码容易把下面这些操作概念上合并成：

```text
unmap()
```

但从 lifetime 角度应该拆开。

### T0 — PTE update

```text
VA → PA
```

变成：

```text
VA → INVALID
```

此时：

```text
Page Table:
new state
```

但：

```text
TLB:
possibly old state
```

---

### T1 — TLB invalidate submitted

KMD/FW/HW 发起：

```text
invalidate VA/range/VMID/PASID
```

这表示：

> 已要求硬件清除旧 translation。

但并不自动等于：

> 已经清除完成。

---

### T2 — TLB invalidation completed

硬件给出明确 completion：

```text
TLB invalidate
       │
       ▼
   completion
```

此时才可以认为相关 translation cache 已满足硬件定义的 invalidation semantics。

---

### T3 — old access drained

还有一个自研 KMD 必须和 HW 确认的问题：

> **TLB invalidate completion 是否同时保证所有已经基于旧 translation 发出的 memory request 都完成？**

不一定应该想当然。

可能存在：

```text
TLB lookup
   ↓
old PA obtained
   ↓
memory request issued
   ↓

       TLB invalidate completes

   ↓
old memory request still in fabric
```

因此需要 HW contract 明确：

```text
TLB invalidation completion
        ?=
all prior translated transactions drained
```

如果答案是否定的，就还需要额外 ordering / drain point。

---

### T4 — BO / page reusable

只有前面的条件满足后，physical backing 才能安全：

```text
return to allocator
```

或：

```text
reuse by another BO
```

于是完整模型是：

```text
PTE update
   │
   ▼
TLB invalidate submit
   │
   ▼
TLB invalidate completion
   │
   ▼
old accesses drained
   │
   ▼
BO / physical page reusable
```

---

## 3. AMDGPU 原来的 dependency 为什么可能丢失？

本问题直接修改：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c
```

函数：

```text
amdgpu_gem_object_close()
```

Weekly #13 的 v2 diff 真正值得看的代码只有几行：

```c
if (r || !fence)
        goto out_tlb;

amdgpu_bo_fence(bo, fence, true);
dma_fence_put(fence);

out_tlb:
        amdgpu_bo_fence(bo, vm->last_tlb_inv, true);
```

完整 v2 diff：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

不要从代码行数判断这个 patch 的重要性。

真正的问题在于：

```text
fence
```

和：

```text
vm->last_tlb_inv
```

代表的 dependency 不完全相同。

---

## 4. 为什么 `clear_freed()` 返回的 fence 不一定够？

考虑下面的时间线。

### 第一次：BO 被 unmap

```text
GPUVA unmap
    │
    ▼
vm->freed receives mapping
    │
    ▼
amdgpu_vm_clear_freed()
    │
    ├── update page tables
    │
    └── trigger TLB invalidation
```

之后：

```text
vm->freed
```

已经被处理。

---

### 第二次：GEM object close

稍后：

```text
amdgpu_gem_object_close()
        │
        ▼
amdgpu_vm_clear_freed()
```

但这个时候：

```text
vm->freed == empty
```

因为真正相关的 unmap 已经发生在更早之前。

于是 close path 这一次得到的：

```text
fence
```

可能并不能代表：

> 之前真正影响这个 BO 的 TLB invalidation 是否已经完成。

这就是 upstream commit message 中指出的核心 bug。

参考：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

因此需要另外保存：

```text
last relevant TLB invalidation
```

也就是：

```text
vm->last_tlb_inv
```

---

## 5. `last_update` 和 `last_tlb_inv` 为什么值得分开？

这是这个问题里比具体 bug 更有架构价值的一点。

逻辑上：

```text
VM update
```

和：

```text
TLB invalidation
```

经常一起发生。

所以很容易设计成：

```text
vm->last_update
```

统一代表：

```text
“上一次 VM operation 完成”
```

但实际上两者生命周期并不相同。

更合理的抽象是：

```text
             struct amdgpu_vm
                     │
          ┌──────────┴──────────┐
          │                     │
     last_update          last_tlb_inv
          │                     │
          ▼                     ▼
 Page-table / VM          Translation-cache
 update dependency         completion
```

也就是说：

```text
last_update
```

回答：

> page-table / VM state 的 update dependency。

而：

```text
last_tlb_inv
```

回答：

> 对这些修改相关的 translation cache invalidation 是否完成。

这是一个很值得自研 KMD 直接吸收的原则：

> **两个异步动作即使通常一起发生，只要它们的完成条件和 consumer 不同，就不应该强行使用同一个 completion/fence state。**

---

## 6. AMDGPU 怎么把 Translation lifetime 接到 BO lifetime？

这一层才是本 patch 最核心的设计。

AMDGPU VM 中有：

```text
amdgpu_vm
    │
    └── last_tlb_inv
            │
            ▼
         dma_fence
```

而 BO 有：

```text
amdgpu_bo
    │
    ▼
dma_resv
```

`dma_resv` 可以理解为：

> 与这个 memory object 的使用和 lifetime 相关的一组 synchronization dependencies。

这次 patch：

```c
amdgpu_bo_fence(bo, vm->last_tlb_inv, true);
```

本质建立：

```text
      GPU VM
         │
         │
  last_tlb_inv fence
         │
         ▼
 ┌─────────────────┐
 │ BO reservation  │
 │    dma_resv     │
 └─────────────────┘
         │
         ▼
     BO release
```

因此它不是简单：

```text
“close 时多等一个 fence”
```

而是：

```text
Translation-cache lifetime
            │
            ▼
Memory-object lifetime dependency
```

这就是为什么这个小 patch 对 Memory/UVM Owner 很有价值。

参考：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html
- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c

重点搜索：

```text
amdgpu_gem_object_close
amdgpu_bo_fence
```

---

## 7. 映射到自研 KMD：不要只提供一个 `tlb_flush()`

如果自研 KMD 最终只有：

```c
gpu_vm_tlb_flush(vm);
```

那么 Memory subsystem 上层仍然回答不了这些关键问题：

```text
这个 flush 属于哪个 VM update？

它影响哪个 VA range？

属于哪个 VM generation？

什么时候真正完成？

哪些 BO/page 依赖这个 completion？

GPU reset 后这个 completion 是否仍然有效？

这个 physical page 什么时候可以回 allocator？
```

因此更适合从 lifetime model 出发。

例如逻辑上：

```text
struct gpu_vm
    │
    ├── pte_generation
    ├── tlb_submit_seq
    ├── tlb_complete_seq
    └── last_tlb_fence
```

BO 则有：

```text
struct gpu_bo
    │
    ├── mapping references
    ├── residency state
    ├── synchronization dependencies
    └── release eligibility
```

具体字段名不重要。

重要的是这些 state 不能丢。

---

### 更合理的 dependency

```text
GPUVA update
     │
     ▼
PTE publication
     │
     ▼
TLB invalidate submission
     │
     ▼
TLB invalidate completion
     │
     ▼
old access drain
     │
     ▼
BO release eligibility
```

这里真正值得 KMD architecture review 的问题是：

> **谁负责把 VM-side completion 转换成 memory-object-side lifetime dependency？**

AMDGPU 这次给出了一个非常具体的参考答案：

```text
VM TLB fence
     ↓
BO reservation
```

---

## 8. 到 UVM / recoverable fault 后，这个问题为什么更复杂？

GEM close 只是最简单的情况。

UVM fault path 是异步链条：

```text
GPU fault
    │
    ▼
fault worker
    │
    ▼
HMM lookup
    │
    ▼
resolve backing
    │
    ├── map system memory
    │
    └── migrate to VRAM
              │
              ▼
         publish GPU PTE
              │
              ▼
          TLB operation
              │
              ▼
            replay
```

与此同时 CPU 可以执行：

```text
munmap()
mprotect()
COW
process exit
```

GPU/KMD 侧还可能执行：

```text
context destroy
VM destroy
GPU reset
FW restart
```

于是就出现比 stale TLB 更进一步的问题。

---

### 示例：stale fault worker republish

```text
GPU fault worker

HMM resolves page
      │
      │
      │           CPU thread
      │
      │           munmap()
      │              │
      │              ▼
      │        mapping invalidated
      │
      ▼
publish GPU PTE
```

如果 fault worker 没有重新验证 generation：

```text
已经被 CPU 删除的 mapping
```

可能再次被 GPU driver 发布回来。

所以：

```text
no stale TLB
```

仍然不足以证明：

```text
memory can be safely reused
```

---

## 9. Memory/UVM 最终需要同时管理哪些 generation？

至少可以开始考虑：

```text
mmu_notifier sequence
        │
        ├── CPU VA/PTE validity
        │
VM generation
        │
        ├── GPU VM lifecycle
        │
Context generation
        │
        ├── execution context lifetime
        │
Recovery generation
        │
        ├── reset/FW restart world
        │
TLB generation / fence
        │
        └── translation-cache lifetime
```

这些 generation 不一定最后都需要作为显式整数存在。

但它们代表的**逻辑生命周期必须存在**。

---

## 10. 建议把问题抽象成一个 Memory invariant

这一期最值得长期留下来的不是：

```c
amdgpu_bo_fence(bo, vm->last_tlb_inv, true);
```

而是下面这个 invariant：

```text
A physical page / BO may be reused

IFF

1. no valid GPU mapping references it

AND

2. all relevant translation-cache
   invalidations have completed

AND

3. old GPU/DMA accesses can no longer
   reach the physical backing

AND

4. no stale fault / migration / replay
   operation can recreate the old mapping
```

也就是说：

```text
SAFE_TO_REUSE(page)
 =
 !mapped
 &&
 !cached_translation
 &&
 !old_access_in_flight
 &&
 !stale_async_republisher
```

这可以成为以后 Memory Owner review UVM、migration、eviction、P2P revoke 等设计时的一条共同原则。

---

## 11. Race / Lifetime Matrix

这一模块建议作为以后 **L4 Memory Deep Dive 的固定组成部分**。

| Path A | Path B | 主要风险 | 需要关注的同步/lifetime |
|---|---|---|---|
| GPUVA unmap | running user queue | stale translation | TLB completion |
| GPUVA unmap | BO close/free | backing 提前复用 | BO reservation |
| BO free | new BO allocation | old VA 访问新对象 | allocator + TLB |
| migration | TLB invalidation | old residency 可继续访问 | migration + TLB |
| HMM fault | `munmap()` | stale PTE republish | `mmu_notifier` |
| fault replay | context destroy | stale execution | context generation |
| TLB invalidate | GPU reset | old completion 跨 generation | recovery generation |
| BO teardown | DMA engine | outstanding DMA after free | DMA completion |

它的价值是把：

```text
“这里可能有 race”
```

变成：

```text
哪个 lifetime
和哪个 lifetime
发生交叉？
```

这样更容易进一步转化成代码锁设计和 test case。

---

## 12. 第一版自研 KMD 建议怎样验证？

不要只做：

```text
map
→ run
→ unmap
→ pass
```

应该主动扩大危险窗口。

例如：

```text
GPU

while (1)
    access VA X


CPU / KMD

unmap X
   │
   ▼
artificially delay
TLB completion
   │
   ▼
close/free BO A
   │
   ▼
allocate BO B
   │
   ▼
attempt to reuse
same physical backing
```

观察：

### Test 1 — BO lifetime

TLB completion 之前：

```text
BO A
```

是否真的还能进入 allocator。

---

### Test 2 — stale access

BO B 分配以后：

```text
old GPU workload
```

是否可能修改 BO B。

---

### Test 3 — Reset race

人为制造：

```text
TLB invalidate in flight
        │
        ▼
GPU reset
```

检查：

```text
old tlb fence
```

是否会在新 generation 中被错误当成有效 completion。

---

### Test 4 — Fault replay race

```text
fault worker
   │
   ▼
resolve page

        context destroy / munmap

fault worker
   │
   ▼
attempt PTE publish
```

检查 generation validation 能否阻止 stale republish。

---

## 13. Observability 最少应该记录什么？

如果这个 subsystem 将来出现问题，仅打印：

```text
TLB timeout
```

远远不够。

至少应该能够关联：

```text
device ID

VM / PASID
    │
VA / range
    │
BO / backing ID
    │
PTE generation
    │
TLB invalidate seq
    │
TLB completion seq
    │
context generation
    │
recovery generation
```

最终 timeline 可以类似：

```text
VM42 / BO17

PTE_UNMAP        seq=105
        │
        ▼
TLB_INV_SUBMIT   seq=73
        │
        │
        ├── BO_CLOSE attempted
        │
        └── BO release blocked
        │
        ▼
TLB_INV_DONE     seq=73
        │
        ▼
BO_RELEASE
```

这种 trace 对将来 UVM/fault debugging 会非常有价值。

---

## 14. 本节源码阅读入口

Weekly 正文不需要复制大量 kernel code。

更有效的方式是：

```text
问题
 ↓
关键 patch
 ↓
关键代码 5~15 行
 ↓
源码位置
 ↓
函数/字段索引
```

### GEM close / BO lifetime

文件：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c

重点：

```text
amdgpu_gem_object_close()
amdgpu_bo_fence()
```

核心 patch：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

---

### GPU VM / page-table update

文件：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

重点搜索：

```text
amdgpu_vm_clear_freed()
last_tlb_inv
last_update
```

---

### VM data structure / synchronization state

文件：

```text
drivers/gpu/drm/amd/amdgpu/amdgpu_vm.h
```

- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vm.h

重点：

```text
struct amdgpu_vm
last_update
last_tlb_inv
```

---

### Patch revision / review history

完整 thread：

- https://lore-kernel.gnuweeb.org/amd-gfx/f99b863b-9ad1-4fba-b6e0-b838849d5b1b%40amd.com/T/

11 月 6 日 review：

- https://mail-archive.com/search?f=1&l=amd-gfx%40lists.freedesktop.org&o=newest&q=date%3A20261106

11 月 9 日 v3：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155265.html

其中 v3 不属于 Weekly #13 的时间窗口，只作为后续进展参考。

---

## 15. 本节结论

这次 AMDGPU bug 表面上只是：

```text
BO free
发生得比
TLB flush completion
更早
```

但对 Memory/UVM Owner 更重要的结论是：

```text
PTE invalid
      ≠
translation inaccessible
```

进一步：

```text
PTE invalidation
      ≠
TLB invalidation submitted
      ≠
TLB invalidation completed
      ≠
old access disappeared
      ≠
physical memory reusable
```

AMDGPU 选择：

```text
vm->last_tlb_inv
        │
        ▼
BO dma_resv
```

把两个 lifetime 连起来，是一个非常具体的 upstream implementation。

参考：

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html

而对于自研 KMD，更值得保留下来的长期设计原则是：

```text
Memory lifetime
    =
mapping lifetime
  + translation-cache lifetime
  + outstanding-access lifetime
  + asynchronous fault/replay lifetime
```

以后进入：

```text
HMM / SVM
migration
eviction
oversubscription
P2P mapping revoke
multi-GPU UVM
GPU reset
```

都应该沿用这一套 lifetime 分解方式，而不是重新把问题简化成一个 `tlb_flush()`。
