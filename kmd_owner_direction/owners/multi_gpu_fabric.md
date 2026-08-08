# Multi-GPU / P2P / Fabric

## Stable Summary
Own the multi-device model, topology/connectivity mechanisms and peer/fabric infrastructure. Memory residency/migration policy stays with Memory.

## Living Sub-directions
- multi-GPU enumeration and stable physical/logical identity
- logical index↔BDF/minor mapping
- device visibility, allowed masks and affinity
- container/namespace/cgroup resource-control integration
- PCIe/NUMA/switch topology and distance matrix
- P2P capability discovery/matrix
- peer BAR/VRAM mapping and peer PTE
- P2P DMA and cross-GPU dma-buf
- shared VA/multi-GPU VM
- fabric/link health, reset and RAS

## Current Entry Feature
Multi-GPU enumeration + topology + visibility/affinity + P2P capability matrix.

### Near-term feature path
Stable device identity → topology graph → process-visible GPU set/affinity → P2P capability matrix → peer mapping → P2P DMA → shared VM → multi-GPU UVM/fabric.

## Industry Updates
### 2026-08-08

1. **DRM GPU SVM explicitly lists multi-GPU as follow-on work.**
   - Source: Linux kernel GPU SVM RFC: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Change: multi-GPU support is called out as work in progress after the initial GPU SVM layer lands, ideally with limited changes to the common SVM core.
   - KMD impact: build the multi-device/topology layer independently from migration policy so later shared-VM work can consume it rather than redesign device identity and peer capability.
   - Priority: **Now** for enumeration/topology/P2P capability; shared VM later.

2. **Device-to-device fast interconnect is becoming part of the memory-management discussion, not only a copy-engine feature.**
   - Source: GPU SVM/drm_pagemap design direction.
   - Change: common memory abstractions are being designed with future peer/device memory in mind.
   - KMD impact: P2P capability must describe more than “can DMA copy”; include addressability, peer aperture, IOMMU/ACS constraints, peer PTE capability and synchronization semantics.
   - Priority: **6–12 months** after basic topology.

3. **Research is moving toward programmable policy across GPU/CXL fabrics.**
   - Source: `fabric_ext` (2026-07-28), “The Fabric Is the Cluster Driver: Cross-Layer eBPF Policies for GPU-CXL Fabrics”: https://arxiv.org/abs/2607.26335
   - Change: the work explores policy and observability spanning GPU, DPU/NIC and CXL/fabric movement paths.
   - KMD impact: this is not a near-term implementation target, but it reinforces that long-term fabric ownership includes topology, movement observability and policy boundaries, not only P2P copy APIs.
   - Priority: **Long-term watch**.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
