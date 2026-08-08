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

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
