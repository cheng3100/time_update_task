# dma-buf / P2P Memory

**Owner:** Memory / Virtual Memory / Unified Memory

## High-value learning resources

### 1. DMA-BUF documentation
- **链接:** https://docs.kernel.org/driver-api/dma-buf.html
- **是什么:** Linux 跨设备 buffer sharing、reservation/fence 与 attachment 的核心接口文档。
- **价值点:** 理解 GPU 与显示、视频、其他 accelerator 共享 memory object 的标准路径。
- **学习重点:** exporter/importer、attachment、`map_dma_buf`、reservation object。
- **学习注意:** dma-buf 解决共享对象与同步，不自动解决 peer physical addressability 或 multi-GPU migration。

### 2. PCI P2PDMA documentation
- **链接:** https://docs.kernel.org/driver-api/pci/p2pdma.html
- **是什么:** Linux PCIe peer-to-peer DMA 的拓扑可达性与资源管理文档。
- **价值点:** 理解 ACS/root complex/topology 为什么直接限制 P2P。
- **学习重点:** provider/client/orchestrator 与 topology/distance check。
- **学习注意:** PCI P2PDMA 是通用框架，不等同于 GPU peer VA/PTE 模型。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
