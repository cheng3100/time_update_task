---
layout: default
title: GPU KMD Owner Direction
hero_title: GPU KMD Owner Direction
hero_subtitle_zh: 稳定 Owner 定义 + 独立 Owner 页面 + 长期资料 + 历次更新摘要。方向定义默认稳定，Living 内容按期更新。
hero_subtitle_en: Stable Owner definitions + independent Owner pages + durable resources + update history. Direction definitions stay stable while Living content refreshes per run.
permalink: /kmd_owner_direction/
back_url: /
back_zh: 所有任务
back_en: All tasks
---

{% assign kmd = site.data.kmd_owner_direction %}
{% assign stable = site.data.kmd_stable_directions %}
{% assign recent_history = site.data.kmd_recent_history.runs %}
{% assign legacy_history = site.data.kmd_history.runs %}
{% assign living = site.data.kmd_living_latest %}

{% include kmd-nav.html active='home' %}

<section class="owner-card stable-definition-note">
  <h2 class="lang zh">稳定方向定义</h2><h2 class="lang en">Stable Direction Definitions</h2>
  <p class="lang zh">{{ stable.policy.zh }}</p>
  <p class="lang en">{{ stable.policy.en }}</p>
</section>

<section class="owner-card">
  <h2 class="lang zh">Owner 大方向与子方向</h2><h2 class="lang en">Owner Map & Sub-directions</h2>
  <p class="task-meta lang zh">这里展示长期稳定的职责定义，而不是本期新闻摘要。当前切入 Feature、Industry Updates 和资料新增会随定期任务变化，但下面的 Owner/子方向含义默认保持不变。</p>
  <p class="task-meta lang en">This section shows long-lived responsibility definitions rather than this run's news. Entry features, Industry Updates, and new resources may change, while the Owner/sub-direction meanings below remain stable by default.</p>

  {% for owner in kmd.owners %}
  {% assign definition = stable.owners[owner.id] %}
  <article class="direction-overview">
    <h3><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}">{{ owner.name }}</a> <span class="badge">Stable</span></h3>
    <p class="lang zh">{{ definition.description_zh }}</p>
    <p class="lang en">{{ definition.description_en }}</p>
    <p class="entry"><strong><span class="lang zh">当前切入：</span><span class="lang en">Current entry: </span></strong><span class="lang zh">{{ owner.entry_zh }}</span><span class="lang en">{{ owner.entry_en }}</span></p>

    <h4 class="lang zh">稳定子方向</h4><h4 class="lang en">Stable Sub-directions</h4>
    <ul class="subdirection-summary-list">
      {% for sub in definition.subdirections %}
      <li><strong>{{ sub.title }}</strong><span class="lang zh"> — {{ sub.short_zh }}</span><span class="lang en"> — {{ sub.short_en }}</span></li>
      {% endfor %}
    </ul>
    <p><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}"><span class="lang zh">进入该 Owner 的完整方向定义、边界与长期资料 →</span><span class="lang en">Open full Owner definition, boundaries, and durable resources →</span></a></p>
  </article>
  {% endfor %}
</section>

<section class="owner-card">
  <h2 class="lang zh">任务内入口</h2><h2 class="lang en">Task Links</h2>
  <p><a href="{{ '/kmd_owner_direction/raw-updates.html' | relative_url }}"><span class="lang zh">原始更新输出归档</span><span class="lang en">Raw Update Archive</span></a> · <a href="{{ '/kmd_owner_direction/memory-roadmap.html' | relative_url }}"><span class="lang zh">Memory 详细路线</span><span class="lang en">Memory Detailed Roadmap</span></a> · <a href="{{ '/kmd_owner_direction/resources.html' | relative_url }}"><span class="lang zh">长期高价值资料总索引</span><span class="lang en">Durable Learning Resources</span></a></p>
</section>

<section class="owner-card">
  <h2 class="lang zh">Living 内容如何更新</h2><h2 class="lang en">How Living Content Updates</h2>
  <p class="lang zh">稳定方向定义与 Living 内容分离：上面的 Owner / 子方向职责默认不变；当前切入 Feature、业界动态、长期资料新增、每期摘要按任务运行持续更新。</p>
  <p class="lang en">Stable direction definitions are separated from Living content: Owner/sub-direction responsibilities above remain stable, while entry features, Industry Updates, resource additions, and run summaries refresh with the scheduled task.</p>
</section>

<section class="owner-card update-history">
  <h2 class="lang zh">历次更新摘要</h2><h2 class="lang en">Update History</h2>
  <p class="task-meta"><span class="lang zh">按时间从新到旧。每一期直接保留关键技术结论、资料引用与深入主题；完整上下文仍可进入结构化更新或原始输出。当前：{{ living.current_run }}</span><span class="lang en">Newest first. Each run keeps key technical conclusions, references and deep-dive topics here. Current: {{ living.current_run }}</span></p>

  {% for run in recent_history %}
  <article class="history-item{% if run.latest %} latest{% endif %}">
    <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h3>
    <p class="history-intro lang zh">{{ run.intro_zh }}</p><p class="history-intro lang en">{{ run.intro_en }}</p>
    <div class="history-highlights">
      {% for item in run.highlights %}
      <section class="history-highlight">
        <h4>{% if item.url %}<a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{% endif %}<span class="lang zh">{{ item.title_zh }}</span><span class="lang en">{{ item.title_en }}</span>{% if item.url %}</a>{% endif %}</h4>
        <p class="lang zh">{{ item.body_zh }}</p><p class="lang en">{{ item.body_en }}</p>
      </section>
      {% endfor %}
    </div>
    <div class="history-links"><a href="{{ run.curated | relative_url }}"><span class="lang zh">查看完整结构化更新 →</span><span class="lang en">Full curated update →</span></a><a href="{{ run.raw | relative_url }}"><span class="lang zh">查看完整原始输出 →</span><span class="lang en">Full raw output →</span></a></div>
  </article>
  {% endfor %}

  {% for run in legacy_history %}
  <article class="history-item">
    <h3>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span></h3>
    <p class="history-intro lang zh">{{ run.intro_zh }}</p><p class="history-intro lang en">{{ run.intro_en }}</p>
    <div class="history-highlights">
      {% for item in run.highlights %}
      <section class="history-highlight"><h4>{% if item.url %}<a href="{% if item.url contains '://' %}{{ item.url }}{% else %}{{ item.url | relative_url }}{% endif %}">{% endif %}<span class="lang zh">{{ item.title_zh }}</span><span class="lang en">{{ item.title_en }}</span>{% if item.url %}</a>{% endif %}</h4><p class="lang zh">{{ item.body_zh }}</p><p class="lang en">{{ item.body_en }}</p></section>
      {% endfor %}
    </div>
    <div class="history-links"><a href="{{ run.curated | relative_url }}"><span class="lang zh">查看完整结构化更新 →</span><span class="lang en">Full curated update →</span></a><a href="{{ run.raw | relative_url }}"><span class="lang zh">查看完整原始输出 →</span><span class="lang en">Full raw output →</span></a></div>
  </article>
  {% endfor %}
</section>
