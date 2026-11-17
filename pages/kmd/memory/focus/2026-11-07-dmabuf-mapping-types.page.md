---
layout: default
title: "2026-11-07 · DMA-BUF Mapping Types"
parent: "Focus"
ancestor: "GPU Memory / Virtual Memory / Unified Memory"
nav_order: 2
permalink: "/kmd_owner_direction/memory/focus/2026-11-07-dmabuf-mapping-types/"
---

# L3 — DMA-BUF Mapping Types：为什么 `sg_table` 开始不够了

## 0. 问题背景

传统 dma-buf attachment mapping 以 `sg_table` 为核心，但 VRAM、PCIe P2P、IOMMUFD、vGPU/XGMI 等场景需要的 mapping representation 并不天然等价于普通 `dma_addr_t`。

- https://lists.openwall.net/netdev/2026/11/05/140
- https://lists.openwall.net/netdev/2026/11/05/152
- https://github.com/torvalds/linux/blob/master/drivers/dma-buf/dma-buf.c
- https://github.com/torvalds/linux/blob/master/include/linux/dma-buf.h

```text
Memory Object
      ≠
Mapping Representation
      ≠
Device Accessibility
```
