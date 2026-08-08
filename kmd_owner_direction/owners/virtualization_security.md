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

## Industry Updates
### 2026-08-08
- Nova-style Linux architectures are moving toward hardware/firmware abstraction layers that can serve both DRM and VFIO/vGPU managers, increasing the control-plane/virtualization intersection.
- Follow-up: **6–12 months** — first verify ASIC SR-IOV/resource-partition capability before committing to a full virtualization roadmap.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
