# GPU Observability / Profiling / Programmable Driver Infrastructure

## Summary (stable)
Own software-event tracing, hardware performance monitoring, cross-layer correlation and programmable diagnostics. eBPF is an entry technology, not the owner identity.

## Candidate sub-directions
- stable KMD tracepoint/event model
- BTF/CO-RE, eBPF kprobe/fentry/fexit/tracepoint tracing
- PID/PASID/VM/context/queue/job correlation
- GPUVM/fault/migration tracing
- firmware/KMD/UMD unified timeline
- per-process/per-context metrics and latency attribution
- dynamic diagnostics, triggers and fault-injection/debug hooks
- GPU PMU/performance-counter discovery and enumeration
- counter groups, allocation/multiplexing, sampling and overflow
- SM/CU/cache/memory/fabric/engine counters
- per-context/per-process counter attribution and context-switch save/restore
- profiling uAPI, streaming/sample buffers and Linux perf/perf_event integration
- tenant-safe counter virtualization and side-channel restrictions
- long-term verified programmable policy hooks (gpu_ext-like memory/resource/scheduling policy)

## Current entry feature
**eBPF-based GPU KMD dynamic tracing framework** using stable tracepoints + BTF/CO-RE. If hardware PMU support is mature, a second feature can be **GPU PMU counter enumeration + basic per-process/context profiling**.

## Living focus
Converge software traces, firmware events and hardware PMU samples into one timeline/performance-attribution model.
