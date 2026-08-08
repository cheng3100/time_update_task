---
layout: default
title: GPU KMD Owner Direction
hero_title: GPU KMD Owner Direction
hero_subtitle_zh: 稳定 Owner 定义 + 独立 Owner 页面 + 长期资料 + 历次更新摘要。数据来自 Jekyll _data。
hero_subtitle_en: Stable Owner definitions + independent Owner pages + durable resources + update history, rendered from Jekyll data.
permalink: /kmd_owner_direction/
back_url: /
back_zh: 所有任务
back_en: All tasks
---

{% assign kmd = site.data.kmd_owner_direction %}

<nav class="nav-tabs">
  <a class="active" href="{{ '/kmd_owner_direction/' | relative_url }}"><span class="lang zh">首页</span><span class="lang en">Home</span></a>
  {% for owner in kmd.owners %}
  <a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}"><span class="lang zh">{{ owner.tab_zh }}</span><span class="lang en">{{ owner.tab_en }}</span></a>
  {% endfor %}
  <a href="{{ '/kmd_owner_direction/future.html' | relative_url }}"><span class="lang zh">公共未来 Topic</span><span class="lang en">Future Topic</span></a>
</nav>

<section class="owner-card">
  <h2 class="lang zh">Owner 大方向</h2><h2 class="lang en">Owner Map</h2>
  <p class="task-meta lang zh">每个一级 Owner 已恢复为独立页面；点击 Owner 名称进入该方向的 Stable Summary、当前切入、长期资料和 Industry Updates。</p>
  <p class="task-meta lang en">Each top-level Owner is again an independent page containing the stable summary, current entry, durable resources and Industry Updates.</p>
  <table>
    <thead><tr><th>Owner</th><th><span class="lang zh">当前切入</span><span class="lang en">Current entry</span></th></tr></thead>
    <tbody>{% for owner in kmd.owners %}<tr><td><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}">{{ owner.name }}</a></td><td><span class="lang zh">{{ owner.entry_zh }}</span><span class="lang en">{{ owner.entry_en }}</span></td></tr>{% endfor %}</tbody>
  </table>
</section>

<section class="owner-card">
  <h2 class="lang zh">任务内入口</h2><h2 class="lang en">Task Links</h2>
  <p><a href="{{ '/kmd_owner_direction/raw-updates.html' | relative_url }}"><span class="lang zh">原始更新输出归档</span><span class="lang en">Raw Update Archive</span></a> · <a href="{{ '/kmd_owner_direction/memory-roadmap.html' | relative_url }}"><span class="lang zh">Memory 详细路线</span><span class="lang en">Memory Detailed Roadmap</span></a> · <a href="{{ '/kmd_owner_direction/resources.html' | relative_url }}"><span class="lang zh">长期高价值资料总索引</span><span class="lang en">Durable Learning Resources</span></a></p>
</section>

<section class="owner-card">
  <h2 class="lang zh">本期知识结构</h2><h2 class="lang en">Knowledge Structure This Run</h2>
  <p class="lang zh">业界动态按一级 Owner 每期刷新；长期学习资料按 Owner → 稳定子方向累积。每个 Owner 页面同时呈现这两类内容，避免“新闻”和“长期学习资料”混为一体。</p>
  <p class="lang en">Industry updates refresh per top-level Owner, while durable learning resources accumulate by Owner → stable sub-direction. Each Owner page shows both without mixing news and long-lived learning material.</p>
</section>

<section class="owner-card">
  <h2 class="lang zh">历次更新摘要</h2><h2 class="lang en">Update History</h2>
  <p class="task-meta"><span class="lang zh">按时间从新到旧。当前：{{ kmd.current_run }}</span><span class="lang en">Newest first. Current: {{ kmd.current_run }}</span></p>
  {% for run in kmd.history %}
  {% assign raw_name = run.raw | split: '/' | last | replace: '.raw.md', '.html' %}
  {% assign curated_name = run.curated | split: '/' | last | replace: '.update.md', '.html' %}
  {% capture raw_page %}/kmd_owner_direction/raw_updates/{{ raw_name }}{% endcapture %}
  {% capture curated_page %}/kmd_owner_direction/updates/{{ curated_name }}{% endcapture %}
  <article class="history-item{% if run.latest %} latest{% endif %}">
    <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h3>
    <ul class="lang zh">{% for item in run.summary_zh %}<li>{{ item }}</li>{% endfor %}</ul>
    <ul class="lang en">{% for item in run.summary_en %}<li>{{ item }}</li>{% endfor %}</ul>
    <div class="history-links"><a href="{{ curated_page | relative_url }}"><span class="lang zh">结构化更新</span><span class="lang en">Curated update</span></a><a href="{{ raw_page | relative_url }}"><span class="lang zh">原始输出</span><span class="lang en">Raw output</span></a></div>
  </article>
  {% endfor %}
</section>
