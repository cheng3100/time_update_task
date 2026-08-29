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
Recoverable GPU fault + HMM + CPU/GPU migration + replay, with fault/migration measurement and lifetime/race correctness designed into the first implementation.

### Near-term feature path
Recoverable fault → PASID/VM lookup → HMM/CPU PTE resolution → CPU↔VRAM migration → GPU PTE update → TLB invalidate → fault replay, with per-phase metrics and generation/race validation.

# Detailed Owner Growth Roadmap

This roadmap is the long-term depth path for the Memory owner. It is intentionally more detailed than the stable owner summary and should evolve by adding concrete implementation milestones, while the overall progression remains stable unless the owner direction itself changes.

## Stage 1 — Entry: Recoverable GPU Fault + HMM + Migration + Replay

### Goal
Build one complete recoverable shared-memory fault path instead of a collection of isolated memory helpers.

### End-to-end closure

```text
GPU memory access
      ↓
GPU page fault packet
      ↓
PASID / VM / context lookup
      ↓
process mm_struct + CPU VA resolution
      ↓
HMM / CPU PTE state inspection
      ↓
resident-page decision
      ↓
optional CPU→VRAM migration
      ↓
GPU page-table update
      ↓
TLB invalidate
      ↓
fault replay / resume
```

### Core KMD topics to own
- GPU fault packet format and recoverable/unrecoverable classification
- PASID/VM/context/process lifetime and lookup
- `mm_struct`, `mmu_notifier`, invalidation ordering and races
- HMM range / CPU PTE interpretation
- pinned vs pageable memory semantics
- CPU and GPU page-table consistency
- migration-copy engine interaction
- GPU PTE update and TLB invalidation ordering
- replay, duplicate fault, concurrent fault and process-exit handling
- failure rollback: migration failure, OOM, invalid VA, process teardown, reset during fault
- measurement contract: fault/get-pages/migration/copy/bind/TLB phase counts and latency

### First 3–6 month deliverable
A debuggable single-GPU path supporting one defined pageable-memory scenario end to end, with tracepoints/counters for fault → resolve → map/migrate → replay, explicit lifetime/error handling, and enough measurement to identify where the latency is spent.

### Owner capability formed
At the end of this stage, the owner should be able to reason across Linux MM, GPUVM, firmware fault delivery, DMA/migration and GPU MMU instead of only maintaining a BO allocator or page-table helper.

---

## Stage 2 — Deepen: GPUVM Architecture + Migration Granularity + Oversubscription

### Goal
Turn the first working fault/migration path into a scalable memory-management subsystem.

### 2.1 GPUVM depth
- GPU VA lifecycle and address-space ownership
- VMID/PASID allocation and reuse
- page-table hierarchy, PTE formats and protection attributes
- sparse mappings / reserved VA / partial residency
- huge/large pages and mixed page sizes
- TLB shootdown/invalidation granularity and batching
- VM_BIND / async mapping model compatibility
- concurrent map/unmap/fault synchronization

### 2.2 Migration granularity
Do not assume all memory-management units are 4 KiB.

Separate explicitly:

```text
CPU base page
   ≠ migration unit
   ≠ DMA mapping unit
   ≠ GPU PTE unit
   ≠ TLB invalidate unit
```

Progression:

```text
4K correctness
   ↓
batched 4K migration
   ↓
64K / HW-native page experiment
   ↓
2M / compound device page / higher-order DMA
```

Measure MM-call/get-pages overhead, DMA-map cost, copy-engine setup/data cost, page-table bind/update cost, TLB cost, internal fragmentation, false migration and CPU↔GPU bouncing separately.

### 2.3 Oversubscription / eviction / reclaim
- VRAM pressure accounting
- residency state machine
- eviction candidate selection
- VRAM→system migration
- fault-driven repopulation
- working-set protection
- reclaim interaction and OOM behavior
- per-process/context memory accounting
- policy/mechanism separation

### 6–18 month deliverable
A memory subsystem that supports repeated fault/migrate/evict cycles under pressure, mixed page granularity where hardware permits, and a stable GPUVM lifetime model rather than a one-shot HMM demo.

