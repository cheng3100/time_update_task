---
layout: default
title: "GPU Memory / Virtual Memory / Unified Memory"
parent: "GPU KMD Owner Direction"
nav_order: 1
permalink: "/kmd_owner_direction/memory/"
---

# GPU Memory / Virtual Memory / Unified Memory

这是当前更新任务的主 Owner 方向。

关注 GPU memory object 在 **地址空间、backing/residency、fault/migration、translation cache、sharing/P2P、lifetime** 之间如何保持正确性与可扩展性。

```text
Application / Runtime
        │
        ▼
CPU VA / GPU VA
        │
        ▼
GPUVM / HMM / SVM
        │
        ├── Fault / Replay
        ├── Migration / Residency / Eviction
        ├── PTE / TLB / Lifetime
        └── Sharing
             ├── DMA-BUF
             ├── IOMMU / IOMMUFD
             └── P2P / Multi-device
```

- [Timeline]({{ '/kmd_owner_direction/memory/timeline/' | relative_url }})
- [Focus]({{ '/kmd_owner_direction/memory/focus/' | relative_url }})
