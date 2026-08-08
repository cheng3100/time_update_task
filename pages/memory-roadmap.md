---
layout: default
title: GPU Memory Owner Roadmap
hero_title: GPU Memory / Virtual Memory / Unified Memory
hero_subtitle_zh: Memory Owner 的长期纵深路线：切入 → 深化 → 拓展 → 演进。
hero_subtitle_en: Long-term Memory Owner depth path: Entry → Deepen → Expand → Evolve.
permalink: /kmd_owner_direction/memory-roadmap.html
back_url: /kmd_owner_direction/
back_zh: GPU KMD Owner Direction
back_en: GPU KMD Owner Direction
---

{% assign kmd = site.data.kmd_owner_direction %}
{% for stage in kmd.memory_stages %}
<section class="owner-card">
  <h2 class="lang zh">{{ stage.title_zh }}</h2>
  <h2 class="lang en">{{ stage.title_en }}</h2>
  <p class="lang zh">{{ stage.body_zh }}</p>
  <p class="lang en">{{ stage.body_en }}</p>
</section>
{% endfor %}

<p><a href="https://github.com/cheng3100/time_update_task/blob/main/kmd_owner_direction/owners/memory.md"><span class="lang zh">查看完整 Memory owner Markdown →</span><span class="lang en">Open complete Memory owner Markdown →</span></a></p>
