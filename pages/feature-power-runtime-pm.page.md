---
layout: default
title: "Feature HLD · GPU Utilization Accounting → Runtime PM / DVFS"
parent: GPU KMD Owner Direction
permalink: /kmd_owner_direction/features/power-runtime-pm.html
---
# GPU Utilization Accounting → Runtime PM / DVFS

## 1. 一句话定义
先准确回答“GPU/engine 何时真的忙、谁仍需要硬件、当前频率/电源状态是什么”，再安全地执行 runtime suspend/resume 和 DVFS。

## 2. 背景与位置
Power Owner 不是“写一个降频函数”。它连接 scheduler activity、async worker lifetime、FW PM protocol、clock/power domain、PCIe D-state 与 thermal policy。

## 3. 解决的问题
没有可信 accounting，DVFS 无法验证；没有 lifetime model，fault worker/FW request/telemetry 仍在运行时设备可能被 suspend；没有 quiesce transaction，低功耗切换与 reset/remove 会产生竞态。

## 4. 典型场景
engine idle 后 autosuspend；fault worker 唤醒设备；FW command 持有 PM ref；频率按 busy window 调节；system suspend 与 recovery 并发。

## 5. 核心对象
engine busy interval、utilization window、PM reference/reason、quiesce token、runtime state、frequency residency、OPP、thermal/power limit、wake source。

## 6. 控制流
activity begin→busy/account+PM ref→work→activity end→idle window→policy→quiesce/admission drain→FW/clock/power transition→residency telemetry→resume on demand。

## 7. 边界
KMD 负责 activity/lifetime/policy orchestration；FW/HW 执行 clock/power transition；Linux runtime PM/PCI 管理通用 device state；UMD 只能提供 workload hint，不能决定底层安全 quiesce。

## 8. 生命周期
ACTIVE → IDLE_CANDIDATE → QUIESCING → SUSPENDED → RESUMING → ACTIVE；任一 quiesce 条件失败则 rollback 到 ACTIVE。

## 9. 难点
nested PM refs、异步 workqueue、reset/suspend/remove ordering、FW readiness、PCIe D-state、多个 power domain dependency、utilization sampling bias、频率变化与 counter clock domain。

## 10. Failure / Debug
记录 PM ref owner/reason、last busy、quiesce blockers、suspend/resume latency、wake reason、frequency residency、failed transition stage、rollback reason。

## 11. 最小闭环
per-engine busy/idle + PM lifetime + runtime suspend/resume + quiesce/drain + transition latency + frequency residency；复杂 governor 后置。

## 12. 3–6 月
先 measurement contract；再 runtime PM transaction；之后 basic OPP/DVFS，加入 fault/FW/telemetry worker race tests。

## 13. 1–2 年
thermal/power cap、memory bandwidth feedback、per-workload QoS、partition-aware power、energy attribution。

## 14. Cross-Owner
RAS 与 Power 共享 admission/drain；Firmware 提供 PM service；Observability 提供 counters/timeline；Memory fault/migration 是重要 PM client；Virtualization 需要 tenant accounting。

## 15. Upstream 索引
Linux Runtime PM 是 canonical lifecycle；Xe/AMDGPU PM 实现用于研究 GPU-specific quiesce、FW 与 PCI state 组合。

## 16. Hardware Gates
clock/power domain 拓扑？独立 engine gating？频率切换 latency？FW 是否独占 DVFS？可靠 busy counter/energy counter？D3hot/D3cold/wakeup 支持？