### Owner capability formed
The owner becomes responsible for memory correctness, scalability and pressure behavior, not only shared-VA enablement.

---

## Stage 3 — Expand: SVM/SVA + IOMMU + NUMA + Cross-device Memory

### Goal
Expand from one GPU's local memory model to the full host-device address and placement topology.

### 3.1 IOMMU / SVA integration
- PASID end-to-end ownership
- IOMMU page-table vs GPU page-table responsibilities
- SVA binding and process address-space sharing
- ATS translation caching
- PRI page requests and recoverable device faults
- device-TLB invalidation ordering
- IOMMU isolation/security interaction

Architectural question to continuously answer:

> When should the GPU own translation state, when should the IOMMU/SMMU own it, and when should they share one process address space?

### 3.2 NUMA placement
- CPU NUMA node vs GPU locality
- host-memory allocation policy for GPU-visible pages
- topology-aware migration
- remote-memory penalty measurement
- preferred location / access-pattern hints

### 3.3 dma-buf / P2P memory
- cross-device memory export/import lifecycle
- attachment/map/unmap synchronization
- peer memory visibility
- ownership and invalidation across devices
- boundary with Multi-GPU owner: Memory owns page residency/lifetime/policy; Multi-GPU owns topology, connectivity and peer transport mechanism.

### 1–2 year deliverable
A coherent memory architecture spanning CPU virtual memory, GPU page tables, IOMMU/SVA and peer-visible memory, with explicit ownership boundaries and topology-aware placement hooks.

### Owner capability formed
The Memory owner becomes the system-level authority for address translation and residency across CPU + GPU + IOMMU rather than only the GPU's local MMU.

---

## Stage 4 — Evolve: Multi-GPU UVM + Heterogeneous / Tiered / CXL Memory + Policy

### Goal
Move from mechanism ownership to heterogeneous-memory architecture and policy.

### 4.1 Multi-GPU unified memory
- one CPU VA visible to multiple GPUs
- per-GPU residency metadata
- GPU0↔GPU1 migration
- replication vs migration
- preferred GPU / access affinity
- shared VM / peer PTE consistency
- concurrent faults from multiple GPUs
- topology-aware placement and migration cost

### 4.2 Heterogeneous / tiered memory
Potential tiers:

```text
CPU DRAM
GPU local VRAM
peer GPU VRAM
CXL / pooled memory
future device-private tiers
```

Own the abstraction for:
- memory-tier capabilities
- latency/bandwidth/capacity properties
- migration eligibility
- placement constraints
- reclaim hierarchy
- hot/cold data movement

### 4.3 Policy layer
Only after the mechanisms are trustworthy:
- preferred-location hints
- access counters / hotness
- migration thresholds
- replication policy
- NUMA/topology-aware placement
- workload-aware memory QoS
- tenant/accounting constraints
- future programmable policy hooks

The policy layer must remain separable from basic correctness mechanisms so algorithms can evolve without destabilizing GPUVM/HMM lifetime rules.

### 2–5 year target
Own the architecture for unified heterogeneous memory across CPU, one or more GPUs and future memory tiers, including both Linux-MM integration and GPU-specific residency/migration semantics.

### Owner capability formed
This is the final long-term role: **GPU Memory / UVM / Heterogeneous Memory Architecture Owner**, capable of making cross-subsystem decisions spanning Linux MM, DRM/GPUVM, IOMMU, firmware, copy engines, multi-GPU topology and hardware MMU/page-size capabilities.

---

## Recommended learning / implementation sequence

```text
1. GPUVM + page-table lifetime
        ↓
2. mmu_notifier / HMM + recoverable fault
        ↓
3. migration + replay correctness + measurement
        ↓
4. migration granularity / large pages
        ↓
5. eviction / oversubscription / pressure
        ↓
6. IOMMU / PASID / ATS / PRI / SVA
        ↓
7. NUMA + dma-buf/P2P memory
        ↓
8. multi-GPU UVM
        ↓
9. tiered/CXL heterogeneous memory
        ↓
10. placement / migration / memory-QoS policy
```

