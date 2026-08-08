# GPU PMU / Counter Discovery / Sampling / Multiplexing

## High-value learning resources
### 1. NVIDIA Tegra241 PMU
- **链接:** https://docs.kernel.org/admin-guide/perf/nvidia-tegra241-pmu.html
- **是什么:** Linux perf 中复杂 system/fabric PMU 的官方实现文档。
- **价值点:** 借鉴 event discovery、counter encoding、multiplexing 与 per-scope 统计接口。
- **学习重点:** PMU registration、event attributes、bandwidth/latency metrics。
- **学习注意:** system PMU 与 GPU execution PMU scope 不完全相同，还需补充 context attribution。
