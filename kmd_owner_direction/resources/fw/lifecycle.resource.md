# Boot / Restart / Upgrade / Rollback Lifecycle

## High-value learning resources
### 1. Nova VBIOS
- **链接:** https://docs.kernel.org/gpu/nova/core/vbios.html
- **是什么:** Nova 对 GPU boot/VBIOS 相关流程的官方文档。
- **价值点:** 用于理解 GPU firmware boot prerequisite 与 early lifecycle。
- **学习重点:** boot dependency、firmware/board data 获取、failure path。
- **学习注意:** VBIOS 不是通用 GPU FW lifecycle 全貌，需要结合自研 SoC boot chain。

### 2. Nova r000 GSP firmware ABI v2 patch series
- **类型:** Implementation / evolving upstream architecture
- **链接:** https://lkml.iu.edu/2608.2/11372.html
- **是什么:** 2026-08-21 Nova v2 patch series，把 nova-core 从具体 570.144 GSP release 切换到目标为跨 release 稳定的 r000 GSP firmware ABI；同时调整 MCTP/NVDM transport、msgq v2、GSP_INIT、load-and-execute boot event、ucodes/state-monitor buffers 与 validation。
- **价值点:** 这是非常完整的 firmware major-ABI transition 案例，说明“稳定 ABI”并不意味着 wire format 永不变化，而是需要清晰 major-generation 边界、成组 protocol transition、strict validation 和 stable upper service abstraction。
- **学习重点:** transport header/version/vendor/length validation、queue pointer/doorbell semantics、GSP_INIT handshake、bootloader/load-exec、firmware carveout/resource changes、release-specific ABI → stable ABI 的迁移方式。
- **学习注意:** 对应 r000 firmware 当时尚未公开，patch 明确要求 firmware 发布前不合入；学习 lifecycle/compatibility/translation 设计，不依赖当前 Rust API 或具体结构布局。
