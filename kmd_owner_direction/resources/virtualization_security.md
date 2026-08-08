# Virtualization / Security — Learning Resources

## VFIO passthrough / ownership / reset / IOMMU isolation
- [VFIO — Virtual Function I/O](https://docs.kernel.org/driver-api/vfio.html) — Canonical Linux model for secure userspace/device assignment and IOMMU-protected ownership.

## SR-IOV PF/VF lifecycle
- [PCI Express I/O Virtualization HOWTO](https://docs.kernel.org/PCI/pci-iov-howto.html) — Stable kernel reference for PF/VF enablement and PCI-core mechanics; useful as the baseline before GPU-specific provisioning.

## GPU resource provisioning: VMID / queue / doorbell / interrupt / memory partition
- [Nova core architecture](https://docs.kernel.org/gpu/nova/index.html) — Valuable architectural reference for placing hardware/FW resource control below DRM/VFIO clients instead of duplicating paths.

## PF↔VF ABI / VF FLR / accounting / isolation
- [Nova core guidelines](https://docs.kernel.org/next/gpu/nova/core/guidelines.html) — Strong reference for firmware-version-independent lower-layer APIs serving multiple upper drivers.

## vGPU / resource partition / live migration groundwork
- [Nova vGPU direction / nova-core docs](https://docs.kernel.org/gpu/nova/index.html) — Tracks a modern open-source GPU architecture where a lower core can serve a VFIO/vGPU manager.

## Secure boot / measurement / secure reset / attestation
- [Nova firmware security documentation index](https://docs.kernel.org/gpu/nova/index.html) — Use the FWSEC/FSP/Secure Boot sections to understand how GPU firmware trust roots feed into driver architecture.
