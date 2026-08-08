# Multi-GPU / P2P / Fabric

## Summary (stable)
Own the multi-device GPU model, topology/connectivity mechanisms and peer/fabric infrastructure. Memory residency and migration policy remain under the Memory owner; this domain owns device/topology/connectivity mechanisms.

## Candidate sub-directions
- multi-GPU enumeration and stable physical/logical GPU identity
- logical index ↔ BDF/minor mapping
- device visibility, allowed GPU masks and affinity
- process/container/namespace/cgroup interaction
- PCIe/NUMA/switch topology discovery and distance matrix
- P2P capability discovery and capability matrix
- peer BAR/VRAM mapping and peer page-table mappings
- P2P DMA and cross-GPU dma-buf
- shared VA / multi-GPU VM mechanisms
- topology-aware placement hooks
- multi-GPU UVM integration with Memory owner
- fabric/link discovery, health, reset and RAS
- collective-aware groundwork

## Current entry feature
**Multi-GPU enumeration + topology + visibility/affinity + P2P capability matrix.**

## Living focus
After the device/topology model is stable, advance to peer mapping/P2P DMA, then shared VM/fabric. Do not start with complex fabric scheduling.
