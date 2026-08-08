# Public Future Evolution Topic

> This is a shared topic, not a dedicated owner task.

## Stable scope
Track future-facing Linux GPU/accelerator kernel evolution that may change KMD architecture in the next 1–3 years. Do not use this topic to re-document already-implemented basic KMD execution, queue, scheduling, interrupt, probe/init or MMIO/PCIe foundations.

## Watch areas
- DRM/Accel subsystem architecture and common infrastructure
- drm_gpuvm/drm_exec/drm_sched new capabilities and replacement/refactoring trends
- VM_BIND/async VM_BIND and future GPUVM/SVM common abstractions
- dma-buf/dma-fence/syncobj evolution
- accelerator/compute uAPI design
- render/device node, namespace, cgroup and resource-control mechanisms
- firmware-centric and hardware-scheduler KMD architectures
- common kernel frameworks for GPU reset/recovery, telemetry, security and virtualization
- Rust-for-Linux and Rust GPU-driver architecture
- upstream policy, uAPI stability, ABI/versioning and review expectations
- AMD/Intel/Nouveau/Nova/Linux accel architectural changes
- Linux MM/IOMMU/PCIe/CXL/eBPF changes that materially affect GPU KMD

## Current watch — 2026-08-08

### 1. DRM GPU SVM / drm_pagemap
- Source: https://www.kernel.org/doc/html/latest/gpu/rfc/gpusvm.html
- Why it matters: common DRM/MM abstractions are moving toward shared CPU/GPU virtual memory, device-private memory and migration rather than leaving all UVM semantics vendor-private.
- Team action: **design for compatibility now**; do not wait for every upstream API to stabilize before defining internal MM abstraction boundaries.

### 2. Nova / firmware-centric GPU driver architecture
- Source: https://docs.kernel.org/gpu/nova/index.html and https://docs.kernel.org/gpu/nova/core/todo.html
- Why it matters: Nova separates a first-level hardware/FW abstraction from upper DRM/VFIO consumers and explicitly treats unstable GSP firmware APIs as an architectural issue.
- Team action: **use as an architecture reference now**, especially for Firmware/Control Plane and future virtualization; do not copy the implementation mechanically.

### 3. Common crash delivery through devcoredump
- Source: https://www.kernel.org/doc/html/latest/gpu/xe/xe_devcoredump.html
- Why it matters: standardized “snapshot before reset, consume later” is a reusable kernel pattern for production GPU failure diagnostics.
- Team action: **worth implementing now** for Reliability/RAS.

### 4. eBPF-programmable GPU/fabric policy remains research-stage but is accelerating
- Sources: https://arxiv.org/abs/2512.12615 and https://arxiv.org/abs/2607.26335
- Why it matters: work is moving from host tracing toward verified policy hooks across GPU and GPU/CXL fabric paths.
- Team action: **do observability/event-model groundwork now; keep programmable policy as long-term research**, not a current product commitment.

## Each update must answer
1. What new kernel/DRM/Accel/upstream mechanisms could change GPU KMD architecture in 1–3 years?
2. Which are worth prototyping or designing for now?
3. Which are still community/research directions and should not consume current engineering bandwidth?
