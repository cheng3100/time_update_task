# Runtime PM / Suspend-Resume / PCI D-states

## High-value learning resources

### 1. Xe Power Management
- **类型:** Canonical / official
- **链接:** https://docs.kernel.org/gpu/xe/xe_pm.html
- **是什么:** Intel Xe runtime/system PM、D3hot/D3cold 与 GPU lifetime 管理官方文档。
- **价值点:** 展示真实 GPU KMD 如何把 PM reference 与 ioctl/dma-buf/execution/VRAM 条件绑定。
- **学习重点:** outer PM refs、VRAM constraints、D-state transitions、resume path。
- **学习注意:** PM correctness 优先于节能收益；所有 active path 必须有明确 reference 规则。

### 2. LWN / upstream patch series — Power Management for Raspberry Pi V3D GPU
- **类型:** Implementation / upstream engineering case study
- **链接:** https://lwn.net/Articles/1059534/
- **是什么:** V3D GPU 引入 Runtime PM 的完整 upstream patch-series 说明，展示如何让 GPU idle 时真正关闭 clock，并处理 firmware clock hooks 和 driver resource ordering。
- **价值点:** 相比成熟 Xe 文档，这个案例更容易看清“从没有 Runtime PM 到加入 Runtime PM”需要改哪些 driver 生命周期和资源顺序，非常适合作为自研 KMD 第一次做 PM bring-up 的参考。
- **学习重点:** idle clock gating、runtime PM enablement、资源必须在 clock enable 前完成初始化、firmware clock prepare/unprepare，以及 submit/IRQ/MMU 路径如何适配 PM state。
- **学习注意:** V3D 硬件比大型独显简单，不应照搬实现；重点学习 enablement sequence、lifetime ordering 和如何把 PM correctness 拆成可 review 的小 patch。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
