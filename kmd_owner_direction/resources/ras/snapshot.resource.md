# Hang Snapshot / devcoredump / Reset Reason

## High-value learning resources

### 1. Xe Device Coredump
- **类型:** Canonical / upstream implementation
- **链接:** https://docs.kernel.org/gpu/xe/xe_devcoredump.html
- **是什么:** Linux devcoredump 上实现 GPU hang snapshot 的生产案例。
- **价值点:** 最直接说明为什么必须 snapshot-at-hang、read-later。
- **学习重点:** snapshot content、lifetime、first failure、userspace retrieval。
- **学习注意:** 不要在 reset 之后重新读取 live register 拼 crash dump。

### 2. AMD GPUOpen — Hardware Crash Analysis with Radeon GPU Detective
- **类型:** Implementation / GPU crash-analysis engineering article
- **链接:** https://gpuopen.com/learn/rgd-hardware-crash-analysis/
- **是什么:** AMD 介绍 Radeon GPU Detective 如何将 GPU crash dump 中的硬件状态、执行中的 shader/workload 与故障位置关联起来的技术文章。
- **价值点:** 很适合回答“一个有用的 GPU coredump 到底应该保存什么”。它把 crash artifact 从寄存器 dump 提升到 execution marker、page fault/resource、shader/hardware-state correlation 的层次。
- **学习重点:** post-mortem crash workflow、hardware state、in-flight workload、execution marker、page-fault/resource correlation，以及离线工具如何消费 dump。
- **学习注意:** RGD 面向 AMD 图形/应用工具链，不能直接作为 Linux KMD uAPI 模板；重点学习 crash artifact 的信息层次和 producer/consumer 分离。

### 3. NVIDIA Technical Blog — Speed Up GPU Crash Debugging with Nsight Aftermath
- **类型:** Implementation / vendor crash-debugging practice
- **链接:** https://developer.nvidia.com/blog/speed-up-gpu-crash-debugging-with-nvidia-nsight-aftermath/
- **是什么:** 介绍 GPU mini-dump、MMU fault、warp/shader 状态和应用 marker 如何组合做离线 GPU crash 定位。
- **价值点:** 与 RGD 形成跨厂商对照，说明生产级 GPU crash 诊断普遍走向“结构化 dump + workload marker + MMU/hardware state + offline decoder”。
- **学习重点:** crash dump lifetime、marker、MMU fault information、shader correlation、线上采集与离线分析边界。
- **学习注意:** 这是 application-facing SDK/tooling 视角；KMD 应学习所需底层证据，而不是复制其 API。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
