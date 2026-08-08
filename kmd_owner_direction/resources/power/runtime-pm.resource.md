# Runtime PM / Suspend-Resume / PCI D-states

## High-value learning resources
### 1. Xe Power Management
- **链接:** https://docs.kernel.org/gpu/xe/xe_pm.html
- **是什么:** Intel Xe runtime/system PM、D3hot/D3cold 与 GPU lifetime 管理官方文档。
- **价值点:** 展示真实 GPU KMD 如何把 PM reference 与 ioctl/dma-buf/execution/VRAM 条件绑定。
- **学习重点:** outer PM refs、VRAM constraints、D-state transitions、resume path。
- **学习注意:** PM correctness 优先于节能收益；所有 active path 必须有明确 reference 规则。
