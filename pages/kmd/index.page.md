---
layout: default
title: "GPU KMD Owner Direction"
nav_order: 10
permalink: "/kmd_owner_direction/"
---

# GPU KMD Owner Direction

这是 **Time Update Tasks** 下的一个独立 update task，当前以 **GPU Memory / Virtual Memory / Unified Memory** 为主 Owner 方向组织每周技术更新。

## 每期做什么

- **L4**：Memory / UVM / HMM / SVM / GPUVM / fault / migration / TLB / residency 等 Owner 核心主题。
- **L3**：DMA-BUF、P2P、IOMMU/IOMMUFD、virtualization-memory 等与 Memory 强关联主题。
- **L1**：其它 GPU KMD 方向的行业/上游变化，只保留必要 Radar。

```text
Weekly Web Output
      │
      ├── A: L3/L4 Key Topic List
      │        ├── Memory Timeline
      │        └── selected ≤3 → Focus
      ├── B: Key Topic Deep Dive
      │        └── Focus pages
      ├── C: Other Topic Radar
      │        └── Other Topic Timeline
      └── Full reviewed output
               └── Web Update Archive
```

当前 GitHub Pages 从 **Weekly #13 · 2026-11-07** 重新开始。

- [GPU Memory / Virtual Memory / Unified Memory]({{ '/kmd_owner_direction/memory/' | relative_url }})
- [Other Topic]({{ '/kmd_owner_direction/other-topic/' | relative_url }})
- [Web Update Archive]({{ '/kmd_owner_direction/web-update-archive/' | relative_url }})
