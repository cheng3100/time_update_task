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
### 2026-08-08

1. **Nova is explicitly separating hardware/firmware abstraction from upper DRM/VFIO consumers.**
   - Source: Linux Nova documentation: https://docs.kernel.org/gpu/nova/index.html
   - Change: `nova-core` is designed as a first-level driver that abstracts GPU hardware/firmware interfaces and can serve second-level drivers such as `nova-drm` and a vGPU manager VFIO driver.
   - KMD impact: for a self-developed GPU, virtualization should reuse a common control/resource abstraction rather than grow a separate PF/VF-only hardware path.
   - Priority: **6–12 months** architecture reference; especially relevant together with Firmware/Control Plane.

2. **SR-IOV kernel mechanics remain commodity; GPU-specific value is resource isolation.**
   - Source: Linux PCI SR-IOV documentation: https://origin.kernel.org/doc/html/latest/PCI/pci-iov-howto.html
   - Change: Linux PCI core already provides standard PF/VF discovery and enable/disable mechanics. The differentiating KMD work is VMID/doorbell/interrupt/memory/engine provisioning, VF reset and PF↔VF ABI.
   - KMD impact: do not treat `pci_enable_sriov()` as the project. Define the project around real GPU resource provisioning and recovery semantics.
   - Priority: **Now, only if ASIC supports SR-IOV**.

3. **No high-value new GPU-specific SR-IOV patchset was found in this update window that changes the direction.**
   - KMD impact: keep SR-IOV as a hardware-gated candidate rather than forcing implementation based on taxonomy alone.
   - Priority: **Capability assessment first**.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
