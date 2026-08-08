# Multi-GPU / P2P / Fabric

## Stable Summary
Own the multi-device model, topology/connectivity mechanisms and peer/fabric infrastructure. Memory residency/migration policy stays with Memory.

## Living Sub-directions
- multi-GPU enumeration and stable physical/logical identity
- logical index↔BDF/minor mapping
- device visibility, allowed masks and affinity
- container/namespace/cgroup resource-control integration
- PCIe/NUMA/switch topology and distance matrix
- P2P capability discovery/matrix
- peer BAR/VRAM mapping and peer PTE
- P2P DMA and cross-GPU dma-buf
- shared VA/multi-GPU VM
- fabric/link health, reset and RAS

## Current Entry Feature
Multi-GPU enumeration + topology + visibility/affinity + P2P capability matrix.

## Industry Updates
### 2026-08-08
- DRM GPU SVM public design explicitly includes multi-GPU and device-to-device fast interconnect as future work, indicating stronger coupling between shared VM/migration and topology/P2P mechanisms.
- Follow-up: **Now** — establish a robust device/topology/P2P capability model before shared-VM work.

> This section is refreshed on every scheduled update. Stable Summary changes only on an explicit owner-direction decision.
