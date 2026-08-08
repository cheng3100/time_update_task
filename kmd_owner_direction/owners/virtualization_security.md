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
