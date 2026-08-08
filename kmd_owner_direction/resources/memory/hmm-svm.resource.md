# mmu_notifier / HMM / SVM / Device-private Memory

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. Linux HMM documentation
- **链接:** https://docs.kernel.org/mm/hmm.html
- **是什么:** Linux heterogeneous memory management 的核心官方文档，解释 device 如何 mirror CPU address space。
- **价值点:** 是理解 GPU 跟踪 CPU PTE、device-private page 与 migration 的基础。
- **学习重点:** `hmm_range_fault`、device-private pages、migration helper、MM lifetime。
- **学习注意:** HMM 提供机制，不替 GPU KMD 定义 fault replay、GPU PTE 或 residency policy。

### 2. MMU Notifier documentation
- **链接:** https://docs.kernel.org/mm/mmu_notifier.html
- **是什么:** Linux MM 通知外部 MMU/设备页表 CPU PTE 失效和替换的机制。
- **价值点:** 直接决定 GPU PTE/TLB 与 CPU page-table 修改之间的 correctness。
- **学习重点:** invalidate ordering、COW/PTE replacement、locking 与 device TLB invalidation。
- **学习注意:** 不要只记 callback 名称；关键是 CPU PTE 修改与 device mapping invalidation 的先后约束。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
