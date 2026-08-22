---
layout: default
title: Linux GPU / Accelerator Kernel Ecosystem
hero_title: Linux GPU / Accelerator Kernel Ecosystem
hero_subtitle_zh: 公共未来演进 Topic，不分配独立 Owner；跟踪未来 1–3 年可能改变 KMD 架构的 upstream 机制。
hero_subtitle_en: Shared future-evolution topic, not an Owner; tracks upstream mechanisms that may change KMD architecture over 1–3 years.
permalink: /kmd_owner_direction/future.html
back_url: /kmd_owner_direction/
back_zh: GPU KMD Owner 主页
back_en: GPU KMD Owner Home
---

{% include kmd-nav.html active='future' %}

<section class="owner-card">
<h2 class="lang zh">长期跟踪范围</h2><h2 class="lang en">Long-term watch scope</h2>
<ul>
<li>DRM GPU SVM / drm_pagemap / shared VA</li>
<li>DRM / Accel common infrastructure</li>
<li>drm_gpuvm / drm_exec / drm_sched / VM_BIND</li>
<li>dma-buf / dma-fence / syncobj / compute uAPI</li>
<li>device node / namespace / cgroup / resource control</li>
<li>firmware-centric / hardware-scheduler architecture</li>
<li>common recovery / telemetry / security / virtualization framework</li>
<li>Rust GPU drivers, Nova/Nouveau and upstream ABI policy</li>
<li>Linux MM / IOMMU / PCIe / CXL / eBPF changes affecting GPU KMD</li>
</ul>
</section>

<section class="owner-card">
<h2 class="lang zh">当前判断</h2><h2 class="lang en">Current judgement</h2>
<p class="lang zh">当前没有必要增加第 8 个 Owner。GPU SVM、Nova firmware-centric layering、Xe SR-IOV lifecycle、gpu_ext/fabric_ext 等更适合作为现有 Owner 的演进信号与公共架构雷达。</p>
<p class="lang en">No eighth Owner is needed now. GPU SVM, Nova firmware-centric layering, Xe SR-IOV lifecycle and gpu_ext/fabric_ext are better treated as evolution signals for existing Owners and the shared architecture radar.</p>
</section>
