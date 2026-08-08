# Resource Ownership / State Reconciliation

## High-value learning resources
### 1. Nova architecture
- **链接:** https://docs.kernel.org/gpu/nova/index.html
- **是什么:** nova-core 与上层 client 的分层架构。
- **价值点:** 适合思考 KMD/FW 谁拥有 queue/context/VM/engine state，以及 restart 后谁负责重建。
- **学习重点:** lower core 作为共享 HW/FW abstraction 的责任边界。
- **学习注意:** state reconciliation 是自研协议问题，Nova 主要提供架构参照。
