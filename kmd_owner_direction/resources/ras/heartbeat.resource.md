# Heartbeat / Watchdog / Hang Detection

## High-value learning resources
### 1. Xe Device Coredump
- **链接:** https://docs.kernel.org/gpu/xe/xe_devcoredump.html
- **是什么:** Intel Xe GPU hang 时的诊断与恢复入口文档。
- **价值点:** 能反推 hang detection 后必须马上保存哪些状态以及 reset serialization。
- **学习重点:** first-error、capture timing、reset flow、hang state lifetime。
- **学习注意:** watchdog 应与 progress semantics 对齐，不能只依赖固定 wall-clock timeout。
