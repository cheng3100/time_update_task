# vGPU / Live Migration Groundwork

## High-value learning resources
### 1. Linux VFIO documentation
- **链接:** https://docs.kernel.org/driver-api/vfio.html
- **是什么:** VFIO device state、region/IRQ 与 userspace ownership 的标准基础。
- **价值点:** 做 vGPU/live migration 前必须先掌握 device state 暴露与 isolation。
- **学习重点:** reset/state ownership、可序列化状态边界。
- **学习注意:** 真正 live migration 还需要 dirty tracking、state serialization 与 compatibility contract。
