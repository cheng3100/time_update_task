---
layout: default
title: GPU KMD Owner Direction
hero_title: GPU KMD Owner Direction
hero_subtitle_zh: 稳定 Owner 定义 + 一级 Owner 业界动态 + 历次更新摘要。数据来自 _data/kmd_owner_direction.yml。
hero_subtitle_en: Stable Owner definitions + Owner-level industry updates + update history. Data is sourced from _data/kmd_owner_direction.yml.
permalink: /kmd_owner_direction/
back_url: /
back_zh: 所有任务
back_en: All tasks
---

{% assign kmd = site.data.kmd_owner_direction %}

<nav class="nav-tabs">
  <a class="active" href="#home"><span class="lang zh">首页</span><span class="lang en">Home</span></a>
  {% for owner in kmd.owners %}
  <a href="#{{ owner.id }}"><span class="lang zh">{{ owner.tab_zh }}</span><span class="lang en">{{ owner.tab_en }}</span></a>
  {% endfor %}
</nav>

<section id="home">
  <div class="owner-card">
    <h2 class="lang zh">Owner 大方向</h2><h2 class="lang en">Owner Map</h2>
    <table>
      <thead><tr><th>Owner</th><th><span class="lang zh">当前切入</span><span class="lang en">Current entry</span></th></tr></thead>
      <tbody>{% for owner in kmd.owners %}<tr><td><a href="#{{ owner.id }}">{{ owner.name }}</a></td><td><span class="lang zh">{{ owner.entry_zh }}</span><span class="lang en">{{ owner.entry_en }}</span></td></tr>{% endfor %}</tbody>
    </table>
  </div>
  <div class="owner-card">
    <h2 class="lang zh">任务内入口</h2><h2 class="lang en">Task Links</h2>
    <p><a href="{{ '/kmd_owner_direction/raw-updates.html' | relative_url }}"><span class="lang zh">原始更新输出归档</span><span class="lang en">Raw Update Archive</span></a> · <a href="{{ '/kmd_owner_direction/memory-roadmap.html' | relative_url }}"><span class="lang zh">Memory 详细路线</span><span class="lang en">Memory Detailed Roadmap</span></a> · <a href="{{ '/kmd_owner_direction/resources.html' | relative_url }}"><span class="lang zh">长期资料库</span><span class="lang en">Learning Resources</span></a></p>
  </div>
  <div class="owner-card">
    <h2 class="lang zh">历次更新摘要</h2><h2 class="lang en">Update History</h2>
    <p class="task-meta"><span class="lang zh">按时间从新到旧。当前：{{ kmd.current_run }}</span><span class="lang en">Newest first. Current: {{ kmd.current_run }}</span></p>
    {% for run in kmd.history %}
    <article class="history-item{% if run.latest %} latest{% endif %}">
      <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h3>
      <ul class="lang zh">{% for item in run.summary_zh %}<li>{{ item }}</li>{% endfor %}</ul>
      <ul class="lang en">{% for item in run.summary_en %}<li>{{ item }}</li>{% endfor %}</ul>
      <div class="history-links"><a href="{{ run.curated }}"><span class="lang zh">结构化更新</span><span class="lang en">Curated update</span></a><a href="{{ run.raw }}"><span class="lang zh">原始输出</span><span class="lang en">Raw output</span></a></div>
    </article>
    {% endfor %}
  </div>
</section>

{% for owner in kmd.owners %}
<section id="{{ owner.id }}" class="owner-card">
  <h2>{{ owner.name }} <span class="badge">Stable</span></h2>
  <p class="lang zh">{{ owner.summary_zh }}</p><p class="lang en">{{ owner.summary_en }}</p>
  <h3 class="lang zh">子方向</h3><h3 class="lang en">Sub-directions</h3>
  <ul>{% for topic in owner.topics %}<li>{{ topic }}</li>{% endfor %}</ul>
  <p class="entry"><strong><span class="lang zh">当前切入：</span><span class="lang en">Current entry: </span></strong><span class="lang zh">{{ owner.entry_zh }}</span><span class="lang en">{{ owner.entry_en }}</span></p>
  <h3 class="lang zh">本期业界最新动态</h3><h3 class="lang en">Industry Updates — This Run</h3>
  {% for update in owner.updates %}
  <div class="history-item">
    <strong><a href="{{ update.url }}"><span class="lang zh">{{ update.title_zh }}</span><span class="lang en">{{ update.title_en }}</span></a></strong>
    <p><strong><span class="lang zh">KMD 影响：</span><span class="lang en">KMD impact: </span></strong><span class="lang zh">{{ update.impact_zh }}</span><span class="lang en">{{ update.impact_en }}</span></p>
    <p class="task-meta"><strong><span class="lang zh">优先级：</span><span class="lang en">Priority: </span></strong><span class="lang zh">{{ update.priority_zh }}</span><span class="lang en">{{ update.priority_en }}</span></p>
  </div>
  {% endfor %}
</section>
{% endfor %}
