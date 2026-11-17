---
layout: default
title: "2026-11-07 · TLB invalidation completion 与 BO lifetime"
parent: "Focus"
ancestor: "GPU Memory / Virtual Memory / Unified Memory"
nav_order: 1
permalink: "/kmd_owner_direction/memory/focus/2026-11-07-tlb-bo-lifetime/"
---

# L4 — TLB invalidation completion 为什么属于 BO lifetime

> 此页面先按已确认的 Key Topic Detail 模板建立 Focus 节点。后续叶子节点格式 review 将继续调整。

## 0. 问题背景

GPU page-table mapping 已删除，并不意味着对应 BO / physical backing memory 已经可以安全释放。如果此前的 TLB invalidation 尚未完成，运行中的 user queue 仍可能通过 stale translation 访问旧 PA。

- https://mail-archive.com/amd-gfx%40lists.freedesktop.org/msg155047.html
- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_gem.c
- https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vm.c

```text
PTE invalidation
      ≠
TLB invalidation completion
      ≠
old access disappearance
      ≠
physical memory reusable
```

完整已审阅 B1 模板：`kmd_owner_direction/sample/web_output/key_topic_detail_demo.md`。
