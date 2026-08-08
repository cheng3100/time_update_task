# ECC / Bad-page Retirement / PCIe AER / Fault Injection

## High-value learning resources
### 1. AMDGPU RAS
- **链接:** https://docs.kernel.org/gpu/amdgpu/ras.html
- **是什么:** AMDGPU 生产级 CE/UE、bad-page、error injection/RAS 框架文档。
- **价值点:** 展示成熟 GPU 如何把硬件错误计数、隔离、退休和恢复串起来。
- **学习重点:** RAS block、CE/UE、bad page、injection/debugfs。
- **学习注意:** 软件抽象可借鉴，但寄存器和策略高度依赖硬件。

### 2. PCIe AER HOWTO
- **链接:** https://docs.kernel.org/PCI/pcieaer-howto.html
- **是什么:** Linux PCIe Advanced Error Reporting 处理流程官方文档。
- **价值点:** 帮助区分 GPU 内部 RAS 与 PCIe fabric/device link error。
- **学习重点:** error severity、driver callback、recovery sequence。
- **学习注意:** AER recovery 与 GPU internal reset 可能交叉，需避免双方无序重复 reset。
