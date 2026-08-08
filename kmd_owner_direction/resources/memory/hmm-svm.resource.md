# mmu_notifier / HMM / SVM / Device-private Memory

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. Linux HMM documentation
- **类型:** Canonical / official
- **链接:** https://docs.kernel.org/mm/hmm.html
- **是什么:** Linux heterogeneous memory management 的核心官方文档，解释 device 如何 mirror CPU address space。
- **价值点:** 是理解 GPU 跟踪 CPU PTE、device-private page 与 migration 的基础。
- **学习重点:** `hmm_range_fault`、device-private pages、migration helper、MM lifetime。
- **学习注意:** HMM 提供机制，不替 GPU KMD 定义 fault replay、GPU PTE 或 residency policy。

### 2. MMU Notifier documentation
- **类型:** Canonical / official
- **链接:** https://docs.kernel.org/mm/mmu_notifier.html
- **是什么:** Linux MM 通知外部 MMU/设备页表 CPU PTE 失效和替换的机制。
- **价值点:** 直接决定 GPU PTE/TLB 与 CPU page-table 修改之间的 correctness。
- **学习重点:** invalidate ordering、COW/PTE replacement、locking 与 device TLB invalidation。
- **学习注意:** 不要只记 callback 名称；关键是 CPU PTE 修改与 device mapping invalidation 的先后约束。

### 3. LWN — Heterogeneous memory management and MMU notifiers
- **类型:** Deep explanation / LWN
- **链接:** https://lwn.net/Articles/752964/
- **是什么:** Jonathan Corbet 对 HMM 与 MMU notifier 设计背景、GPU 地址空间镜像、迁移动机和 notifier 依赖关系的深度解释。
- **价值点:** 官方 API 文档告诉你“接口怎么用”，这篇文章更适合建立“为什么 Linux MM 需要 HMM、为什么不能简单长期 pin 用户页、为什么 notifier 是 correctness 核心”的系统直觉。
- **学习重点:** address-space mirroring、device memory、HMM 与 `get_user_pages()` 思路差异、MMU notifier 在 CPU/GPU 页表同步中的角色。
- **学习注意:** 文章来自 HMM 较早期阶段，API 名称和实现细节可能已变化；把它用于理解设计动机和问题模型，再回到当前 kernel docs/源码确认接口。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。长期资料优先形成 Canonical → Deep Explanation → Implementation/Practice 的互补层次，而不是只收官方 API 文档。
