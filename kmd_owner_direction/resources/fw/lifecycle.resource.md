# Boot / Restart / Upgrade / Rollback Lifecycle

## High-value learning resources
### 1. Nova VBIOS
- **链接:** https://docs.kernel.org/gpu/nova/core/vbios.html
- **是什么:** Nova 对 GPU boot/VBIOS 相关流程的官方文档。
- **价值点:** 用于理解 GPU firmware boot prerequisite 与 early lifecycle。
- **学习重点:** boot dependency、firmware/board data 获取、failure path。
- **学习注意:** VBIOS 不是通用 GPU FW lifecycle 全貌，需要结合自研 SoC boot chain。
