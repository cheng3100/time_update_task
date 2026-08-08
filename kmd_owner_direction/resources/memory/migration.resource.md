# CPU↔GPU Migration / Oversubscription / Eviction

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Migration sections
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** GPU SVM 公共设计中的 system↔device migration、CPU fault migration-back 与 eviction 路径。
- **价值点:** 可以把 fault-driven migration、device eviction、CPU fault migration-back 串成完整闭环。
- **学习重点:** migrate-to-RAM/device、retry、range ownership、eviction interaction。
- **学习注意:** 先解决 correctness 再优化 batching/large-page；不要把 migration mechanism 与 residency policy 混在一起。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
