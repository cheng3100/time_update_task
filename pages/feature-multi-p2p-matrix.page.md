---
layout: default
title: "Feature HLD · Multi-GPU Topology & P2P Capability Matrix"
parent: GPU KMD Owner Direction
permalink: /kmd_owner_direction/features/multi-p2p-matrix.html
---
# Multi-GPU Topology & Directional/TLP-aware P2P Capability Matrix

## 1. 一句话定义
为每对 GPU 建立稳定 identity/topology，并按方向、TLP class、Address Type、ATS/ACS/IOMMU 条件判断 peer transaction 是 DIRECT、REDIRECT 还是 BLOCKED，并返回原因。

## 2. 背景与位置
它位于 PCIe topology/IOMMU 与 GPU peer mapping/dma-buf/multi-GPU UVM 之间，是“能不能直接互访”的事实层，而不是数据迁移 policy。

## 3. 解决的问题
“同一个 switch 就能 P2P”是错误抽象。Request 与 Completion 路径、ACS controls、translated/untranslated request、ATS 和 nested/asymmetric switch 都可能使 A→B 与 B→A、read 与 write 得到不同答案。

## 4. 典型场景
GPU A DMA 到 GPU B BAR/VRAM；双 GPU dma-buf；一侧 ATS enabled；ACS redirect；hot reset 后旧 peer mapping 必须 revoke。

## 5. 核心对象
stable GPU ID、PCI path/divergence port、NUMA node、source/destination、direction、TLP class、Address Type、ACS bits、ATS mode、IOMMU mode、topology/fabric generation。

## 6. 控制流
enumerate → stable identity → topology walk → find divergence → evaluate Request/Completion class → apply ATS/Address Type/ACS → return capability+reason → optional real peer DMA validation。

## 7. 边界
PCI/IOMMU 提供 routing/translation facts；Multi-GPU Owner 形成 capability matrix 与 lifecycle；Memory Owner 决定 peer residency/mapping；UMD/NCCL 类库据此选择 transport/policy。

## 8. 生命周期
DISCOVERED → TOPOLOGY_VALID → CAPABILITY_VALID → PEER_ACTIVE；hotplug/reset/link error 使 generation 改变并进入 INVALID/REVALIDATING。

## 9. 难点
direction asymmetry、nested switch、per-device vs per-mapping ATS、ACS unreadable state、IOMMU remapping、BAR aperture、peer mapping lifetime、fabric reset。

## 10. Failure / Debug
query 必须返回阻断 port/control/reason，而非 bool。记录 source/destination、direction、TLP/address type、ATS/IOMMU mode、ACS decision、generation 和真实 DMA validation result。

## 11. 最小闭环
enumeration + topology + A→B/B→A capability/reason matrix + debug query + peer BAR/DMA smoke test。

## 12. 3–6 月
先 identity/topology；实现 TLP-aware matrix；加入 ATS/IOMMU/ACS；做 same/nested switch 与双向测试；接 peer mapping prototype。

## 13. 1–2 年
dma-buf P2P、peer PTE、fabric health/reset、shared VM、multi-GPU UVM、CXL/fabric topology。

## 14. Cross-Owner
Memory 消费 reachability；RAS 提供 device/fabric generation；Virtualization 控制 tenant peer policy；Observability 记录 path/latency；Firmware 可能提供 fabric management。

## 15. Upstream 索引
PCI/P2PDMA v9（2026-10-01，18 patches）明确按 TLP class 与方向判断，并在 v9 暂时移除 dma-buf/mlx5 per-mapping ATS patch，使核心 routing model 先独立收敛。

## 16. Hardware Gates
PCIe topology 是否允许 direct peer route？ACS control 是否可读/可控？ATS/per-mapping ATS？IOMMU peer translation？peer BAR/VRAM aperture？GPU DMA engine 是否支持 peer address？