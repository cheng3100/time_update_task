# IOMMU / ATS / PRI / PASID / SVA

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. Linux Shared Virtual Addressing
- **链接:** https://docs.kernel.org/arch/x86/sva.html
- **是什么:** Linux/x86 对 SVA、PASID、ATS、PRI 等机制的官方说明。
- **价值点:** 把 PCIe device address translation 与进程虚拟地址空间连接起来。
- **学习重点:** PASID 与 mm 的绑定、ATS cache、PRI page request、IOMMU fault path。
- **学习注意:** 不同 IOMMU/SMMU 平台能力差异很大，不要把 Intel x86 行为泛化到所有架构。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
