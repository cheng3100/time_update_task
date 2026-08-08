# BTF / CO-RE / eBPF Dynamic Tracing

## High-value learning resources
### 1. Kernel BPF documentation
- **链接:** https://docs.kernel.org/bpf/index.html
- **是什么:** Linux eBPF verifier、program types、BTF 等官方入口。
- **价值点:** GPU KMD 动态 tracing/diagnostics 的核心技术基础。
- **学习重点:** tracing program types、BTF、verifier、ring buffer。
- **学习注意:** eBPF 能动态观察不代表应该暴露任意内部结构；优先稳定 tracepoint/BTF 边界。

### 2. BPF CO-RE Reference Guide
- **链接:** https://nakryiko.com/posts/bpf-core-reference-guide/
- **是什么:** 高质量 CO-RE/BTF 实战参考。
- **价值点:** 非常适合把内核版本差异与字段 relocation 讲清楚。
- **学习重点:** field existence/type matching、preserve_access_index、兼容模式。
- **学习注意:** 博客很实用，但最终行为仍以 kernel/libbpf 官方实现为准。
