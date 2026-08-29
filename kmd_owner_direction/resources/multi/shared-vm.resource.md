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

### 3. DRM Fabric RFC — vendor-neutral scale-up accelerator topology
- **类型:** Canonical / RFC architecture
- **链接:** https://lkml.iu.edu/2608.3/00335.html
- **是什么:** 2026-08-24 提出的 DRM 公共 fabric topology infrastructure，使用 `fabric → endpoint → port → peer` 对 GPU/AI accelerator 的 scale-up interconnect 建模，协议无关、厂商无关。
- **价值点:** 它把“topology 公共层”和“vendor data path / firmware / memory semantics”边界讲得非常清楚；peer 还是 typed identity/value，而不是必须解析成 live local object，这对跨 OS、switch、动态设备生命周期很重要。
- **学习重点:** object identity/lifetime、direct adjacency vs reachability、directed half-edge、port operational state/counters、provider ownership、未来 privileged provisioning。
- **学习注意:** 仍是 RFC，generic-netlink/uAPI/object details 都可能变化；优先学习模型和边界，不绑定当前接口。

### 4. AMDGPU UALink infrastructure — remote memory / TLB / interrupt / reset
- **类型:** Implementation / Practice
- **链接:** https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg149538.html
- **是什么:** 2026-08-21 AMD 发出的 UALink/AMDGPU 大型 patch series，覆盖 pod configuration、NPA、remote state、cross-GPU TLB shootdown/interrupt、memory export/import/revoke、connection reset、peer PTE mapping。
- **价值点:** 与 DRM Fabric 形成很好的对照：DRM Fabric 展示 common topology layer，UALink 展示 vendor-specific transport/memory/control path 到底复杂在哪里。
- **学习重点:** remote state/ring、peer authorization、remote invalidation、connection reset、NPA mapping、opaque handle、FW mailbox/ring integration。
- **学习注意:** 不要把 AMD UALink 具体协议上升为通用 DRM 语义；抽取 topology/control/memory boundary 和 generation/lifetime 设计。

### 5. fabric_ext paper
- **类型:** Research / long-term architecture radar
- **链接:** https://arxiv.org/abs/2607.26335
- **是什么:** 研究跨 GPU/DPU/CXL fabric 的 observability/policy 抽象。
- **价值点:** 把 Fabric Owner 从“P2P copy”扩展到 movement/ordering/ownership/link-health 的长期视角。
- **学习重点:** movement graph、ordering/ownership、跨设备 policy hooks。
- **学习注意:** 研究性强，当前仅作为长期架构雷达，不应产品化照搬。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
