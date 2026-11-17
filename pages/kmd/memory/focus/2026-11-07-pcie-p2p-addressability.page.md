---
layout: default
title: "2026-11-07 · PCIe P2P addressability"
parent: "Focus"
ancestor: "GPU Memory / Virtual Memory / Unified Memory"
nav_order: 3
permalink: "/kmd_owner_direction/memory/focus/2026-11-07-pcie-p2p-addressability/"
---

# L3 — PCIe P2P：Topology reachable ≠ DMA addressable

## 0. 问题背景

PCIe topology 可达只证明存在 peer route，并不能证明 DMA initiator 的 DMA mask、IOMMU mode 和 mapping representation 能真正覆盖 peer BAR aperture。

- https://lists.openwall.net/linux-kernel/2026/11/04/194
- https://github.com/torvalds/linux/blob/master/drivers/pci/p2pdma.c
- https://github.com/torvalds/linux/blob/master/kernel/dma/direct.c

```text
Topology reachability
       ≠
DMA addressability
       ≠
Usable P2P mapping
```
