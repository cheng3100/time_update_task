---
layout: default
title: "Other Topic Timeline"
parent: "Other Topic"
nav_order: 1
permalink: "/kmd_owner_direction/other-topic/timeline/"
---

# Other Topic Timeline

每个时间节点标题都链接到对应的 Web Update Archive 原始记录。

## [2026-11-07 · Weekly #13]({{ '/kmd_owner_direction/web-update-archive/2026-11-07-weekly-13/' | relative_url }})

### RAS / Recovery — [GFX11 engine-level soft reset v4](https://www.mail-archive.com/amd-gfx%40lists.freedesktop.org/msg154928.html)

AMDGPU recovery 继续从 full-device reset 向 queue/engine scoped recovery 演进，并引入更明确的 state preservation 与 escalation 路径。

### Power / Performance — [restore forced performance level after reset v4](https://mid.mail-archive.com/amd-gfx%40lists.freedesktop.org/msg154866.html)

PMFW reset 后 software cached policy 与真实 hardware-applied state 可能分叉；修复路径改为在 reset/recovery 后重新 apply retained performance level。

### Observability / Profiling — [SPM VMID state around GFXOFF](https://mail-archive.com/search?f=1&l=amd-gfx%40lists.freedesktop.org&o=newest&q=date%3A20261106)

SPM VMID configuration 不能假设在 GFXOFF 生命周期中永久保留，需要在合适 execution path 重新同步硬件状态。
