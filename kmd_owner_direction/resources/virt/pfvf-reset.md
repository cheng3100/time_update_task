# PF↔VF ABI / VF FLR / Reset / Accounting

## High-value learning resources
### 1. Nova architecture
- **链接:** https://docs.kernel.org/gpu/nova/index.html
- **是什么:** Nova 将 lower HW/FW abstraction 与 upper DRM/VFIO client 解耦的架构文档。
- **价值点:** 有助于思考 PF/VF 是否应复用统一 resource/control-plane service。
- **学习重点:** nova-core 与 second-level driver 的分层。
- **学习注意:** Nova 不是 SR-IOV 实现文档；这里主要借鉴分层思想。
