# Frequency Residency / Memory-bandwidth Telemetry

## High-value learning resources
### 1. NVIDIA Tegra241 PMU
- **链接:** https://docs.kernel.org/admin-guide/perf/nvidia-tegra241-pmu.html
- **是什么:** Linux perf 中复杂 fabric/system PMU 的官方实例。
- **价值点:** 帮助设计 GPU/fabric counter 如何接入标准 perf_event 模型。
- **学习重点:** event encoding、counter scope、bandwidth/latency metrics、multiplexing。
- **学习注意:** system PMU 与 GPU execution PMU scope 不完全相同，需要补充 context attribution 设计。
