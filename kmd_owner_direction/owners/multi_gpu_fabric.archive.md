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
### 2026-08-08 · Test #4
1. **`fabric_ext` elevates movement, ordering and ownership into explicit fabric semantics.**
   - Source: https://arxiv.org/abs/2607.26335 (2026-07-28)
   - KMD impact: long-term Fabric interfaces may need movement/ownership/ordering/link-health metadata, not only a boolean peer-copy capability.
   - Priority: **Long-term watch; do not productize programmable policy now.**

2. **GPU SVM N:1 per-device mapping state reinforces topology-first / shared-VA-later sequencing.**
   - Source: https://docs.kernel.org/next/gpu/rfc/gpusvm.html
   - KMD impact: Multi-GPU owns identity/topology/peer capability; Memory can then layer per-device residency/migration/shared-VA semantics on top.
   - Priority: **Design compatibility now.**

### 2026-08-08 · Test #2
1. **`fabric_ext` strengthens the case for treating movement/ownership telemetry as part of future Fabric architecture.**
   - Source: https://arxiv.org/abs/2607.26335 (2026-07-28)
   - Change: proposes cross-layer eBPF policy spanning GPU, DPU/NIC and CXL fabric hooks around a semantic movement graph.
   - KMD impact: long-term topology/fabric interfaces may need to expose movement, ordering, ownership and link-health semantics, not only `peer_copy()` capability.
   - Priority: **Long-term watch; do not productize now.**

2. **NCCLbpf shows collective policy programmability is emerging above the KMD.**
   - Source: https://arxiv.org/abs/2603.11438
   - KMD impact: keep collective scheduling out of the KMD owner for now, but expose stable topology/link/health primitives so upper runtimes can make policy decisions.
   - Priority: **Long-term watch.**

3. **DRM GPU SVM multi-GPU work reinforces topology-first sequencing.**
   - Source: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Priority: **Now for identity/topology/P2P matrix; shared VM later.**

### 2026-08-08 · Test #1
1. **DRM GPU SVM explicitly lists multi-GPU as follow-on work.**
2. **Device-to-device fast interconnect is entering memory-management design.**
3. **Programmable GPU/CXL fabric policy is a long-term research signal.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
