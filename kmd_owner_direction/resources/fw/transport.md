# Shared-memory / Ring / Mailbox Transport

## High-value learning resources
### 1. Nouveau / GSP documentation
- **链接:** https://docs.kernel.org/gpu/nouveau.html
- **是什么:** Nouveau/NVIDIA GSP command/status queue 与 firmware communication 的官方入口。
- **价值点:** 为 GPU firmware ring/mailbox/shared-memory control path 提供成熟案例。
- **学习重点:** command queue、status/event queue、doorbell/notification 语义。
- **学习注意:** transport 只是承载层；message ABI/version/error semantics 应与 transport 解耦。
