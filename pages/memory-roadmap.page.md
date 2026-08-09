---
layout: default
title: GPU Memory Owner Roadmap
hero_title: GPU Memory / Virtual Memory / Unified Memory
hero_subtitle_zh: "Memory Owner 的长期纵深路线：切入 → 深化 → 拓展 → 演进。"
hero_subtitle_en: "Long-term Memory Owner depth path: Entry → Deepen → Expand → Evolve."
permalink: /kmd_owner_direction/memory-roadmap.html
back_url: /kmd_owner_direction/owners/memory.html
back_zh: Memory Owner
back_en: Memory Owner
---

{% assign roadmap = site.data.memory_roadmap %}
{% for stage in roadmap.stages %}
<section class="owner-card">
  <h2 class="lang zh">{{ stage.title_zh }}</h2>
  <h2 class="lang en">{{ stage.title_en }}</h2>
  <p><strong><span class="lang zh">阶段目标：</span><span class="lang en">Goal: </span></strong><span class="lang zh">{{ stage.goal_zh }}</span><span class="lang en">{{ stage.goal_en }}</span></p>
  <ul>{% for item in stage.items %}<li>{{ item }}</li>{% endfor %}</ul>
  <p class="entry"><strong><span class="lang zh">阶段交付：</span><span class="lang en">Deliverable: </span></strong><span class="lang zh">{{ stage.deliverable_zh }}</span><span class="lang en">{{ stage.deliverable_en }}</span></p>
  <p><strong><span class="lang zh">Owner 能力形成：</span><span class="lang en">Owner capability: </span></strong><span class="lang zh">{{ stage.capability_zh }}</span><span class="lang en">{{ stage.capability_en }}</span></p>
</section>
{% endfor %}
<section class="owner-card">
  <h2 class="lang zh">推荐推进顺序</h2><h2 class="lang en">Recommended Progression</h2>
  <p><code>{{ roadmap.sequence }}</code></p>
  <blockquote><span class="lang zh">{{ roadmap.principle_zh }}</span><span class="lang en">{{ roadmap.principle_en }}</span></blockquote>
</section>
<p><a href="https://github.com/cheng3100/time_update_task/blob/main/kmd_owner_direction/owners/memory.archive.md"><span class="lang zh">查看完整 Memory owner Markdown →</span><span class="lang en">Open complete Memory owner Markdown →</span></a></p>
