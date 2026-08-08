# VFIO Passthrough / Ownership / IOMMU Isolation

## High-value learning resources
### 1. Linux VFIO documentation
- **链接:** https://docs.kernel.org/driver-api/vfio.html
- **是什么:** Linux 将设备安全交给 userspace/VM 的标准框架。
- **价值点:** 理解 IOMMU group、device ownership、DMA isolation 与 userspace device model。
- **学习重点:** group/container/device、IOMMU isolation、reset、region/IRQ。
- **学习注意:** VFIO passthrough 不等于 GPU virtualization；GPU state/resource ownership 仍需 KMD 设计。
