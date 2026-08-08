# Shared VA / Multi-GPU VM / Fabric Health

## High-value learning resources

### 1. DRM GPU SVM RFC
- **类型:** Canonical / upstream architecture
- **链接:** https://docs.kernel.org/next/gpu/rfc/gpusvm.html
- **是什么:** GPU shared virtual memory 与 N:1 多设备映射的 upstream 设计。
- **价值点:** 直接用于理解 one logical range → per-device residency/mapping 的 multi-GPU 数据模型。
- **学习重点:** N:1、multi-GPU future work、device-specific mapping。
- **学习注意:** 仍处演进期，先学习抽象和数据模型，不绑定具体 API。

### 2. NVIDIA Technical Blog — Fast Multi-GPU collectives with NCCL
- **类型:** Deep explanation / topology-aware multi-GPU engineering
- **链接:** https://developer.nvidia.com/blog/fast-multi-gpu-collectives-nccl/
- **是什么:** 从 PCIe 树、GPU ring ordering、GPUDirect P2P 和 collective bandwidth 解释 multi-GPU topology 为什么直接影响通信性能的经典工程文章。
- **价值点:** 虽然 NCCL 位于 runtime/library 层，但它非常直观地说明 KMD 为什么需要提供准确的 stable identity、peer-access capability 和 topology 信息；上层只有拿到这些基础事实才能做正确 policy。
- **学习重点:** PCIe root/switch topology、peer access、ring ordering、跨 root 的 staged transfer、topology-aware communication。
- **学习注意:** Collective algorithm 不属于 KMD Owner；KMD 要学习的是“必须暴露什么 topology/capability primitive”，不要把 NCCL policy 下沉进 kernel。

### 3. fabric_ext paper
- **类型:** Research / long-term architecture radar
- **链接:** https://arxiv.org/abs/2607.26335
- **是什么:** 研究跨 GPU/DPU/CXL fabric 的 observability/policy 抽象。
- **价值点:** 把 Fabric Owner 从“P2P copy”扩展到 movement/ordering/ownership/link-health 的长期视角。
- **学习重点:** movement graph、ordering/ownership、跨设备 policy hooks。
- **学习注意:** 研究性强，当前仅作为长期架构雷达，不应产品化照搬。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
