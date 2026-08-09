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
{% assign history = site.data.kmd_history.runs %}

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

<section class="owner-card update-history">
  <h2 class="lang zh">历次更新摘要</h2><h2 class="lang en">Update History</h2>
  <p class="task-meta"><span class="lang zh">按时间从新到旧。每一期直接保留关键技术结论、资料引用与深入主题；完整上下文仍可进入结构化更新或原始输出。当前：{{ kmd.current_run }}</span><span class="lang en">Newest first. Each run keeps its key technical conclusions, references and deep-dive topics here; full context remains available through the curated and raw reports. Current: {{ kmd.current_run }}</span></p>

  {% for run in history %}
  <article class="history-item{% if run.latest %} latest{% endif %}">
    <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h3>
    <p class="history-intro lang zh">{{ run.intro_zh }}</p>
    <p class="history-intro lang en">{{ run.intro_en }}</p>

    <div class="history-highlights">
      {% for item in run.highlights %}
      <section class="history-highlight">
        <h4>{% if item.url %}<a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{% endif %}<span class="lang zh">{{ item.title_zh }}</span><span class="lang en">{{ item.title_en }}</span>{% if item.url %}</a>{% endif %}</h4>
        <p class="lang zh">{{ item.body_zh }}</p>
        <p class="lang en">{{ item.body_en }}</p>
      </section>
      {% endfor %}
    </div>

    <div class="history-links">
      <a href="{{ run.curated | relative_url }}"><span class="lang zh">查看完整结构化更新 →</span><span class="lang en">Full curated update →</span></a>
      <a href="{{ run.raw | relative_url }}"><span class="lang zh">查看完整原始输出 →</span><span class="lang en">Full raw output →</span></a>
    </div>
  </article>
  {% endfor %}
</section>
