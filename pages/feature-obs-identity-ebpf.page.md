---
layout: default
title: "Feature HLD · Stable GPU Object/Event Identity + eBPF Trace"
parent: GPU KMD Owner Direction
permalink: /kmd_owner_direction/features/obs-identity-ebpf.html
---
# Stable GPU Object/Event Identity + eBPF KMD Trace

## 1. 一句话定义
先为 device/client/PID/PASID/VM/context/queue/job/fault/migration/FW request/recovery 建立可跨生命周期关联的 identity，再让 tracepoint/eBPF/software counter/PMU/SPM/crash dump 共享同一语义。

## 2. 背景与位置
Observability 不是 printk 集合。它横跨 UMD→KMD→FW→GPU，并为 Memory/RAS/Power/Virtualization 提供“发生了什么、属于谁、在 reset 前还是后”的共同时间线。

## 3. 解决的问题
函数级 kprobe 能看到调用，却回答不了某 fault 属于哪个 VM/job、某 FW completion 是否跨 reset、某 PMU sample 属于哪个 process。没有稳定 identity，数据越多反而越难关联。

## 4. 典型场景
fault latency breakdown；hang 前最后 N 个 job；per-process utilization；FW timeout 与 queue/job 关联；reset 前后同名 queue 防误关联；eBPF 临时诊断。

## 5. 核心对象
device_id/client_id/PID/PASID/VM/context/queue/job/fault/request IDs、recovery_generation、event schema/version、timestamp domain、profiler_session、counter buffer。

## 6. 数据流
object lifecycle → stable IDs → tracepoint/schema → eBPF/consumer → timeline/counters；PMU/SPM 与 FW event 后续通过同一 identity/generation 关联。

## 7. 边界
各 Owner 产生语义事件；Observability Owner 定义公共 identity/schema/timestamp/correlation contract，不替代各域内部状态机。

## 8. 生命周期
ALLOC → PUBLISHED → ACTIVE → DYING → RETIRED；ID 不应在仍可能存在延迟事件时立即复用。profiler session 另有 acquire/configure/run/stop/release/reset-invalidated 生命周期。

## 9. 难点
ID reuse、object free 后 late event、trace overhead、schema stability、BTF/CO-RE、timestamp clock-domain correlation、PMU attribution、security/privacy。

## 10. Failure / Debug
必须能发现 dropped events、buffer overflow、unknown/stale ID、timestamp skew、counter multiplex error；reset_generation 是核心 correlation key。

## 11. 最小闭环
stable object IDs + lifecycle tracepoints + eBPF CO-RE consumer + software counters + reset-generation correlation + basic timeline exporter。

## 12. 3–6 月
定义 schema/ID；覆盖 submission/fault/FW/reset；eBPF 工具；latency/counter dashboard；profiler resource prototype。

## 13. 1–2 年
PMU/SPM、per-process profiling、perf_event integration、UMD/FW/GPU timestamp correlation、dynamic diagnostics/programmable hooks。

## 14. Cross-Owner
Memory/RAS/FW/Power/Virtualization/Multi-GPU 都是事件 producer；Observability 提供统一 correlation，不拥有它们的 policy。

## 15. Upstream 索引
AMDGPU profiler/SPM 12-patch discussion 的重要启示是先定义 profiler resource ownership/lifetime，再暴露 ABI；DRM usage stats 是稳定 userspace accounting 的参考。

## 16. Hardware Gates
是否有 per-context/VMID counter？SPM buffer/interrupt？counter multiplex？GPU timestamp 与 host clock correlation？FW 是否能附带 stable object IDs？