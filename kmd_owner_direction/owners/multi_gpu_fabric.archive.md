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
Multi-GPU enumeration + stable identity + topology/port/peer model + visibility/affinity + directional P2P capability matrix.

### Near-term feature path
Stable device identity → topology graph / endpoint-port-peer model → process-visible GPU set/affinity → directional P2P capability + reason matrix → peer mapping → P2P DMA → link/fabric control primitives → shared VM → multi-GPU UVM/fabric.

## Industry Updates
### 2026-08-29 · Weekly #3
1. **DRM Fabric RFC proposes a vendor-neutral accelerator topology object model.**
   - Source: https://lkml.iu.edu/2608.3/00335.html (2026-08-24)
   - Change: proposes protocol-agnostic `fabric → endpoint → port → peer` objects. A peer is a typed identity/value descriptor rather than necessarily a live local object; topology represents direct adjacency rather than end-to-end reachability; port state/counters may be reported by providers.
   - KMD impact: the current topology/P2P feature should evolve beyond a GPU×GPU boolean matrix. Model directed port/peer identity, link state/counters, capability and failure reason while leaving vendor FW/memory/data-path semantics outside the common topology layer.
   - Priority: **Refine the topology data model now.**

2. **AMD UALink turns fabric remote memory/control into concrete KMD implementation.**
   - Source: https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html (2026-08-21)
   - Change: the large AMDGPU series adds pod/station configuration, NPA translation, remote state, remote TLB shootdown/interrupt, export/import/revoke, connection reset and remote PTE mapping.
   - KMD impact: Multi-GPU should own topology/link/control primitives and connection lifecycle; Memory should continue to own residency/migration/shared-VA policy layered above them.
   - Priority: **Topology/control model now; actual fabric data path only when hardware exists.**

### 2026-08-15 · Weekly #1
1. **No new production-level direction change was found this run.**
   - Current research reference: https://arxiv.org/abs/2607.26335
   - Observation: `fabric_ext` remains a useful long-term signal that movement, ordering, ownership and link-health may eventually become explicit fabric semantics, but it is not evidence that programmable fabric policy should enter a production KMD now.
   - KMD impact: keep topology-first sequencing: stable identity/topology/P2P capability primitives now; shared VM and programmable fabric policy later.
   - Priority: **Topology/P2P now; fabric policy long-term.**

2. **GPU SVM N:1 per-device mapping state continues to support the owner boundary.**
   - Source: https://docs.kernel.org/next/gpu/rfc/gpusvm.html
   - KMD impact: Multi-GPU owns identity/topology/peer transport; Memory owns per-device residency/migration/shared-VA policy layered on top.
   - Priority: **Design compatibility now.**

### 2026-08-08 · Test #4
1. **`fabric_ext` elevates movement, ordering and ownership into explicit fabric semantics.**
   - Source: https://arxiv.org/abs/2607.26335 (2026-07-28)
   - KMD impact: long-term Fabric interfaces may need movement/ownership/ordering/link-health metadata, not only a boolean peer-copy capability.
   - Priority: **Long-term watch; do not productize programmable policy now.**

2. **GPU SVM N:1 per-device mapping state reinforces topology-first / shared-VA-later sequencing.**
   - Source: https://docs.kernel.org/gpu/rfc/gpusvm.html
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
