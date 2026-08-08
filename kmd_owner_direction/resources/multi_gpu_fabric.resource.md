# Multi-GPU / P2P / Fabric — Learning Resources

## Multi-GPU enumeration / stable identity / logical mapping
- [DRM device and driver model](https://docs.kernel.org/gpu/drm-internals.html) — Durable reference for device objects, minors and the DRM-side identity/lifetime model that multi-GPU enumeration builds on.

## Device visibility / affinity / namespace / resource control
- [DRM subsystem documentation](https://docs.kernel.org/gpu/index.html) — Use the DRM device-node and client model as the baseline before adding vendor-specific visibility or affinity controls.

## PCIe / NUMA / switch topology / distance
- [Linux PCI documentation](https://docs.kernel.org/PCI/pci.html) — Canonical kernel view of PCI devices/resources; pair with NUMA topology interfaces for placement policy.

## P2P capability / peer BAR / peer mapping
- [PCI Peer-to-Peer DMA Support](https://docs.kernel.org/driver-api/pci/p2pdma.html) — Best Linux reference for peer-memory topology constraints, provider/client/orchestrator roles and safe P2P DMA setup.

## Cross-GPU dma-buf / synchronization
- [DMA-BUF sharing and synchronization](https://docs.kernel.org/driver-api/dma-buf.html) — Essential for exporter/importer ownership, attachments, fences and reservation objects across devices.

## Shared VA / multi-GPU VM / multi-GPU UVM
- [GPU SVM / drm_pagemap RFC](https://docs.kernel.org/gpu/rfc/gpusvm.html) — Current common-layer design explicitly anticipates multi-GPU and peer/device-memory evolution.

## Fabric / link health / movement policy
- [fabric_ext paper](https://arxiv.org/abs/2607.26335) — Research-stage, but unusually useful for thinking about future movement, ordering, ownership and observability semantics across GPU/DPU/CXL fabrics. Read as architecture inspiration, not an implementation blueprint.
