# GPU KMD Long-Term Owner Map

> Stable page. Change only after an explicit owner-direction decision.

| Owner domain | Stable scope | Current entry feature |
|---|---|---|
| Memory / Virtual Memory / Unified Memory | GPUVM, HMM/SVM, fault, migration, IOMMU/SVA, heterogeneous memory | Recoverable fault + HMM + migration + replay |
| Virtualization / Security | VFIO, SR-IOV, resource isolation, vGPU, confidential GPU | SR-IOV PF/VF provisioning if HW supports it; otherwise VFIO/reset/ownership assessment |
| Power / Performance | Utilization, DVFS, runtime PM, thermal, power cap | Busy/idle + utilization accounting → basic DVFS/runtime PM |
| Reliability / Recovery / RAS | Hang detection, dump, reset, containment, ECC/AER | Hang snapshot + devcoredump + reset reason + heartbeat/watchdog |
| Multi-GPU / P2P / Fabric | Device model, visibility, topology, P2P, shared VM, fabric | Enumeration + topology + visibility/affinity + P2P capability matrix |
| Observability / Profiling / Programmable Driver | eBPF/trace, PMU/profiling, unified timeline, programmable diagnostics | eBPF-based KMD dynamic tracing |
| Firmware / Control Plane | Versioned KMD↔FW protocol, lifecycle, capability model, state reconciliation | Versioned async protocol + capability negotiation |

## Public future-evolution topic

Not an owner task. Track only future-facing Linux GPU/accelerator kernel evolution: DRM/Accel common infrastructure, GPUVM/SVM abstractions, VM_BIND evolution, uAPI, upstream architecture, Rust GPU drivers, common recovery/telemetry/security/virtualization frameworks, and relevant MM/IOMMU/CXL/eBPF changes.

## Explicitly out of scope as owner directions

Basic KMD foundation already partially implemented: basic execution/submission, queue/context, basic scheduler, interrupts, probe/init, MMIO/PCIe bring-up. These may appear only when a new industry mechanism materially changes the architecture.
