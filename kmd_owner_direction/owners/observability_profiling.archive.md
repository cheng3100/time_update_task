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
Stable GPU event/object identity + eBPF-based KMD dynamic tracing + low-overhead software/pipeline counters + unified Telemetry Service. Second entry when HW PMU is mature: PMU counter enumeration + per-process/context profiling joined into the same timeline.

### Near-term feature path
Stable tracepoints/object IDs → always-on low-cost software/pipeline counters → unified Telemetry Service → PID/PASID/VM/context/queue/job correlation → KMD/FW timeline → PMU counter integration → bottleneck attribution → dynamic diagnostics → verified programmable hooks.

## Industry Updates
### 2026-09-05 · Weekly #4
1. **Crescent Island PMT v4 shows that real GPU telemetry is a lifetime/arbitration service, not just a counter-read API.**
   - Source: https://lwn.net/Articles/1092225/ (2026-09-01)
   - Change: Crescent Island PMT uses a shared MMIO access window that requires driver-specific callbacks/index selection; crashlog/telemetry access depends on device power, FW-backed discovery uses late binding, and the series handles hotplug, lock ordering and SR-IOV VF behavior.
   - KMD impact: do not let debugfs/hwmon/profiler/RAS independently control shared telemetry windows. Introduce a unified Telemetry Service that owns PM lifetime, FW readiness, privilege/VF filtering, access serialization, counter discovery and snapshot/cache policy. This service can feed the existing software-counter/trace/eBPF/PMU stack.
   - Priority: **Software telemetry service now; hardware PMU as hardware matures.**

### 2026-08-29 · Weekly #3
1. **DAMON/perf hardware-sampling observability RFC reinforces stage-by-stage visibility for asynchronous pipelines.**
   - Source: https://lwn.net/Articles/1089344/
   - Change: the proposed observability layer exposes per-CPU pipeline counters, debugfs statistics and tracepoints that distinguish event creation/enablement, lack of hardware samples, AUX/ring drops, draining and filtering/matching failures instead of exposing only a final sample count.
   - KMD impact: future GPU PMU/fabric tracing should expose health/counters at each pipeline stage—producer, enqueue/ring, overflow/drop, drain, decode and consumer—while keeping the current software counters + stable IDs/eBPF + PMU three-layer model.
   - Priority: **Software pipeline counters now; hardware PMU/AUX integration later.**

2. **Fabric work gives Observability new object types without changing the owner entry point.**
   - References: https://lkml.iu.edu/2608.3/00335.html and https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html
   - KMD impact: reserve stable identities/events for fabric endpoint/port/peer, link-state changes, remote invalidation and connection generation so future fabric diagnostics join the same timestamp/generation model as job/fault/reset events.
   - Priority: **Schema reserve now; implementation with real fabric hardware.**

### 2026-08-15 · Weekly #1
1. **Xe GT Statistics demonstrates a practical always-on KMD software-telemetry layer.**
   - Source: https://docs.kernel.org/next/gpu/xe/xe_gt_stats.html
   - KMD impact: Observability should not jump directly from tracepoints to HW PMU. Add always-on software counters, stable object IDs/tracepoints for attribution and PMU for hardware bottlenecks.
   - Priority: **Software counters + object model now.**

2. **SysOM-AI continues to validate continuous cross-layer observability at production scale.**
   - Source: https://arxiv.org/abs/2603.29235
   - Priority: **Now.**

### 2026-08-08 · Test #4
1. **SysOM-AI demonstrates continuous cross-layer observability at production scale.**
   - Source: https://arxiv.org/abs/2603.29235
   - Priority: **Trace/object model now.**
2. **Radeon GPU Profiler reinforces unified timeline + hardware-counter consumption.**
   - Source: https://gpuopen.com/rgp/
   - Priority: **6–12 months if HW PMU is mature.**
3. **gpu_ext / fabric_ext remain long-term programmable-policy signals.**
   - Priority: **Long-term watch.**

### 2026-08-08 · Test #2
1. **ProfInfer strengthens the unified trace + hardware-counter direction.**
2. **AMD uProf shows production profiling consuming GPU hardware events.**
3. **gpu_ext / fabric_ext remain research signals, not immediate product APIs.**

### 2026-08-08 · Test #1
1. **Linux perf provides a mature model for complex fabric/system PMUs.**
2. **gpu_ext explores verified eBPF GPU-driver policy hooks.**
3. **Cross-layer programmable observability is expanding toward GPU/CXL fabrics.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
