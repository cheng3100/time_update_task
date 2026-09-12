# CPU↔GPU Migration / Oversubscription / Eviction

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Migration sections
- **类型:** Canonical / upstream architecture
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** GPU SVM 公共设计中的 system↔device migration、CPU fault migration-back 与 eviction 路径。
- **价值点:** 可以把 fault-driven migration、device eviction、CPU fault migration-back 串成完整闭环。
- **学习重点:** migrate-to-RAM/device、retry、range ownership、eviction interaction。
- **学习注意:** 先解决 correctness 再优化 batching/large-page；不要把 migration mechanism 与 residency policy 混在一起。

### 2. NVIDIA Technical Blog — Improving GPU Memory Oversubscription Performance
- **类型:** Implementation / performance engineering blog
- **链接:** https://developer.nvidia.com/blog/improving-gpu-memory-oversubscription-performance/
- **是什么:** 用真实访问模式比较 Unified Memory fault-driven migration、system-memory access 等 oversubscription 策略的性能文章。
- **价值点:** 它把“显存不够就迁移”拆成 working set、访问局部性、GPU residency、fault/migration overhead 等可以测量的变量，是进入 eviction/oversubscription policy 前非常好的工程材料。
- **学习重点:** streaming/random access 对 page fault 的影响、GPU residency 收益、oversubscription 下 fault 与 pinned/system-memory 访问的取舍，以及为什么 workload pattern 会决定最佳策略。
- **学习注意:** benchmark 结论依赖 NVIDIA 平台和 CUDA Unified Memory；不要照搬策略阈值。真正值得迁移到自研 KMD 的是 measurement model：分别测 fault、copy、DMA-map、PTE/TLB、working-set reuse 和 eviction 成本。

### 3. Linux cgroup v2 — Device Memory (DMEM) controller
- **类型:** Canonical / Spec
- **链接:** https://www.kernel.org/doc/html/v7.0/admin-guide/cgroup-v2.html
- **是什么:** Linux cgroup v2 中针对 device-memory region 的 accounting/protection 控制器，定义 `dmem.current`、`dmem.max`、`dmem.min`、`dmem.low` 和 `dmem.capacity` 等语义。
- **价值点:** 它提供了一个权威的上游模型，把显存/设备内存的“用了多少”“硬上限”“保护量”“可回收压力”拆成不同概念，适合用来设计 GPU VRAM pressure、tenant accounting 和 memory QoS 的机制/策略边界。
- **学习重点:** `max/min/low` 语义差异、region/cgroup pool 模型、accounting 与 reclaim 的解耦、保护量如何影响 reclaim 候选，以及 dmem controller 与 TTM/device reclaim callback 的接口边界。
- **学习注意:** 这是 Linux common-control semantic reference，不代表自研 KMD 必须复制相同 cgroup/uAPI。重点学习 accounting/protection/reclaim 分层，而不是文件名本身。

### 4. IGT `cgroup_dmem` eviction tests — synchronous / interruptible / nonblocking reclaim
- **类型:** Implementation / Practice
- **链接:** https://www.mail-archive.com/dri-devel@lists.freedesktop.org/msg632941.html
- **是什么:** IGT 针对 dmem/TTM reclaim 的压力与 eviction 测试，覆盖降低 `dmem.max` 后的同步 eviction、可被 signal 中断的 eviction，以及 `O_NONBLOCK` 下延后 reclaim、再由后续 BO allocation 触发 reclaim 的场景。
- **价值点:** 它把“显存 reclaim 是否正确”从抽象机制转成可执行 test design，尤其适合参考如何验证 limit lowering、usage convergence、interruptibility 和 deferred reclaim。
- **学习重点:** 如何构造稳定 VRAM pressure、如何观察 usage 收敛、同步/异步 reclaim 的完成语义、被中断后的状态恢复，以及后续 allocation 如何继续驱动 reclaim。
- **学习注意:** IGT 场景建立在 DRM/TTM/dmem cgroup 上；自研 KMD 应迁移 test invariant 和 pressure methodology，不要机械复制具体 ioctl/TTM helper。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
