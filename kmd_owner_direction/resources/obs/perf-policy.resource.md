# perf_event Integration / Dynamic Diagnostics / Programmable Hooks

## High-value learning resources
### 1. perf userspace ring buffer
- **链接:** https://docs.kernel.org/userspace-api/perf_ring_buffer.html
- **是什么:** Linux perf userspace ring-buffer/采样数据模型文档。
- **价值点:** 帮助设计 profiling 数据流与 sampling consumer contract。
- **学习重点:** mmap ring buffer、record lifetime、overflow handling。
- **学习注意:** profiling uAPI 的安全/side-channel 限制必须单独评估。

### 2. gpu_ext
- **链接:** https://arxiv.org/abs/2512.12615
- **是什么:** 探索用 verified eBPF hooks 扩展 GPU OS policy 的研究。
- **价值点:** 说明 stable GPU event/object hooks 可能演化为 programmable diagnostics/policy surface。
- **学习重点:** hook placement、verifier/safety、memory/scheduling policy examples。
- **学习注意:** 当前应投资稳定 hook/telemetry，不应把 programmable policy 直接产品化。
