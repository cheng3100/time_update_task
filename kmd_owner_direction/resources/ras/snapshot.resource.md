# Hang Snapshot / devcoredump / Reset Reason

## High-value learning resources
### 1. Xe Device Coredump
- **链接:** https://docs.kernel.org/gpu/xe/xe_devcoredump.html
- **是什么:** Linux devcoredump 上实现 GPU hang snapshot 的生产案例。
- **价值点:** 最直接说明为什么必须 snapshot-at-hang、read-later。
- **学习重点:** snapshot content、lifetime、first failure、userspace retrieval。
- **学习注意:** 不要在 reset 之后重新读取 live register 拼 crash dump。
