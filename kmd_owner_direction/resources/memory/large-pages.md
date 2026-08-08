# NUMA / Large & Compound Pages / Migration Granularity

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Future design
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** 当前 upstream 对 compound device pages、higher-order DMA mapping 与 migration 开销的讨论入口。
- **价值点:** 帮助建立 CPU base page、migration unit、DMA mapping unit、GPU PTE unit 不一定相同的架构意识。
- **学习重点:** compound device pages、higher-order mapping、core-MM migration overhead。
- **学习注意:** 很多内容仍是 future work；重点学习抽象边界，而不是寻找可直接复制的现成接口。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
