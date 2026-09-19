# Secure Boot / Measurement / Scrub / Attestation

## High-value learning resources
### 1. Nova FWSEC
- **链接:** https://docs.kernel.org/gpu/nova/core/fwsec.html
- **是什么:** NVIDIA/Nova GPU firmware secure boot/verification 链路的官方文档。
- **价值点:** 把 reset 后的 firmware trust chain、ucode verification 与 GPU bring-up 串起来。
- **学习重点:** FWSEC 在 boot chain 中的位置、验证对象与失败模式。
- **学习注意:** Firmware authenticity 只是 confidential GPU 的一部分；memory isolation/attestation 是后续层。

### 2. AMDGPU Process Isolation（Canonical / Implementation boundary）
- **链接:** https://docs.kernel.org/gpu/amdgpu/process-isolation.html
- **是什么:** AMDGPU 对 graphics engine 进程隔离和 cleaner shader 的官方说明；可在进程切换时清理 LDS/GPR，并支持 partition-aware isolation。
- **价值点:** 展示 GPU 安全隔离不只发生在 IOMMU/VF/VM 边界，shader architectural state 也可能跨 workload 泄漏，需要显式 scrub/serialization 机制。
- **学习重点:** cleaner shader、LDS/GPR state、job serialization、per-partition enable、manual cleanup 与自动 isolation 的边界。
- **学习注意:** 这不是 SR-IOV/VFIO/IOMMU isolation 的替代品；它解决的是执行单元残留状态与跨进程 confidentiality，应作为多层隔离模型中的补充层理解。
