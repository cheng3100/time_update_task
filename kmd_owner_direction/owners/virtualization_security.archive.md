# GPU Virtualization / Security

## Stable Summary
Own GPU virtualization, tenant/resource isolation and security mechanisms for safe multi-tenant GPU use.

## Living Sub-directions
- VFIO passthrough, ownership switching, reset/BAR/MSI/IOMMU isolation
- SR-IOV PF/VF lifecycle and resource provisioning
- VMID/queue/doorbell/interrupt/memory partition
- PF↔VF ABI, VF FLR/reset, per-VF accounting/isolation
- vGPU/resource partition, tenant quota, virtual interrupts
- live-migration groundwork
- secure boot/measurement, memory scrub, secure reset
- attestation/confidential GPU

## Current Entry Feature
SR-IOV PF/VF bring-up + provisioning/isolation + versioned admin control when ASIC capability exists; otherwise VFIO/reset/ownership assessment.

### Near-term decision gate
First confirm ASIC capabilities: SR-IOV extended capability, VF BAR/interrupt model, VMID/resource partitioning, reset semantics, IOMMU isolation and PF↔VF control path. Only then decide whether virtualization is a real feature project or just platform integration.

## Industry Updates
### 2026-08-29 · Weekly #3
1. **No new GPU-specific SR-IOV/vGPU mechanism changes the hardware-gated plan this week.**
   - Current GPU reference: https://docs.kernel.org/next/gpu/xe/xe_configfs.html
   - KMD impact: keep ASIC capability first and keep PF/VF provisioning/isolation/admin control as the real feature rather than generic PCI SR-IOV enablement.
   - Priority: **ASIC capability first.**

2. **UALink peer-memory authorization is a future fabric/security boundary signal, not a reason to expand virtualization now.**
   - Source: https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html
   - KMD impact: future multi-tenant fabrics will need peer-memory authorization and connection/reset isolation, but these should be layered on real fabric hardware and tenant requirements rather than pre-productized today.
   - Priority: **Long-term boundary watch.**

### 2026-08-22 · Weekly #2
1. **A mature SR-IOV driver case makes the PF↔VF admin-channel work concrete.**
   - Source: https://lwn.net/Articles/1088518/ (Cisco enic SR-IOV V2 admin channel/MBOX v13, 2026-08-12)
   - Change: the design uses a direct PF-VF communication channel built on dedicated WQ/RQ/CQ hardware resources plus MSI-X and a mailbox protocol.
   - KMD impact: if the GPU ASIC supports SR-IOV, PF↔VF control should be treated as a versioned service with transport/resource ownership, request/completion, interrupt notification, teardown/reset ordering and capability negotiation—not scattered MMIO side effects.
   - Priority: **Architecture reference now; implementation only after ASIC capability gate passes.**

2. **No new GPU-specific SR-IOV mechanism this week changes the hardware-gated decision.**
   - Current GPU reference: https://docs.kernel.org/next/gpu/xe/xe_configfs.html
   - Priority: **ASIC capability first.**

### 2026-08-15 · Weekly #1
1. **No high-value direction-level new item was found after the previous run.**
   - Current reference: https://docs.kernel.org/next/gpu/xe/xe_configfs.html
   - KMD impact: the value remains GPU-specific resource mode, provisioning, PF↔VF ABI, reset and isolation rather than generic `pci_enable_sriov()` mechanics.
   - Priority: **ASIC capability first.**

### 2026-08-08 · Test #4
1. **VFIO CXL Type-2 passthrough v3 extends the problem beyond ordinary PCI passthrough.**
   - Source: https://lwn.net/Articles/1079613/
   - Priority: **Long-term watch.**
2. **Current Intel graphics families continue to use SR-IOV as the production virtualization direction.**
   - Source: https://www.intel.com/content/www/us/en/support/articles/000093216/graphics/processor-graphics.html
   - Priority: **Capability assessment first.**

### 2026-08-08 · Test #2
1. **SR-IOV kernel mechanics remain commodity; GPU-specific value is resource isolation.**
2. **Nova validates common lower HW/FW services for DRM/VFIO consumers.**

### 2026-08-08 · Test #1
1. **Nova separates hardware/firmware abstraction from upper DRM/VFIO consumers.**
2. **SR-IOV kernel mechanics remain commodity; GPU-specific value is resource isolation.**
3. **No high-value new GPU-specific SR-IOV patchset changed the direction.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
