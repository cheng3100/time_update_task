# Shared VA / Multi-GPU VM / Fabric Health

## High-value learning resources
### 1. DRM GPU SVM RFC
- **链接:** https://docs.kernel.org/next/gpu/rfc/gpusvm.html
- **是什么:** GPU shared virtual memory 与 N:1 多设备映射的 upstream 设计。
- **价值点:** 直接用于理解 one logical range → per-device residency/mapping 的 multi-GPU 数据模型。
- **学习重点:** N:1、multi-GPU future work、device-specific mapping。
- **学习注意:** 仍处演进期，先学习抽象和数据模型，不绑定具体 API。

### 2. fabric_ext paper
- **链接:** https://arxiv.org/abs/2607.26335
- **是什么:** 研究跨 GPU/DPU/CXL fabric 的 observability/policy 抽象。
- **价值点:** 把 Fabric Owner 从“P2P copy”扩展到 movement/ordering/ownership/link-health 的长期视角。
- **学习重点:** movement graph、ordering/ownership、跨设备 policy hooks。
- **学习注意:** 研究性强，当前仅作为长期架构雷达，不应产品化照搬。
