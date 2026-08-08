# Job Abort / Queue Kill / Context Kill / Engine Reset

## High-value learning resources
### 1. AMDGPU documentation
- **链接:** https://docs.kernel.org/gpu/amdgpu/index.html
- **是什么:** AMDGPU reset/recovery 相关章节和源码索引入口。
- **价值点:** 帮助建立从局部错误到 engine/full GPU reset 的分级恢复思路。
- **学习重点:** reset domain、scheduler recovery、VM/context restore。
- **学习注意:** 具体 reset granularity 受硬件约束，先建立 recovery decision ladder 再实现。
