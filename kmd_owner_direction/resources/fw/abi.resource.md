# Versioned Firmware ABI / Command & Event Namespace

## High-value learning resources
### 1. Nova Core Guidelines
- **链接:** https://docs.kernel.org/next/gpu/nova/core/guidelines.html
- **是什么:** Nova 对 firmware-version-independent core API 的架构规则。
- **价值点:** 最直接支持“FW version translation 应集中在 lower layer”的设计原则。
- **学习重点:** second-level driver 不应看到 version-specific FW structures/semantics。
- **学习注意:** 不要照搬 Nova API；应抽象适合自研 GPU 的 version/capability contract。
