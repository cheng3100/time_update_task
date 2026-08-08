# Post-reset Restore / Replay

## High-value learning resources
### 1. Xe Device Coredump
- **链接:** https://docs.kernel.org/gpu/xe/xe_devcoredump.html
- **是什么:** Xe reset serialization 与 hang-state 捕获的官方说明。
- **价值点:** 有助于把 capture、reset、restore 三个阶段明确分开。
- **学习重点:** reset 后哪些 driver state 仍可信、哪些必须重建。
- **学习注意:** job replay 需要幂等性与用户可见语义设计，不能默认所有 workload 都可安全 replay。
