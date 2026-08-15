# Heartbeat / Watchdog / Hang Detection

## High-value learning resources
### 1. Xe Device Coredump
- **链接:** https://docs.kernel.org/gpu/xe/xe_devcoredump.html
- **是什么:** Intel Xe GPU hang 时的诊断与恢复入口文档。
- **价值点:** 能反推 hang detection 后必须马上保存哪些状态以及 reset serialization。
- **学习重点:** first-error、capture timing、reset flow、hang state lifetime。
- **学习注意:** watchdog 应与 progress semantics 对齐，不能只依赖固定 wall-clock timeout。

### 2. Intel Xe GPU Health Indicator / Device Wedging
- **类型:** Canonical / management-interface case study
- **链接:** https://docs.kernel.org/next/gpu/xe/xe_device.html
- **是什么:** Xe 将 GPU 内部故障状态通过 `gpu_health` sysfs 和 DRM wedged uevent 暴露给管理工具，并定义 `ok / warning / critical` 以及 rebind/bus-reset、firmware-flash 等恢复路径。
- **价值点:** 展示 RAS 不应止于“driver 能 reset”；生产级 KMD 还需要一个稳定的 device-health contract，让监控、运维、fwupd/管理服务知道 GPU 是否可用、需要哪种恢复动作。
- **学习重点:** health state 与底层 fault evidence 的解耦、wedged state、recovery-method hint、userspace/admin responsibility，以及“诊断结果如何转成可消费 health state”。
- **学习注意:** health flag 不能替代真实 heartbeat/ECC/hang counters，也不能把复杂 recovery policy 全塞进 sysfs；更合理的是底层证据→RAS policy→health state/uevent 的分层。
