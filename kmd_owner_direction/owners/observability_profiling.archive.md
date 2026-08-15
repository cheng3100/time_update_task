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
Stable GPU event/object identity + eBPF-based KMD dynamic tracing + low-overhead software counters. Second entry when HW PMU is mature: PMU counter enumeration + per-process/context profiling joined into the same timeline.

### Near-term feature path
Stable tracepoints/object IDs → always-on low-cost software counters → PID/PASID/VM/context/queue/job correlation → KMD/FW timeline → PMU counter integration → bottleneck attribution → dynamic diagnostics → verified programmable hooks.

## Industry Updates
### 2026-08-15 · Weekly #1
1. **Xe GT Statistics demonstrates a practical always-on KMD software-telemetry layer.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_gt_stats.html
   - Change: per-GT statistics cover SVM/TLB/migration/copy/bind/reclaim and scheduler wait/suspend paths; the implementation uses per-CPU counters to avoid expensive atomics/cache-coherency traffic on high-frequency paths.
   - KMD impact: Observability should not jump directly from tracepoints to HW PMU. Add a first layer of always-on software counters, then use stable object IDs/tracepoints for attribution and PMU for hardware bottlenecks.
   - Priority: **Software counters + object model now.**

2. **SysOM-AI continues to validate continuous cross-layer observability at production scale.**
   - Source: https://arxiv.org/abs/2603.29235
   - KMD impact: stable timestamps and CPU/GPU/NCCL/KMD object correlation are durable infrastructure rather than one-off debug scripts.
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **SysOM-AI demonstrates continuous cross-layer observability at production scale.**
   - Source: https://arxiv.org/abs/2603.29235
   - Change: combines CPU stack profiling, GPU kernel tracing and NCCL instrumentation with eBPF-based mechanisms; reports <0.4% overhead and deployment across more than 80,000 GPUs.
   - KMD impact: stable object IDs, timestamps and cross-layer correlation are durable infrastructure; build them before one-off profiler-specific interfaces.
   - Priority: **Trace/object model now.**

2. **Radeon GPU Profiler 2.7 reinforces the unified timeline + hardware-counter consumption model.**
   - Source: https://gpuopen.com/rgp/
   - KMD impact: GPU PMU should not become an isolated register-reading tool; counter discovery/sampling should correlate with queue/job/context timelines.
   - Priority: **6–12 months if HW PMU is mature.**

3. **`gpu_ext` / `fabric_ext` remain long-term programmable-policy signals.**
   - Sources: https://arxiv.org/abs/2512.12615 and https://arxiv.org/abs/2607.26335
   - KMD impact: build stable hooks and correlation now; do not expose programmable scheduling/memory policy until verifier/security/uAPI boundaries are mature.
   - Priority: **Long-term watch.**

### 2026-08-08 · Test #2
1. **ProfInfer strengthens the unified trace + hardware-counter direction.**
   - Source: https://arxiv.org/abs/2601.20755
   - KMD impact: avoid separate debug-trace and performance-profiling object models.
   - Priority: **Trace now; unified timeline in 6–12 months.**

2. **AMD uProf 5.3 shows production profiling consuming GPU hardware events through ROCm/rocprofiler.**
   - Priority: **6–12 months.**

3. **`gpu_ext` / `fabric_ext` remain research signals, not immediate product APIs.**
   - Priority: **Long-term policy watch.**

### 2026-08-08 · Test #1
1. **Linux perf provides a mature model for complex fabric/system PMUs.**
2. **`gpu_ext` explores verified eBPF GPU-driver policy hooks.**
3. **Cross-layer programmable observability is expanding toward GPU/CXL fabrics.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
