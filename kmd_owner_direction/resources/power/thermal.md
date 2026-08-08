# Thermal Throttling / Power Cap

## High-value learning resources
### 1. AMDGPU documentation
- **链接:** https://docs.kernel.org/gpu/amdgpu/index.html
- **是什么:** AMDGPU power/SMU/thermal/telemetry 的官方入口文档。
- **价值点:** 提供成熟产品 GPU power/thermal 管理的参考实现入口。
- **学习重点:** 沿 SMU、powerplay、hwmon/metrics 章节继续深入源码。
- **学习注意:** AMDGPU 体系复杂，先画清 host KMD↔SMU firmware↔sensor/clock 控制链再读细节。
