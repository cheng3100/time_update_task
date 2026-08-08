# Recoverable GPU Page Fault / Fault Replay

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC
- **类型:** Canonical / upstream architecture
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** Linux DRM 面向 GPU shared virtual memory、device-private memory 与迁移的公共设计文档。
- **价值点:** 把 GPU fault、HMM、migration、device memory 和 future multi-GPU 放在同一设计中，是当前最重要的 upstream 架构参考之一。
- **学习重点:** GPU fault handler、retry/concurrency、migrate-to-RAM/device、N:1 设备模型。
- **学习注意:** RFC 仍在演进，适合作为架构方向和问题模型，不应把当前 API 当成冻结 ABI。

### 2. NVIDIA Technical Blog — Unified Memory for CUDA Beginners
- **类型:** Deep explanation / vendor engineering blog
- **链接:** https://developer.nvidia.com/blog/unified-memory-cuda-beginners/
- **是什么:** 从 Pascal 的 Page Migration Engine 和硬件 page faulting 出发解释 Unified Memory demand paging 的工程文章。
- **价值点:** 很适合把抽象的“GPU fault → residency resolution → page migration → resume”转成具体硬件/软件执行过程；对理解为什么 fault replay 需要和 migration、VA、context lifetime 联动非常有帮助。
- **学习重点:** GPU page fault、Page Migration Engine、first-touch/demand paging、CPU/GPU 访问导致的 residency 变化，以及 multi-GPU Unified Memory 的基本行为。
- **学习注意:** 这是 CUDA/NVIDIA 实现视角，不代表 Linux DRM/HMM API；学习的是 fault-driven unified-memory 的工程模型，不应把 CUDA runtime 行为直接映射成自研 KMD 接口。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
