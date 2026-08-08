# Device Visibility / Affinity / Namespace / Cgroup

## High-value learning resources
### 1. DRM Internals
- **链接:** https://docs.kernel.org/gpu/drm-internals.html
- **是什么:** DRM device node 与 per-file client model 的基础文档。
- **价值点:** 为 userspace visibility/permission/affinity 提供 Linux device model 基础。
- **学习重点:** render node、file private、open/close lifetime。
- **学习注意:** CUDA_VISIBLE_DEVICES 类逻辑主要在 userspace；KMD 应提供稳定 identity/capability/permission primitives。
