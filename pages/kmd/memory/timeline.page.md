---
layout: default
title: "Timeline"
parent: "GPU Memory / Virtual Memory / Unified Memory"
nav_order: 1
permalink: "/kmd_owner_direction/memory/timeline/"
---

# Memory / UVM Timeline

按每次更新日期追加。标题直接指向 primary/upstream reference；若该条进入当期 B Deep Dive，则额外提供 **Focus →**。

## 2026-11-07 · Weekly #13

### [AMDGPU: TLB invalidation completion 与 BO lifetime](https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html)

AMDGPU 修复 GPUVA unmap 与 GEM object close 之间的 lifetime race：PTE 已删除时，相关 TLB invalidation 仍可能尚未完成，因此 BO backing 不能提前复用。  
[Focus →]({{ '/kmd_owner_direction/memory/focus/2026-11-07-tlb-bo-lifetime/' | relative_url }})

### [DMA-BUF Mapping Types v2/23](https://lists.openwall.net/netdev/2026/11/05/140)

DMA-BUF 开始从固定 `sg_table + dma_addr_t` 模型走向 importer/exporter 可协商的 mapping representation，以覆盖 VRAM、P2P、IOMMUFD 等场景。  
[Focus →]({{ '/kmd_owner_direction/memory/focus/2026-11-07-dmabuf-mapping-types/' | relative_url }})

### [PCIe P2P: topology reachable ≠ DMA addressable](https://lists.openwall.net/linux-kernel/2026/11/04/194)

AMDGPU 补充 importer DMA addressability 检查：PCIe topology 可达并不意味着 DMA mask 一定能够覆盖 exporter VRAM BAR。  
[Focus →]({{ '/kmd_owner_direction/memory/focus/2026-11-07-pcie-p2p-addressability/' | relative_url }})
