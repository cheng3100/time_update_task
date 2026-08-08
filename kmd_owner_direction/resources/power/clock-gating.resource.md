# Clock / Power Gating / Idle Residency

## High-value learning resources
### 1. Xe Power Management
- **链接:** https://docs.kernel.org/gpu/xe/xe_pm.html
- **是什么:** GPU 低功耗状态与 runtime power transition 的工程参考。
- **价值点:** 理解 idle residency 如何与 device power state 连接。
- **学习重点:** idle→runtime suspend 边界、wakeup path、state transition。
- **学习注意:** 硬件 gating 细节高度 vendor-specific；公共文档更适合学习软件 state machine。
