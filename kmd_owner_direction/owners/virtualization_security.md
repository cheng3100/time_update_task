# GPU Virtualization / Security

## Summary (stable)
Own GPU virtualization, tenant/resource isolation and the security mechanisms that make multi-tenant GPU use safe. Security may split into a separate owner only after the domain grows.

## Candidate sub-directions
- VFIO passthrough, device ownership switching, reset semantics, BAR/MSI/IOMMU isolation
- SR-IOV PF/VF bring-up and lifecycle
- VF resource provisioning: VMID, queue, doorbell, interrupt, memory aperture
- PF↔VF mailbox/ABI, VF FLR/reset, per-VF accounting and isolation
- vGPU/resource partition, tenant quota, virtual interrupts
- live-migration groundwork and state save/restore
- firmware secure boot/measurement
- memory scrub, secure reset, command/uAPI hardening
- attestation and confidential GPU

## Current entry feature
If the ASIC exposes SR-IOV: **PF/VF bring-up + VF resource provisioning/isolation**. Otherwise: **VFIO passthrough/reset/ownership assessment** as a preparatory feature, not automatically a full long-term owner workload.

## Living focus
Re-evaluate whenever hardware virtualization capabilities, confidential-computing requirements, or upstream VFIO/SR-IOV GPU mechanisms change.
