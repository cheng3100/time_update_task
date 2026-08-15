# NUMA / Large & Compound Pages / Migration Granularity

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Future design
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** 当前 upstream 对 compound device pages、higher-order DMA mapping 与 migration 开销的讨论入口。
- **价值点:** 帮助建立 CPU base page、migration unit、DMA mapping unit、GPU PTE unit 不一定相同的架构意识。
- **学习重点:** compound device pages、higher-order mapping、core-MM migration overhead。
- **学习注意:** 很多内容仍是 future work；重点学习抽象边界，而不是寻找可直接复制的现成接口。

### 2. Intel Xe GT Statistics — SVM page-size / migration measurement
- **类型:** Canonical / implementation measurement reference
- **链接:** https://docs.kernel.org/next/gpu/xe/xe_gt_stats.html
- **是什么:** Xe KMD 的 per-GT debugfs statistics 设计，已经把 SVM page fault、migration、CPU/device copy、get-pages、GPU bind、TLB invalidation 等指标按 4K / 64K / 2M 粒度拆分统计。
- **价值点:** 对 migration granularity 最有价值的不是某个 Xe API，而是它展示了一套可以真实回答“64K/2M 是否比 4K 更值”的 measurement schema；可以直接启发自研 KMD 在优化前先建立可量化基线。
- **学习重点:** `SVM_*_PAGEFAULT_*`、`SVM_*_MIGRATE_*`、copy time/bytes、get-pages time、bind time、TLB invalidation time，以及 page-reclaim-list counters。
- **学习注意:** 这是 debugfs/driver-internal statistics，不应直接照搬成稳定 uAPI。重点学习指标分解和低开销 per-CPU 计数方式；最终产品 telemetry 是否通过 debugfs、tracepoint、perf 或私有工具暴露需另行设计。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
