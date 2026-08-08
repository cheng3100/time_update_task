# Secure Boot / Measurement / Scrub / Attestation

## High-value learning resources
### 1. Nova FWSEC
- **链接:** https://docs.kernel.org/gpu/nova/core/fwsec.html
- **是什么:** NVIDIA/Nova GPU firmware secure boot/verification 链路的官方文档。
- **价值点:** 把 reset 后的 firmware trust chain、ucode verification 与 GPU bring-up 串起来。
- **学习重点:** FWSEC 在 boot chain 中的位置、验证对象与失败模式。
- **学习注意:** Firmware authenticity 只是 confidential GPU 的一部分；memory isolation/attestation 是后续层。
