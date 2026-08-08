# GPUVM / Page Tables / VMID / PASID / TLB

**Owner:** Memory / Virtual Memory / Unified Memory

## Stable learning scope
本页只维护该子方向长期有效的学习路径与高价值资料，不记录每期行业新闻。内容采用稳定增长方式维护。

## High-value learning resources

### 1. Linux DRM GPUVM / DRM MM documentation
- **链接:** https://docs.kernel.org/gpu/drm-mm.html
- **是什么:** Linux DRM 中 GPU virtual address、VM 管理及相关内存管理基础设施的官方文档入口。
- **价值点:** 建立 GPUVM、VA 管理、锁与对象生命周期的 upstream 视角，便于把 vendor KMD 设计与 Linux 公共抽象对齐。
- **学习重点:** GPU VA 对象、VM lifetime、锁顺序，以及 GPUVM 与 BO/exec 的关系。
- **学习注意:** DRM 公共抽象不等同于具体 GPU 硬件页表格式；硬件 page-table walker/MMU 仍需单独理解。

## Maintenance notes
- 新资料默认追加，不因每期定时更新重新排序或整体改写。
- Industry Updates 保留在一级 Owner Living 区域，本页不混入短期新闻。
