# Multi-GPU Unified Memory

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Multi-GPU / N:1
- **链接:** https://docs.kernel.org/next/gpu/rfc/gpusvm.html
- **是什么:** GPU SVM 对一个 CPU VA range 被多个 GPU device 独立映射的未来模型。
- **价值点:** 直接帮助设计 multi-GPU residency、per-device DMA mapping 与 shared VA 数据模型。
- **学习重点:** N:1 representation、多设备 pages/mapping 与 multi-GPU future work。
- **学习注意:** 不要简单把 single-GPU residency 字段扩成数组；先区分 logical range 与 per-device state。

### 2. AMDGPU UALink infrastructure / remote-memory design — 2026-08
- **类型:** Implementation / Practice + upstream design
- **链接:** https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html
- **是什么:** AMDGPU 面向 UALink scale-up pod 的完整 remote-memory 系列，定义 NPA（Network Physical Address）空间、peer memory export/import authorization、remote PTE、remote TLB shootdown、presence retry 与 connection reset。
- **价值点:** 它把 multi-GPU shared-memory correctness 从“多个 GPU 映射同一 range”的抽象推进到 exporter/importer mapping lifetime、memory eviction/revocation 和跨 GPU invalidation protocol，是当前非常少见的 production-oriented 实现参考。
- **学习重点:** exported memory 不永久 pin；TTM eviction/MMU notifier 如何触发 remote TLB shootdown；importer presence check/retry；opaque handle 与 remote PTE；local/remote mapping generation 的必要性。
- **学习注意:** UALink/NPA 是 AMD 的具体 fabric/driver 方案，不应照搬 wire protocol 或地址布局。学习的是 ownership、authorization、invalidation、retry、generation 和 mapping-lifetime 模型。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
