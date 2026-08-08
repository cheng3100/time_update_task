# FW Health / Logs / Authentication / Measurement

## High-value learning resources
### 1. Nova Core TODO
- **链接:** https://docs.kernel.org/gpu/nova/core/todo.html
- **是什么:** 包含 GSP log retention、probe failure diagnostics 等现实工程问题。
- **价值点:** 适合定义 FW health/log 为正式 control-plane service。
- **学习重点:** logs 在 probe failure 后仍应导出的需求。
- **学习注意:** log retention 属于诊断基础设施，不应只在 debug build 可用。

### 2. Nova FWSEC
- **链接:** https://docs.kernel.org/gpu/nova/core/fwsec.html
- **是什么:** Nova/NVIDIA firmware secure boot/verification 链路文档。
- **价值点:** 用于建立 reset→FWSEC→ucode verification→GSP/PMU 的 trust chain 概念。
- **学习重点:** 验证阶段、firmware trust root、failure behavior。
- **学习注意:** 认证只是安全边界的一部分，还需与 secure reset/memory scrub/attestation 结合。
