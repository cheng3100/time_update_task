# Stable KMD Tracepoint / Event Model

## High-value learning resources
### 1. Linux Tracepoints
- **链接:** https://docs.kernel.org/trace/tracepoints.html
- **是什么:** Linux kernel 静态 tracepoint 设计与使用官方文档。
- **价值点:** 建立低开销、稳定事件 schema 的基础。
- **学习重点:** tracepoint definition、probe lifetime、ABI 稳定性考虑。
- **学习注意:** 不要把内部 debug print 直接升级成长期 tracepoint；先定义对象 ID 与事件语义。
