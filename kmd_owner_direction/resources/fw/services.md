# FW-centric Init / PM / Reset / HW Scheduler Services

## High-value learning resources
### 1. Xe Firmware
- **链接:** https://docs.kernel.org/gpu/xe/xe_firmware.html
- **是什么:** Intel Xe 将 GuC 用作 scheduling/power 等 firmware-managed service 的官方说明。
- **价值点:** 展示现代 KMD 如何逐步把硬件管理能力移到 firmware control plane。
- **学习重点:** GuC service boundaries、host programming interface、power conservation。
- **学习注意:** 先把基础 async/version/error contract 做稳定，再扩展多个 service class。
