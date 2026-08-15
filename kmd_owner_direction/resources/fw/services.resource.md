# FW-centric Init / PM / Reset / HW Scheduler Services

## High-value learning resources
### 1. Xe Firmware
- **链接:** https://docs.kernel.org/gpu/xe/xe_firmware.html
- **是什么:** Intel Xe 将 GuC 用作 scheduling/power 等 firmware-managed service 的官方说明。
- **价值点:** 展示现代 KMD 如何逐步把硬件管理能力移到 firmware control plane。
- **学习重点:** GuC service boundaries、host programming interface、power conservation。
- **学习注意:** 先把基础 async/version/error contract 做稳定，再扩展多个 service class。

### 2. Nova Device Initialization (devinit)
- **类型:** Canonical / firmware-lifecycle architecture
- **链接:** https://docs.kernel.org/next/gpu/nova/core/devinit.html
- **是什么:** Nova 对 Ampere-era GPU reset 后低层 firmware initialization 的概念说明：FWSEC/GSP/PMU 等微控制器按序运行，devinit 负责 VRAM controller timing、power sequencing、clock/PLL、thermal 等关键初始化，并通过 GFW_BOOT 向 host 表示核心初始化完成。
- **价值点:** 很适合建立“GPU reset 并不等于 KMD 重新写一批寄存器”的现代 control-plane 直觉；firmware boot、secure privilege、device init、runtime suspend/resume 是一条连续生命周期。
- **学习重点:** reset→FWSEC→devinit→GFW_BOOT 的阶段边界、secure/low-secure 权限切换、哪些硬件在 host driver 介入前已经初始化，以及 devinit 为什么在 suspend/resume 时也需要重新执行。
- **学习注意:** 文档以 Ampere 为例且实现会演进；不要照搬具体微控制器职责。应抽象的是 phase/generation/capability/timeout/error/recovery contract。
