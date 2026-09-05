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

### 3. VFIO PCI error recovery RFC — host recovery state and access guards
- **类型:** Implementation / evolving uAPI design
- **链接:** https://lwn.net/Articles/1091953/
- **是什么:** 2026-09-01 的 19-patch RFC，为 generic `vfio-pci` 补齐 PCI AER recovery participation，并把 host recovery 的状态、reset 结果和 sequence 暴露给 userspace/VMM。
- **价值点:** 它非常具体地展示 assigned device 在恢复期间如何关闭和恢复所有 access path：BAR/config/ioeventfd/interrupt/runtime PM/DMA-BUF/reset 等都必须受统一 recovery state 约束；同时 userspace 只观察 recovery，不参与 host AER recovery 本身。这个模型对 GPU passthrough/vGPU/SR-IOV 的 production recovery 很有长期参考价值。
- **学习重点:** `error_detected()` / `slot_reset()` / `resume()` 生命周期、access guard、BAR fault retry、DMA-BUF revoke、status + sequence uAPI、`recovery_lock` 与 `pci_bus_sem` 锁序、AER fault injection。
- **学习注意:** 当前是 RFC，具体 uAPI bit/locking 实现尚未冻结。长期应学习 recovery/admission/state-sequence 模式，而不是绑定当前字段定义；GPU-specific context/queue/VM 恢复仍需 KMD 自己设计。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
