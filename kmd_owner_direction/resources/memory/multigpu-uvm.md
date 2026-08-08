# Multi-GPU Unified Memory

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DRM GPU SVM RFC — Multi-GPU / N:1
- **链接:** https://docs.kernel.org/next/gpu/rfc/gpusvm.html
- **是什么:** GPU SVM 对一个 CPU VA range 被多个 GPU device 独立映射的未来模型。
- **价值点:** 直接帮助设计 multi-GPU residency、per-device DMA mapping 与 shared VA 数据模型。
- **学习重点:** N:1 representation、多设备 pages/mapping 与 multi-GPU future work。
- **学习注意:** 不要简单把 single-GPU residency 字段扩成数组；先区分 logical range 与 per-device state。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
