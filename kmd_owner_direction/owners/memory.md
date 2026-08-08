# GPU Memory / Virtual Memory / Unified Memory

## Stable Summary
Own GPU memory architecture from GPUVM through Linux MM integration and unified/heterogeneous memory. This is the KMD leader depth line.

## Living Sub-directions
- GPUVM/page tables, VMID/PASID, TLB, sparse/large pages
- recoverable GPU page fault and replay
- mmu_notifier, HMM/SVM, device-private memory
- CPU↔GPU migration, oversubscription and eviction
- NUMA and compound/large device pages
- IOMMU/ATS/PRI/PASID/SVA
- dma-buf/P2P memory and multi-GPU unified memory
- heterogeneous/tiered/CXL memory and memory QoS

## Current Entry Feature
Recoverable GPU fault + HMM + CPU/GPU migration + replay.

## Industry Updates
### 2026-08-08
- Linux DRM GPU SVM / drm_pagemap is pushing common abstractions for system RAM ↔ device memory migration, device-private pages, and future multi-GPU/compound-page support.
- Follow-up: **Now** — keep HMM/migration architecture compatible with emerging common abstractions.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
