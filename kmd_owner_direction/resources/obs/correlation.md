# PID / PASID / VM / Context / Queue / Job Correlation

## High-value learning resources
### 1. DRM Internals
- **链接:** https://docs.kernel.org/gpu/drm-internals.html
- **是什么:** DRM device/file/client/object lifetime 的官方基础文档。
- **价值点:** 为定义跨层稳定 GPU object identity 提供 Linux-facing 对象模型。
- **学习重点:** `drm_file`/client 与 device object lifetime。
- **学习注意:** KMD 私有 context/queue/job 仍需自己定义稳定 ID，不能直接暴露内核指针。
