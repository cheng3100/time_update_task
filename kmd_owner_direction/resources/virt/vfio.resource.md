# VFIO Passthrough / Ownership / IOMMU Isolation

## High-value learning resources

### 1. Linux VFIO documentation
- **类型:** Canonical / official
- **链接:** https://docs.kernel.org/driver-api/vfio.html
- **是什么:** Linux 将设备安全交给 userspace/VM 的标准框架。
- **价值点:** 理解 IOMMU group、device ownership、DMA isolation 与 userspace device model。
- **学习重点:** group/container/device、IOMMU isolation、reset、region/IRQ。
- **学习注意:** VFIO passthrough 不等于 GPU virtualization；GPU state/resource ownership 仍需 KMD 设计。

### 2. Alex Williamson — VFIO tips and tricks: IOMMU Groups, inside and out
- **类型:** Deep explanation / maintainer engineering blog
- **链接:** https://vfio.blogspot.com/2014/08/iommu-groups-inside-and-out.html
- **是什么:** VFIO 主要维护者之一 Alex Williamson 对 IOMMU Group 为什么存在、PCIe 拓扑/ACS 如何影响 isolation boundary 的经典解释。
- **价值点:** 官方 VFIO 文档会告诉你 group 是安全单元，这篇文章更适合真正理解“为什么一个 BDF 不能天然成为独立安全域”，对 GPU passthrough、P2P、ACS、IOMMU isolation 的边界判断非常关键。
- **学习重点:** IOMMU group formation、PCI bridge isolation、ACS、peer-to-peer 路径、device ownership 与 topology 的关系。
- **学习注意:** 文章较早，VFIO API 后续有演进；长期价值主要在 isolation model 和 PCIe topology reasoning，而不是旧 userspace API 细节。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
