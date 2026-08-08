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
### 2026-08-08 · Test #2
1. **ProfInfer strengthens the unified trace + hardware-counter direction.**
   - Source: https://arxiv.org/abs/2601.20755
   - Change: uses eBPF probes to correlate runtime functions/operator timelines with hardware-counter trends at low overhead.
   - KMD impact: avoid separate “debug trace” and “performance profiling” data models; define one timestamp/object identity model that PMU samples can join later.
   - Priority: **Trace now; unified timeline in 6–12 months.**

2. **AMD uProf 5.3 shows production profiling consuming GPU hardware events through ROCm/rocprofiler.**
   - Source: https://docs.amd.com/r/en-US/57368-uProf-user-guide/7.13.1.-GPU-Profiling
   - KMD impact: PMU counter discovery, naming, grouping/multiplexing and per-context attribution should be treated as first-class KMD interfaces when hardware supports them.
   - Priority: **6–12 months.**

3. **`gpu_ext` / `fabric_ext` remain research signals, not immediate product APIs.**
   - Sources: https://arxiv.org/abs/2512.12615 and https://arxiv.org/abs/2607.26335
   - KMD impact: build stable hooks and correlation primitives now; postpone programmable policy until verifier/security/uAPI constraints are much clearer.
   - Priority: **Long-term policy watch.**

### 2026-08-08 · Test #1
1. **Linux perf provides a mature model for complex fabric/system PMUs.**
2. **`gpu_ext` explores verified eBPF GPU-driver policy hooks.**
3. **Cross-layer programmable observability is expanding toward GPU/CXL fabrics.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
