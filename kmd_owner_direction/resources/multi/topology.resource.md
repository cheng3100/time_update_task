# PCIe / NUMA / Switch Topology

## High-value learning resources
### 1. Linux PCI documentation
- **链接:** https://docs.kernel.org/PCI/pci.html
- **是什么:** Linux PCI subsystem、BAR、bus/device/function 与拓扑管理的入口文档。
- **价值点:** Multi-GPU topology/P2P capability 建模的 Linux 基础。
- **学习重点:** PCI hierarchy、bridge/switch、NUMA locality，并结合 P2PDMA 文档。
- **学习注意:** BDF 本身不足以判断 P2P；ACS/root complex/IOMMU path 同样关键。
