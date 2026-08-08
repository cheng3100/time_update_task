# Recoverable GPU Page Fault / Fault Replay

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC
- **链接:** https://docs.kernel.org/gpu/rfc/gpusvm.html
- **是什么:** Linux DRM 面向 GPU shared virtual memory、device-private memory 与迁移的公共设计文档。
- **价值点:** 把 GPU fault、HMM、migration、device memory 和 future multi-GPU 放在同一设计中，是当前最重要的 upstream 架构参考之一。
- **学习重点:** GPU fault handler、retry/concurrency、migrate-to-RAM/device、N:1 设备模型。
- **学习注意:** RFC 仍在演进，适合作为架构方向和问题模型，不应把当前 API 当成冻结 ABI。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
