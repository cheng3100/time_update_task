---
layout: default
title: "Feature HLD · SR-IOV PF/VF Provisioning & Isolation"
parent: GPU KMD Owner Direction
permalink: /kmd_owner_direction/features/virt-pfvf.html
---
# SR-IOV PF/VF Provisioning & Isolation

## 1. 一句话定义
PF KMD 把物理 GPU 的 VMID/queue/doorbell/interrupt/memory/engine 等 GPU-specific 资源安全分配给多个 VF，并保证 VF 的 DMA、MMIO、FW command 与 reset 只能作用于授权范围。

## 2. 背景与位置
PCIe SR-IOV 只解决“一个 PF 暴露多个 PCI function”，不会自动解决 GPU 内部资源切分。真正的 virtualization control plane 位于 PCI SR-IOV/VFIO/IOMMU 与 GPU resource manager/FW admin service 之间。

## 3. 解决的问题
没有显式 provisioning/isolation，VF 即使枚举成功，也可能共享不可隔离的 VMID、doorbell、IRQ、VRAM 或 reset domain；这不是可交付 virtualization。

## 4. 典型场景
多 VM 共享 GPU；一个 VF FLR 不能影响其它 tenant；host AER recovery 期间 VF/VMM 必须知道设备不可访问；live migration/restore 的 resource ID 不能被当作可信内部状态。

## 5. 核心对象
PF、VF、tenant、resource capability、assignment、VMID/PASID、doorbell aperture、IRQ vector、memory partition、engine mask、PF↔VF admin channel、VF generation、FLR/AER state。

## 6. 控制流
PF capability discovery → resource pool → VF create/assign → VF probe/handshake → workload → FLR/AER → block access/drain → reclaim/reinitialize → generation advance → VF reopen。

## 7. 边界
PCI core 创建 VF；IOMMU/VFIO 提供 DMA/isolation framework；PF KMD 拥有 GPU-specific resource partition 与 recovery；VF KMD 只消费授予能力；FW 可实现 admin channel，但 resource policy 仍归 PF KMD。

## 8. 生命周期
DISABLED → PROVISIONED → ACTIVE → QUIESCING → RESETTING → REINITIALIZING → ACTIVE；失败进入 FAILED/REVOKED。Host AER 与 guest recovery 必须是两个可观察但不同 ownership 的状态机。

## 9. 关键难点
资源并非天然可分区；PF global reset/VF FLR scope；doorbell/IRQ/memory aperture isolation；PF↔VF ABI version；stale completion；restore blob bounds/type/capability/generation validation；SR-IOV enable/disable 与 userspace access 并发。

## 10. Failure / Debug
记录 tenant/VF ID、resource assignment、admin seq/generation、FLR/AER reason、blocked access reason、IOMMU fault、recovery sequence。错误恢复期间访问必须有确定 errno/status，而非随机 timeout。

## 11. 最小闭环
先做 capability assessment。ASIC/FW 真支持时：PF enable → VF resource allocate → VF probe → basic workload → VF FLR → resource reclaim/reassign，并证明一个 VF 不能访问另一个 VF 的 DMA/MMIO/doorbell/resource。

## 12. 3–6 月
capability matrix；resource object/ownership；PF↔VF minimal admin ABI；IOMMU/doorbell/IRQ isolation；VF FLR；AER recovery window。

## 13. 1–2 年
live migration、vGPU/resource partition、per-tenant QoS/accounting、secure boot/measurement/attestation、confidential GPU。

## 14. Cross-Owner
Memory 提供 per-tenant GPUVM/PASID；RAS 提供 recovery primitive；FW 提供 versioned admin service；Power 提供 partition-aware PM；Observability 提供 tenant attribution；Multi-GPU 提供 virtual topology/peer policy。

## 15. Upstream 索引
VFIO PCI error recovery RFC v2（16 patches）是重要参考：host recovery 期间 block access + SRCU drain，并通过 UAPI status/sequence 通知 userspace。

## 16. Hardware Gates
是否真有 SR-IOV capability？VMID/queue/doorbell/IRQ/VRAM 是否硬件可隔离？VF 是否有独立 FLR/reset domain？IOMMU/PASID/ATS 支持？FW 是否有 PF admin privilege 与 VF mailbox？