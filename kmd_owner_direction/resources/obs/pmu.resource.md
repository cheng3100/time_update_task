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

### 3. Intel Xe GT Statistics — low-overhead KMD software telemetry
- **类型:** Canonical / implementation practice
- **链接:** https://docs.kernel.org/next/gpu/xe/xe_gt_stats.html
- **是什么:** Xe driver 以 per-CPU 64-bit counters 记录高频 GPU/KMD 事件的实现，包括 SVM faults/migration/TLB、page reclaim，以及 scheduler long-running queue suspend/wait 等统计。
- **价值点:** 它补足了“硬件 PMU”之外的另一类 observability：很多最重要的瓶颈其实是 KMD software path latency，需要和 HW counter/timeline 一起关联。其 per-CPU counter 设计也展示了如何避免高频原子操作和 cache-coherency 开销。
- **学习重点:** software counters 与 hardware PMU 的职责边界、per-CPU accumulation、reset/read semantics，以及怎样把 fault/migration/scheduler latency 对齐到统一 workload object/timeline。
- **学习注意:** debugfs aggregate counters 缺少 per-process/context attribution，因此更适合作为第一层 low-overhead health/benchmark telemetry；真正 profiling 仍需 tracepoint/object ID/PMU sampling 组合。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
