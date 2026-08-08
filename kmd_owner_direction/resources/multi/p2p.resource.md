# P2P Capability / Peer BAR / Peer PTE

## High-value learning resources
### 1. PCI P2PDMA
- **链接:** https://docs.kernel.org/driver-api/pci/p2pdma.html
- **是什么:** Linux PCI P2P DMA 的拓扑判定与资源暴露文档。
- **价值点:** 帮助定义“能否 P2P”应是结构化 capability，而不是单一 boolean。
- **学习重点:** topology distance、provider/client/orchestrator。
- **学习注意:** GPU peer PTE/shared VA 是更高层能力，不能由 PCI P2PDMA 可达性自动推出。
