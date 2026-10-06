---
layout: default
title: "GPU KMD Current Feature HLDs"
parent: GPU KMD Owner Direction
permalink: /kmd_owner_direction/features/
---
# Current Feature HLDs

这一层不是 Stable Owner taxonomy，也不是 weekly news。它记录每个 Owner 当前最值得直接立项的 feature 的长期设计说明，首先解释“它是什么、为什么存在、解决什么问题和难点”，再逐步沉淀实现方案。

| Owner | Current Feature |
|---|---|
| Memory | [Recoverable Fault + HMM/SVM + Migration + Replay](/time_update_task/kmd_owner_direction/features/memory-recoverable-fault.html) |
| Virtualization | [SR-IOV PF/VF Provisioning & Isolation](/time_update_task/kmd_owner_direction/features/virt-pfvf.html) |
| Power | [Utilization → Runtime PM / DVFS](/time_update_task/kmd_owner_direction/features/power-runtime-pm.html) |
| RAS | [Recovery Admission + Snapshot + Reconciliation](/time_update_task/kmd_owner_direction/features/ras-recovery.html) |
| Multi-GPU | [Topology & P2P Capability Matrix](/time_update_task/kmd_owner_direction/features/multi-p2p-matrix.html) |
| Observability | [Stable Identity + eBPF Trace](/time_update_task/kmd_owner_direction/features/obs-identity-ebpf.html) |
| Firmware | [Versioned Async Firmware Control Plane](/time_update_task/kmd_owner_direction/features/fw-versioned-protocol.html) |