The key principle is **mechanism before policy, lifetime/correctness before optimization, measurement before granularity tuning, single-GPU closure before multi-GPU policy**.

## Boundary with other owners
- **Multi-GPU / Fabric:** owns device identity, topology, links, P2P transport and fabric health; Memory owns page residency, migration, shared-VM semantics and placement policy.
- **Firmware / Control Plane:** owns protocol/lifecycle/capability mechanism; Memory defines memory-service semantics such as fault replay, migration commands and MMU-state requirements.
- **Reliability / RAS:** owns system failure containment/recovery; Memory owns VM/page-table/migration state and provides restore/snapshot primitives.
- **Virtualization / Security:** owns tenant/resource isolation; Memory owns per-VM memory mappings/residency mechanisms and memory accounting primitives consumed by virtualization.
- **Observability:** owns tracing/profiling infrastructure; Memory defines stable memory event semantics (fault, bind, migrate, evict, TLB invalidate, replay) and the metrics required to compare memory mechanisms.

## Industry Updates
### 2026-08-29 · Weekly #3
1. **AMDGPU UALink makes future multi-GPU memory invalidation a concrete ownership/protocol problem.**
   - Source: https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html (2026-08-21)
   - Change: remote GPU memory uses NPA mappings and explicit export/import authorization; exported memory may move or be revoked by TTM eviction/MMU notifier, requiring remote TLB shootdown plus importer presence-check/retry rather than permanent pinning.
   - KMD impact: keep the current single-GPU fault/HMM implementation as P0, but preserve separate logical allocation/range, local residency/PTE, peer mapping, invalidation target and connection/mapping generations. A future remote invalidation protocol cannot be modeled as merely iterating local TLB flushes.
   - Priority: **Single-GPU correctness now; remote invalidation architecture reserve only.**

2. **No new common GPU-SVM mechanism changes the current entry path this week.**
   - Reference: https://docs.kernel.org/next/gpu/rfc/gpusvm.html
   - KMD impact: continue measurement-first, notifier/generation correctness and N:1/per-device-state evolvability.
   - Priority: **Now.**

### 2026-08-15 · Weekly #1
1. **Xe GT Statistics turns SVM migration granularity into a measurable engineering problem.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_gt_stats.html (`next-20260722` documentation)
   - Change: Xe exposes SVM fault count/time, TLB invalidation count/time, 4K/64K/2M fault and migration counters, CPU/device copy time/bytes, get-pages time, bind time and page-reclaim-list statistics.
   - KMD impact: the first recoverable-fault implementation should already define a measurement contract so later batched-4K/64K/2M experiments can attribute cost to MM/get-pages, copy, PTE bind or TLB instead of guessing.
   - Priority: **Measurement schema now; 64K/2M prototype in 6–12 months.**

2. **GPU SVM / drm_pagemap direction remains stable rather than changing this week.**
   - Source: https://docs.kernel.org/next/gpu/rfc/gpusvm.html
   - KMD impact: continue to keep logical CPU-range identity, per-device residency, DMA mapping and GPU-PTE state decoupled; N:1/multi-device evolvability remains important.
   - Priority: **Design compatibility now.**

### 2026-08-08 · Test #2
1. **Migration granularity is promoted to an explicit second-stage architecture item.**
   - Source: Linux DRM GPU SVM RFC / `drm_pagemap`: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - KMD impact: do not encode 4 KiB as the lifetime/ownership unit. Separate CPU base-page size, migration unit, DMA mapping unit and GPU PTE unit.
   - Priority: **Architecture now; prototype 64K/2M or batched migration in 6–12 months.**
2. **Multi-GPU and mixed system/device residency remain active common-SVM targets.**
   - Priority: **6–12 months / longer-term depending on multi-GPU hardware.**
3. **Driver-side migration policy remains open above common mechanisms.**
   - Priority: **Boundary now; policy later.**

### 2026-08-08 · Test #1
1. **Linux DRM GPU SVM is converging on a common shared-memory layer.**
   - Source: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
   - Priority: **Now**.
2. **Multi-GPU and compound device pages are explicit follow-on targets.**
3. **Driver-side migration policy remains intentionally open.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
