---
layout: default
title: Memory Detailed Roadmap
parent: GPU KMD Owner Direction
nav_order: 8
permalink: /kmd_owner_direction/memory-roadmap.html
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
