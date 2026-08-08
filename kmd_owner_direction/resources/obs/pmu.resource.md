# GPU PMU / Counter Discovery / Sampling / Multiplexing

## High-value learning resources

### 1. NVIDIA Tegra241 PMU
- **类型:** Canonical / perf PMU reference
- **链接:** https://docs.kernel.org/admin-guide/perf/nvidia-tegra241-pmu.html
- **是什么:** Linux perf 中复杂 system/fabric PMU 的官方实现文档。
- **价值点:** 借鉴 event discovery、counter encoding、multiplexing 与 per-scope 统计接口。
- **学习重点:** PMU registration、event attributes、bandwidth/latency metrics。
- **学习注意:** system PMU 与 GPU execution PMU scope 不完全相同，还需补充 context attribution。

### 2. AMD GPUOpen — Radeon GPU Profiler
- **类型:** Implementation / production profiling practice
- **链接:** https://gpuopen.com/rgp/
- **是什么:** AMD 的低层 GPU profiling 工具，围绕 queue/event timeline、shader execution、cache/memory 与硬件性能数据提供分析视图。
- **价值点:** 很适合从“硬件有 counter”进一步思考 KMD/driver 要怎样组织 event naming、counter capture、timeline correlation 和 userspace consumption；也能帮助定义 PMU feature 的最终用户价值，而不只是寄存器读取接口。
- **学习重点:** queue/event timeline、hardware counter、instruction timing/thread divergence、cache/memory bottleneck，以及 profiler 如何把 workload identity 和 counter 关联起来。
- **学习注意:** RGP 是完整 AMD 工具链，不等于 Linux `perf_event` API。自研 KMD 应拆出可复用 PMU/counter mechanism，再决定由 perf、私有 profiler 或两者共同消费。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
