# Sequence ID / Async Completion / Timeout / Error

## High-value learning resources
### 1. Nova Core Guidelines
- **链接:** https://docs.kernel.org/next/gpu/nova/core/guidelines.html
- **是什么:** Nova core 的 firmware abstraction/guideline 文档。
- **价值点:** 帮助建立稳定 host-facing API 与实际 FW request/response 的隔离。
- **学习重点:** sequence、async completion、error normalization 应作为统一 service contract 设计。
- **学习注意:** 不同 FW service 不应各自发明 timeout/error 语义。
