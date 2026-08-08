# Versioned Firmware ABI / Command & Event Namespace

## High-value learning resources

### 1. Nova Core Guidelines
- **类型:** Canonical / upstream architecture rule
- **链接:** https://docs.kernel.org/next/gpu/nova/core/guidelines.html
- **是什么:** Nova 对 firmware-version-independent core API 的架构规则。
- **价值点:** 最直接支持“FW version translation 应集中在 lower layer”的设计原则。
- **学习重点:** second-level driver 不应看到 version-specific FW structures/semantics。
- **学习注意:** 不要照搬 Nova API；应抽象适合自研 GPU 的 version/capability contract。

### 2. Hector Zelaya — Nova: A NVIDIA Driver Written in Rust for the Linux Kernel, Part 1
- **类型:** Deep explanation / source-architecture walkthrough
- **链接:** https://hectorzelaya.dev/posts/nova-driver/part1-architecture-initialization-hardware-discovery/
- **是什么:** 2026 年基于 upstream Nova 源码写成的长篇架构导读，解释 nova-core/nova-drm 两层结构、PCI 初始化、BAR、硬件发现、resource lifetime 和 GSP-centric driver model。
- **价值点:** 官方 guidelines 很精炼，这篇文章能把“为什么 lower HW/FW control layer 与 upper DRM/VFIO client 要解耦”放到完整初始化和资源生命周期中理解，适合作为阅读 Nova 源码/patch 前的入口。
- **学习重点:** nova-core vs nova-drm boundary、auxiliary bus、多 consumer 设计、GSP firmware-centric architecture、resource ownership/lifetime，以及 Rust 如何表达 driver cleanup/lifetime。
- **学习注意:** Nova 仍高速演进，文章也明确提示 API 是 snapshot；学习其 architectural reasoning 和 source-reading method，不把具体 Rust API 当固定范式。

## Maintenance notes
本页稳定增长；Industry Updates 不放在这里。
