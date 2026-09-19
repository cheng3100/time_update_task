# Shared-memory / Ring / Mailbox Transport

## High-value learning resources
### 1. Nouveau / GSP documentation
- **链接:** https://docs.kernel.org/gpu/nouveau.html
- **是什么:** Nouveau/NVIDIA GSP command/status queue 与 firmware communication 的官方入口。
- **价值点:** 为 GPU firmware ring/mailbox/shared-memory control path 提供成熟案例。
- **学习重点:** command queue、status/event queue、doorbell/notification 语义。
- **学习注意:** transport 只是承载层；message ABI/version/error semantics 应与 transport 解耦。

### 2. Tyr `MappedBo` — FW shared section 的 CPU/GPU mapping lifetime（Implementation / Practice）
- **链接:** https://lkml.iu.edu/2609.1/18699.html
- **是什么:** Tyr Rust GPU driver 为 firmware section 引入 `MappedBo`，把 KernelBo 与 persistent CPU vmap 绑定在同一个对象 lifetime 中；shared section 因此可以同时拥有稳定 GPU mapping 和 CPU access。
- **价值点:** 展示 firmware shared-memory 不应由多个模块分别保存裸 CPU pointer、GPU VA 和 BO lifetime；一个同时拥有双侧 mapping 的对象也是执行 firmware-reported MCU address bounds validation 的自然位置。
- **学习重点:** persistent vmap lifetime、KernelBo ownership、CPU/GPU mapping 同寿命、FW-reported VA 到 validated shared-section view 的转换、错误路径 cleanup。
- **学习注意:** Tyr/CSF 的 BO 与 MCU VA 模型不能机械复制到 R82/MHU；应提取 ownership/bounds-validation pattern，并结合自研平台的 cache/coherency、doorbell/ringbuffer 和 reset generation 重新设计。
