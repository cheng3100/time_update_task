# P2P DMA / Cross-GPU dma-buf

## High-value learning resources
### 1. DMA-BUF documentation
- **链接:** https://docs.kernel.org/driver-api/dma-buf.html
- **是什么:** 跨设备 buffer sharing 和同步的标准 Linux 框架。
- **价值点:** 跨 GPU buffer export/import 与 fence/reservation 的基础。
- **学习重点:** attachment/map、dma_resv/fence、implicit/explicit sync。
- **学习注意:** dma-buf 不解决 peer aperture/ATS/IOMMU topology，本层仍需独立 capability check。
