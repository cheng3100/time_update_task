# GPU Resource Partition / VMID / Queue / Doorbell / Memory

## High-value learning resources
### 1. Intel Xe SR-IOV configfs
- **链接:** https://docs.kernel.org/gpu/xe/xe_configfs.html
- **是什么:** Intel Xe 对 PF mode 与 VF 数量/资源配置的用户接口文档。
- **价值点:** 提供 GPU virtualization 在 probe 前决定硬件 resource mode 的工程实例。
- **学习重点:** PF/native mode、max_vfs 生命周期、资源配置位置。
- **学习注意:** 学习 control-plane 边界，不应复制 Intel-specific ABI。
