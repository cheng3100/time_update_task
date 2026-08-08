# DVFS / OPP / Firmware PM Protocol

## High-value learning resources
### 1. Xe Firmware
- **链接:** https://docs.kernel.org/gpu/xe/xe_firmware.html
- **是什么:** Intel Xe GuC/SLPC 等 firmware-managed GPU services 文档。
- **价值点:** 展示 host KMD 与 firmware 在 frequency/power policy 上的责任分层。
- **学习重点:** GuC SLPC/Power Conservation、host interface、state ownership。
- **学习注意:** 不要默认 governor 必须在 KMD；先明确 FW 是否已经是最终 control authority。
