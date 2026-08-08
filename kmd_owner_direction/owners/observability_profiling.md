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

## Industry Updates
### 2026-08-08
- Linux perf already supports complex system/uncore PMUs, while research such as gpu_ext explores verified eBPF hooks for GPU observability and policy.
- Follow-up: **Now** — build eBPF trace and object correlation; **later** unify PMU samples into the same timeline; programmable policy remains longer-term research.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
