# Multi-GPU Enumeration / Stable Physical & Logical Identity

## High-value learning resources
### 1. DRM Internals
- **链接:** https://docs.kernel.org/gpu/drm-internals.html
- **是什么:** Linux DRM device/minor/file/client 基础对象模型文档。
- **价值点:** 帮助定义 BDF、DRM minor、logical GPU index 与 per-process client 的稳定关系。
- **学习重点:** `drm_device`、minor、file/client lifetime。
- **学习注意:** logical index 不应等同于 BDF；容器/可见性可能重排用户看到的编号。
