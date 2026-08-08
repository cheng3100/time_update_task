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
### 2026-08-08 · Test #2
1. **Migration granularity is promoted to an explicit second-stage architecture item.**
   - Source: Linux DRM GPU SVM RFC / `drm_pagemap`: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Change: the current roadmap explicitly includes compound device pages and higher-order DMA mapping for migration; NVIDIA/AMD/Intel are recorded as agreeing that migrate-device core-MM calls are a performance bottleneck.
   - KMD impact: do not encode 4 KiB as the lifetime/ownership unit. Separate CPU base-page size, migration unit, DMA mapping unit and GPU PTE unit.
   - Priority: **Architecture now; prototype 64K/2M or batched migration in 6–12 months.**

2. **Multi-GPU and mixed system/device residency remain active common-SVM targets.**
   - Source: same GPU SVM RFC.
   - KMD impact: keep fault/migration metadata capable of representing mixed residency and future per-device residency without rewriting the single-GPU fault path.
   - Priority: **6–12 months / longer-term depending on multi-GPU hardware.**

3. **Driver-side migration policy remains open above common mechanisms.**
   - KMD impact: preserve mechanism/policy separation for future eviction, NUMA, preferred-location and workload-hint policies.
   - Priority: **Boundary now; policy later.**

### 2026-08-08 · Test #1
1. **Linux DRM GPU SVM is converging on a common shared-memory layer.**
   - Source: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Change: common design covers notifiers/ranges, system↔device migration and device-private memory, with concurrent GPU faults, mixed pages and common userptr in follow-on work.
   - KMD impact: keep a clear hardware-specific GPUVM/fault layer underneath a Linux-MM-facing abstraction.
   - Priority: **Now**.

2. **Multi-GPU and compound device pages are explicit follow-on targets.**
   - Priority: **6–12 months after baseline migration.**

3. **Driver-side migration policy remains intentionally open.**
   - Priority: **Longer-term**, but design the boundary now.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
