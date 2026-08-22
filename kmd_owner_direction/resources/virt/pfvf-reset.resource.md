# PF↔VF ABI / VF FLR / Reset / Accounting

## High-value learning resources
### 1. Nova architecture
- **类型:** Canonical / architecture reference
- **链接:** https://docs.kernel.org/gpu/nova/index.html
- **是什么:** Nova 将 lower HW/FW abstraction 与 upper DRM/VFIO client 解耦的架构文档。
- **价值点:** 有助于思考 PF/VF 是否应复用统一 resource/control-plane service。
- **学习重点:** nova-core 与 second-level driver 的分层。
- **学习注意:** Nova 不是 SR-IOV 实现文档；这里主要借鉴分层思想。

### 2. Cisco enic SR-IOV V2 admin channel / MBOX protocol
- **类型:** Implementation / practice / upstream case study
- **链接:** https://lwn.net/Articles/1088518/
- **是什么:** 2026-08 的 net-next v13 patch series，为 SR-IOV V2 建立直接 PF↔VF admin channel；使用 dedicated WQ/RQ/CQ hardware resources 和 MSI-X，并定义 mailbox protocol。
- **价值点:** 虽然不是 GPU driver，但它非常具体地展示了真正的 SR-IOV owner 工作为何远超过 `pci_enable_sriov()`：PF/VF 需要独立 transport、消息协议、资源生命周期、interrupt/completion 和 teardown/reset ordering。
- **学习重点:** admin channel resource ownership、request/completion、PF/VF protocol versioning、MSI-X notification、remove/reset ordering，以及 mailbox 与业务 data path 的边界。
- **学习注意:** NIC queue model 不能直接映射 GPU VMID/doorbell/engine partition；应抽取 control-plane pattern，再映射到 GPU PF/VF ABI。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
