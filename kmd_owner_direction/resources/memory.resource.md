# Memory / Virtual Memory / Unified Memory — Learning Resources

## GPUVM / page tables / VMID / PASID / TLB
- [AMDGPU driver documentation index](https://docs.kernel.org/gpu/amdgpu/index.html) — Read the VM, MMU notifier, memory-domain and BO sections together to understand how a production KMD connects GPUVM to the rest of DRM.

## Recoverable GPU page fault / replay
- [Linux GPU SVM / drm_pagemap RFC](https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html) — Best current upstream design document for GPU fault-driven shared memory, device-private pages and migration boundaries.

## mmu_notifier / HMM / SVM / device-private memory
- [Heterogeneous Memory Management (HMM)](https://docs.kernel.org/mm/hmm.html) — Core Linux MM reference for CPU page-table mirroring, SVM and device memory integration.
- [MMU notifier ordering rules](https://docs.kernel.org/mm/mmu_notifier.html) — Essential for COW, PTE replacement and device-TLB correctness.

## CPU↔GPU migration / oversubscription / eviction
- [Linux GPU SVM / drm_pagemap RFC](https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html) — Focus on migration, unbind handling, residency conflicts and future driver-side policy.

## NUMA / large & compound pages / higher-order DMA
- [Linux GPU SVM / drm_pagemap RFC](https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html) — Explicitly discusses compound device pages and higher-order DMA mapping as migration-performance directions.

## IOMMU / ATS / PRI / PASID / SVA
- [Linux Shared Virtual Addressing](https://www.kernel.org/doc/html/latest/arch/x86/sva.html) — Compact but high-value reference tying SVA to ATS, PRI, PASID, IOMMU and mmu_notifier.

## dma-buf / P2P memory / multi-GPU sharing
- [DMA-BUF sharing and synchronization](https://docs.kernel.org/driver-api/dma-buf.html) — Canonical reference for exporter/importer ownership, attachments, dma-fence and dma-resv.

## Multi-GPU UVM / heterogeneous or CXL memory / memory QoS
- [Linux GPU SVM / drm_pagemap RFC](https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html) — Best common-layer reference today for future multi-device device-memory semantics; use with the Multi-GPU resource library for topology/fabric mechanics.
