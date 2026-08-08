# GPU Observability / Profiling / Programmable Driver Infrastructure

## Stable Summary
Own software-event tracing, hardware performance monitoring, cross-layer correlation and programmable diagnostics. eBPF is an entry technology, not the owner identity.

## Living Sub-directions
- stable KMD tracepoint/event model
- BTF/CO-RE and eBPF dynamic tracing
- PID/PASID/VM/context/queue/job correlation
- GPUVM/fault/migration tracing
- firmware/KMD/UMD unified timeline
- per-process/context latency and performance attribution
- dynamic diagnostics and fault-injection hooks
- GPU PMU counter discovery, allocation/multiplexing and sampling
- SM/CU/cache/memory/fabric/engine counters
- profiling uAPI and Linux perf/perf_event integration
- tenant-safe counter virtualization
- long-term gpu_ext-like verified programmable policy

## Current Entry Feature
eBPF-based GPU KMD dynamic tracing. Second entry when HW PMU is mature: PMU counter enumeration + per-process/context profiling.

### Near-term feature path
Stable tracepoints → PID/PASID/VM/context/queue/job correlation → KMD/FW timeline → PMU counter integration → bottleneck attribution → dynamic diagnostics → verified programmable hooks.

## Industry Updates
### 2026-08-08

1. **Linux perf provides a mature model for complex fabric/system PMUs.**
   - Source: NVIDIA Tegra241 PMU documentation: https://cdn.kernel.org/doc/html/latest/admin-guide/perf/nvidia-tegra241-pmu.html
   - Change: standard perf PMU infrastructure exposes bandwidth, latency and utilization counters across SCF, NVLink-C2C and PCIe-style system fabrics.
   - KMD impact: if the GPU HW counter block is suitable, prefer a Linux perf/perf_event-compatible abstraction instead of a completely private profiling stack; keep GPU-specific session/security needs layered on top.
   - Priority: **6–12 months** when HW PMU is ready.

2. **`gpu_ext` explores the GPU driver/device as a verified eBPF policy surface.**
   - Source: `gpu_ext: Extensible OS Policies for GPUs via eBPF` (2025-12): https://arxiv.org/abs/2512.12615
   - Change: the research exposes safe GPU-driver/device hooks for memory placement, scheduling and observability while retaining verifier-based policy safety.
   - KMD impact: near-term value is not “run eBPF on GPU”; it is to design stable event/object identities and trace hooks that could later support programmable diagnostics or policy.
   - Priority: **Now for observability primitives; long-term for policy hooks**.

3. **Cross-layer programmable observability is expanding toward GPU/CXL fabrics.**
   - Source: `fabric_ext` (2026-07-28): https://arxiv.org/abs/2607.26335
   - Change: the work proposes consistent observation/policy points across GPU, NIC/DPU and CXL movement paths.
   - KMD impact: reinforces the value of a unified object/event model and timestamps that can correlate KMD, FW, DMA, memory placement and fabric events.
   - Priority: **Long-term watch**, but timestamp/object-correlation design should not block future extension.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
