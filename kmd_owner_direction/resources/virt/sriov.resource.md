# SR-IOV PF/VF Lifecycle

## High-value learning resources
### 1. PCI SR-IOV HOWTO
- **链接:** https://docs.kernel.org/PCI/pci-iov-howto.html
- **是什么:** Linux PCI core 对 SR-IOV PF/VF 创建与管理的基础文档。
- **价值点:** 明确 PCI core 已解决的部分，使 KMD 项目聚焦 GPU-specific provisioning。
- **学习重点:** `sriov_configure`、numvfs、VF enumeration、driver binding。
- **学习注意:** 不要把 `pci_enable_sriov()` 当成 GPU 虚拟化项目主体。
