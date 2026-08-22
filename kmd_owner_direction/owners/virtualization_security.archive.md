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
SR-IOV PF/VF bring-up + provisioning/isolation when ASIC capability exists; otherwise VFIO/reset/ownership assessment.

### Near-term decision gate
First confirm ASIC capabilities: SR-IOV extended capability, VF BAR/interrupt model, VMID/resource partitioning, reset semantics, IOMMU isolation and PF↔VF control path. Only then decide whether virtualization is a real feature project or just platform integration.

## Industry Updates
### 2026-08-22 · Weekly #2
1. **A mature SR-IOV driver case makes the PF↔VF admin-channel work concrete.**
   - Source: https://lwn.net/Articles/1088518/ (Cisco enic SR-IOV V2 admin channel/MBOX v13, 2026-08-12)
   - Change: the design uses a direct PF-VF communication channel built on dedicated WQ/RQ/CQ hardware resources plus MSI-X and a mailbox protocol.
   - KMD impact: if the GPU ASIC supports SR-IOV, PF↔VF control should be treated as a versioned service with transport/resource ownership, request/completion, interrupt notification, teardown/reset ordering and capability negotiation—not scattered MMIO side effects. The NIC implementation is not a GPU template, but the control-plane pattern maps well to VMID/doorbell/queue/memory provisioning.
   - Priority: **Architecture reference now; implementation only after ASIC capability gate passes.**

2. **No new GPU-specific SR-IOV mechanism this week changes the hardware-gated decision.**
   - Current GPU reference: https://docs.kernel.org/next/gpu/xe/xe_configfs.html
   - KMD impact: keep PF/VF provisioning/isolation as the feature, not generic PCI SR-IOV enablement.
   - Priority: **ASIC capability first.**

### 2026-08-15 · Weekly #1
1. **No high-value direction-level new item was found after the previous run.**
   - Current reference: https://docs.kernel.org/next/gpu/xe/xe_configfs.html
   - Observation: Xe configfs still provides a concrete GPU SR-IOV lifecycle model where PF mode / `max_vfs` are selected before bind/probe; current `next` also exposes admin-only PF configuration internally.
   - KMD impact: the value remains GPU-specific resource mode, provisioning, PF↔VF ABI, reset and isolation rather than generic `pci_enable_sriov()` mechanics.
   - Priority: **ASIC capability first.**

### 2026-08-08 · Test #4
1. **VFIO CXL Type-2 passthrough v3 extends the problem beyond ordinary PCI passthrough.**
   - Source: https://lwn.net/Articles/1079613/ (2026-06-25)
   - Change: CXL.mem-capable GPUs/accelerators require HDM decoder management, HDM region exposure and component-register virtualization in addition to normal vfio-pci mechanisms.
   - KMD impact: if a future GPU roadmap includes CXL Type-2/coherent memory, virtualization must coordinate memory/fabric ownership rather than treating passthrough as only BAR/IRQ/IOMMU mapping.
   - Priority: **Long-term watch; design early only if ASIC roadmap includes CXL.**

2. **Current Intel graphics families continue to use SR-IOV as the production virtualization direction.**
   - Source: https://www.intel.com/content/www/us/en/support/articles/000093216/graphics/processor-graphics.html (reviewed 2026-05-27)
   - KMD impact: SR-IOV remains a real industry direction, but the self-developed project remains hardware-gated; the value is GPU resource partition/reset/isolation, not generic PCI enablement.
   - Priority: **Capability assessment first.**

### 2026-08-08 · Test #2
1. **No high-value new GPU-specific SR-IOV kernel mechanism was found in this short second-test window.**
   - Baseline source: https://origin.kernel.org/doc/html/latest/PCI/pci-iov-howto.html
   - KMD impact: keep the project hardware-gated; do not manufacture work around generic PCI SR-IOV enable/disable mechanics.
   - Priority: **Capability assessment first.**

2. **Nova continues to validate a shared lower hardware/FW abstraction usable by DRM and VFIO/vGPU upper drivers.**
   - Source: https://docs.kernel.org/gpu/nova/index.html
   - KMD impact: resource ownership, reset and firmware protocol should be common lower-layer capabilities that virtualization consumes rather than duplicates.
   - Priority: **6–12 months architecture reference.**

### 2026-08-08 · Test #1
1. **Nova separates hardware/firmware abstraction from upper DRM/VFIO consumers.**
   - Priority: **6–12 months** architecture reference.
2. **SR-IOV kernel mechanics remain commodity; GPU-specific value is resource isolation.**
   - Priority: **Now, only if ASIC supports SR-IOV.**
3. **No high-value new GPU-specific SR-IOV patchset changed the direction.**
   - Priority: **Capability assessment first.**

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
