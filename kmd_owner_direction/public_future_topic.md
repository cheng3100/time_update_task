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

## Each update must answer
1. What new kernel/DRM/Accel/upstream mechanisms could change GPU KMD architecture in 1–3 years?
2. Which are worth prototyping or designing for now?
3. Which are still community/research directions and should not consume current engineering bandwidth?
