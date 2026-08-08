# GPU Memory / Virtual Memory / Unified Memory

## Summary (stable)
Own GPU memory architecture from GPUVM through Linux MM integration and unified/heterogeneous memory. This is the KMD leader's fixed depth direction.

## Candidate sub-directions
- GPUVM/page tables, VMID/PASID, TLB invalidation, sparse/large pages
- recoverable GPU page fault and fault replay
- mmu_notifier, HMM, SVM, device-private memory
- CPU↔GPU migration, eviction and VRAM oversubscription
- NUMA placement and compound/large device pages
- IOMMU, ATS, PRI, PASID, SVA
- dma-buf/P2P memory integration
- multi-GPU unified memory and GPU↔GPU migration policy
- heterogeneous/tiered/CXL memory and memory QoS

## Current entry feature
**Recoverable GPU fault + HMM + CPU/GPU migration + replay.**

## Living focus
Track Linux DRM GPU SVM/drm_pagemap evolution, migration granularity, compound device pages, oversubscription and multi-GPU memory semantics.
