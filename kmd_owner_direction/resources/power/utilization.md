# Busy/Idle / Per-engine Utilization

## High-value learning resources
### 1. Xe GT Frequency
- **链接:** https://docs.kernel.org/gpu/xe/xe_gt_freq.html
- **是什么:** Intel Xe 的 GT frequency/utilization 相关控制与 telemetry 文档。
- **价值点:** 帮助区分 measurement、policy 与 frequency actuation。
- **学习重点:** min/max/current frequency、GT scope、workload 与 telemetry 的关系。
- **学习注意:** 瞬时 busy 比例不应直接等价为可用于 governor 的稳定负载指标。
