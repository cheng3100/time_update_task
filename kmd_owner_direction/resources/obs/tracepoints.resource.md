# Stable KMD Tracepoint / Event Model

## High-value learning resources

### 1. Linux Tracepoints
- **类型:** Canonical / official
- **链接:** https://docs.kernel.org/trace/tracepoints.html
- **是什么:** Linux kernel 静态 tracepoint 设计与使用官方文档。
- **价值点:** 建立低开销、稳定事件 schema 的基础。
- **学习重点:** tracepoint definition、probe lifetime、ABI 稳定性考虑。
- **学习注意:** 不要把内部 debug print 直接升级成长期 tracepoint；先定义对象 ID 与事件语义。

### 2. Brendan Gregg — Linux eBPF Tracing Tools
- **类型:** Deep explanation / practical observability guide
- **链接:** https://www.brendangregg.com/ebpf.html
- **是什么:** Brendan Gregg 对 BCC、bpftrace、kprobe/tracepoint/profiling 等 Linux eBPF tracing 工具和使用模型的长期入口页。
- **价值点:** 官方 BPF 文档偏机制，这个页面更适合建立“遇到一个真实 latency/hang/调用链问题时该怎么选 hook、怎么收集 timestamp、怎么做 histogram/stack correlation”的实战直觉。
- **学习重点:** static vs dynamic tracing、BCC vs bpftrace、kprobe/tracepoint、latency measurement、stack/profile、低开销聚合。
- **学习注意:** GPU KMD 最终仍应优先提供稳定 tracepoint/object schema；kprobe/fentry 很适合探索阶段，但不应被当成稳定产品接口。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
