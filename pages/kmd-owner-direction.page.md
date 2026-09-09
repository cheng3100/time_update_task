---
layout: default
title: GPU KMD Owner Direction
nav_order: 2
has_children: true
hero_title: GPU KMD Owner Direction
hero_subtitle_zh: 稳定 Owner 定义 + 架构导览 + 独立 Owner 页面 + 长期资料 + 历次更新摘要。
hero_subtitle_en: Stable Owner definitions + architecture guide + independent Owner pages + durable resources + update history.
permalink: /kmd_owner_direction/
---

{% assign kmd = site.data.kmd_owner_direction %}
{% assign stable = site.data.kmd_stable_directions %}
{% assign guides = site.data.kmd_owner_guides %}
{% assign recent_history = site.data.kmd_recent_history.runs %}
{% assign legacy_history = site.data.kmd_history.runs %}
{% assign living = site.data.kmd_living_latest %}

<section class="owner-card stable-definition-note">
  <h2 class="lang zh">先看全局：七个 Owner 在 GPU 软件栈中的位置</h2><h2 class="lang en">Start with the whole system: where the seven Owners fit</h2>
  <p class="lang zh">{{ guides.global.intro_zh }}</p><p class="lang en">{{ guides.global.intro_en }}</p>
  <div style="display:flex;flex-direction:column;gap:.45rem;margin:1rem 0;">
    {% for layer in guides.global.layers %}
    <div style="border:1px solid #d0d7de;border-radius:10px;padding:.85rem 1rem;background:rgba(127,127,127,.04);">
      <strong class="lang zh">{{ layer.title_zh }}</strong><strong class="lang en">{{ layer.title_en }}</strong>
      <div class="lang zh">{{ layer.desc_zh }}</div><div class="lang en">{{ layer.desc_en }}</div>
    </div>
    {% unless forloop.last %}<div style="text-align:center;font-size:1.3rem;opacity:.55;">↕</div>{% endunless %}
    {% endfor %}
  </div>
  <p class="task-meta lang zh">理解方式：七个 Owner 是“未来能力域”，不是七个源码目录。一个真实 feature 往往跨 Owner，例如 recoverable fault 由 Memory 主导，但会消费 Firmware generation、RAS recovery state 和 Observability trace。</p>
  <p class="task-meta lang en">Think of the seven Owners as future capability domains rather than source directories. A real feature may cross domains: recoverable faults are Memory-owned but consume Firmware generations, RAS recovery state and Observability traces.</p>
</section>

<section class="owner-card">
  <h2 class="lang zh">七个 Owner：先理解问题，再进入细节</h2><h2 class="lang en">Seven Owners: understand the problem before the details</h2>
  {% for owner in kmd.owners %}
  {% assign definition = stable.owners[owner.id] %}
  {% assign guide = guides.owners[owner.id] %}
  <article class="direction-overview">
    <h3><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}">{{ owner.name }}</a> <span class="badge">Stable</span></h3>
    <p class="lang zh">{{ guide.beginner_zh }}</p><p class="lang en">{{ guide.beginner_en }}</p>
    <p><strong><span class="lang zh">为什么需要：</span><span class="lang en">Why it exists: </span></strong><span class="lang zh">{{ guide.why_zh }}</span><span class="lang en">{{ guide.why_en }}</span></p>
    <p class="entry"><strong><span class="lang zh">当前切入：</span><span class="lang en">Current entry: </span></strong><span class="lang zh">{{ owner.entry_zh }}</span><span class="lang en">{{ owner.entry_en }}</span></p>
    <p><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}"><span class="lang zh">进入完整介绍、架构流、发展阶段、子方向和最新动态 →</span><span class="lang en">Open the full introduction, architecture flow, roadmap, sub-directions and latest updates →</span></a></p>
  </article>
  {% endfor %}
</section>

<section class="owner-card">
  <h2 class="lang zh">稳定方向定义</h2><h2 class="lang en">Stable Direction Definitions</h2>
  <p class="lang zh">{{ stable.policy.zh }}</p><p class="lang en">{{ stable.policy.en }}</p>
  <p class="task-meta lang zh">详细介绍、架构图和阶段路线同样属于 Stable Guide：不会因为每周出现新 patchset 自动变化。Living Industry Updates 仍单独刷新。</p>
  <p class="task-meta lang en">Detailed introductions, architecture flows and staged roadmaps are also Stable Guide content. They do not change automatically with weekly patchsets; Living Industry Updates remain separate.</p>
</section>

<section class="owner-card">
  <h2 class="lang zh">任务内入口</h2><h2 class="lang en">Task Links</h2>
  <p><a href="{{ '/kmd_owner_direction/raw-updates.html' | relative_url }}"><span class="lang zh">运行归档与原始输出状态</span><span class="lang en">Run Archive & Raw Provenance</span></a> · <a href="{{ '/kmd_owner_direction/memory-roadmap.html' | relative_url }}"><span class="lang zh">Memory 详细路线</span><span class="lang en">Memory Detailed Roadmap</span></a> · <a href="{{ '/kmd_owner_direction/resources.html' | relative_url }}"><span class="lang zh">长期高价值资料总索引</span><span class="lang en">Durable Learning Resources</span></a></p>
</section>

<section class="owner-card update-history">
  <h2 class="lang zh">历次更新摘要</h2><h2 class="lang en">Update History</h2>
  <p class="task-meta"><span class="lang zh">按时间从新到旧。Stable Guide 与每周 Living Update 分离；当前：{{ living.current_run }}</span><span class="lang en">Newest first. Stable Guides remain separate from weekly Living Updates. Current: {{ living.current_run }}</span></p>
  {% for run in recent_history %}
  <article class="history-item{% if run.latest %} latest{% endif %}">
    <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h3>
    <p class="history-intro lang zh">{{ run.intro_zh }}</p><p class="history-intro lang en">{{ run.intro_en }}</p>
    <div class="history-highlights">{% for item in run.highlights %}<section class="history-highlight"><h4>{% if item.url %}<a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{% endif %}<span class="lang zh">{{ item.title_zh }}</span><span class="lang en">{{ item.title_en }}</span>{% if item.url %}</a>{% endif %}</h4><p class="lang zh">{{ item.body_zh }}</p><p class="lang en">{{ item.body_en }}</p></section>{% endfor %}</div>
    <div class="history-links"><a href="{{ run.curated | relative_url }}"><span class="lang zh">查看完整结构化更新 →</span><span class="lang en">Full curated update →</span></a><a href="{{ run.raw | relative_url }}"><span class="lang zh">查看该期归档记录 →</span><span class="lang en">Open run archive record →</span></a></div>
  </article>
  {% endfor %}
  {% for run in legacy_history %}
  <article class="history-item"><h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span></h3><p class="history-intro lang zh">{{ run.intro_zh }}</p><p class="history-intro lang en">{{ run.intro_en }}</p><div class="history-highlights">{% for item in run.highlights %}<section class="history-highlight"><h4>{% if item.url %}<a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{% endif %}<span class="lang zh">{{ item.title_zh }}</span><span class="lang en">{{ item.title_en }}</span>{% if item.url %}</a>{% endif %}</h4><p class="lang zh">{{ item.body_zh }}</p><p class="lang en">{{ item.body_en }}</p></section>{% endfor %}</div><div class="history-links"><a href="{{ run.curated | relative_url }}"><span class="lang zh">查看完整结构化更新 →</span><span class="lang en">Full curated update →</span></a><a href="{{ run.raw | relative_url }}"><span class="lang zh">查看该期归档记录 →</span><span class="lang en">Open run archive record →</span></a></div></article>
  {% endfor %}
</section>
