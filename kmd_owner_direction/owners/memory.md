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

### Near-term feature path
Recoverable fault → PASID/VM lookup → HMM/CPU PTE resolution → CPU↔VRAM migration → GPU PTE update → TLB invalidate → fault replay.

## Industry Updates
### 2026-08-08

1. **Linux DRM GPU SVM is converging on a common shared-memory layer.**
   - Source: Linux kernel GPU SVM RFC / `drm_pagemap`: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Change: the common design covers notifiers/ranges, system↔device migration and device-private memory, and explicitly lists concurrent GPU faults, mixed system/device pages and common userptr as follow-on work.
   - KMD impact: avoid baking HMM/SVM semantics entirely into a vendor-private layer; keep a clear hardware-specific GPUVM/fault layer underneath a Linux-MM-facing abstraction.
   - Priority: **Now**.

2. **Multi-GPU and compound device pages are explicit follow-on targets.**
   - Source: same GPU SVM RFC.
   - Change: multi-GPU support is work in progress; NVIDIA/AMD/Intel agree that migrate-device core-MM costs are a bottleneck and compound device pages can reduce that overhead. Higher-order DMA mapping (for example 2 MiB) is also called out for migration performance.
   - KMD impact: after the basic 4 KiB migration loop works, migration granularity and page-size abstraction should become a second-stage architecture feature rather than an afterthought.
   - Priority: **6–12 months** after baseline migration.

3. **Driver-side migration policy remains intentionally open.**
   - Source: same GPU SVM RFC.
   - Change: driver-side madvise and migration policies are listed as future work rather than fixed common policy.
   - KMD impact: retain policy/mechanism separation so residency, eviction, NUMA and workload hints can evolve without rewriting the fault/migration mechanism.
   - Priority: **Longer-term**, but design the boundary now.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
