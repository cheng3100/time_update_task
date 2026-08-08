# Observability / Profiling / Programmable Driver — Learning Resources

## Stable KMD tracepoint / event schema
- [Linux tracepoints documentation](https://docs.kernel.org/trace/tracepoints.html) — Core reference for stable tracepoint design and low-overhead event instrumentation.

## BTF / CO-RE / eBPF dynamic tracing
- [BPF documentation](https://docs.kernel.org/bpf/index.html) — Canonical kernel reference for BPF architecture, verifier, BTF and program types.
- [BPF CO-RE reference guide](https://nakryiko.com/posts/bpf-core-reference-guide/) — High-quality long-lived practical guide for portable tracing across kernel builds.

## PID / PASID / VM / context / queue / job correlation
- [DRM internals](https://docs.kernel.org/gpu/drm-internals.html) — Useful for mapping Linux process/file/device objects to driver-side client/context objects before defining a correlation schema.

## UMD → KMD → FW → GPU unified timeline
- [ProfInfer](https://arxiv.org/abs/2601.20755) — Practical research example combining dynamic eBPF runtime traces with hardware-counter trends and timeline visualization.

## GPU PMU / counter discovery / perf integration
- [perf_event subsystem](https://docs.kernel.org/userspace-api/perf_ring_buffer.html) — Foundation for sampling/streaming semantics and perf userspace data transport.
- [NVIDIA Tegra241 PMU](https://docs.kernel.org/admin-guide/perf/nvidia-tegra241-pmu.html) — Concrete example of complex GPU-adjacent fabric counters represented through standard Linux perf PMUs.

## Dynamic diagnostics / fault injection
- [Linux fault injection](https://docs.kernel.org/fault-injection/index.html) — Strong baseline for designing controlled driver fault-injection hooks rather than ad-hoc debug knobs.

## Verified programmable policy hooks
- [gpu_ext](https://arxiv.org/abs/2512.12615) — Research-stage but important long-term reference for treating the GPU driver/device layer as a verified eBPF policy interface. Read for hook/object-safety design, not near-term product requirements.
