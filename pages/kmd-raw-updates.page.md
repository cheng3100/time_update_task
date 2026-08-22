---
layout: default
title: Raw Update Archive
parent: GPU KMD Owner Direction
nav_order: 10
permalink: /kmd_owner_direction/raw-updates.html
---

{% assign provenance = site.data.kmd_raw_provenance %}
{% assign recent = site.data.kmd_recent_history.runs %}

<p class="lang zh">这里区分 <strong>Verified Raw</strong>、<strong>未验证历史 raw</strong> 与 <strong>恢复/重构版</strong>。只有确认与聊天窗口报告一致的内容才称为原始输出。</p>
<p class="lang en">This archive distinguishes Verified Raw, unverified historical raw, and recovered/reconstructed records. Only content verified against the chat report is labelled original raw.</p>

{% for run in recent %}
{% assign raw_stem = run.raw | split: '/' | last | replace: '.html', '' | replace: '.raw.md', '' %}
{% assign prov = provenance[raw_stem] %}
<article class="history-item{% if run.latest %} latest{% endif %}">
  <h2>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h2>
  <p class="lang zh">{{ run.intro_zh }}</p><p class="lang en">{{ run.intro_en }}</p>
  {% if prov %}
  <p><strong><span class="lang zh">归档状态：</span><span class="lang en">Archive status: </span></strong><span class="lang zh">{{ prov.label_zh }}</span><span class="lang en">{{ prov.label_en }}</span></p>
  <p class="task-meta lang zh">{{ prov.detail_zh }}</p><p class="task-meta lang en">{{ prov.detail_en }}</p>
  {% endif %}
  <p><a href="{{ run.raw | relative_url }}"><span class="lang zh">打开该期归档记录 →</span><span class="lang en">Open this run archive record →</span></a></p>
</article>
{% endfor %}

{% assign kmd = site.data.kmd_owner_direction %}
{% for run in kmd.history %}
{% assign raw_name = run.raw | split: '/' | last | replace: '.raw.md', '.html' %}
{% assign raw_stem = run.raw | split: '/' | last | replace: '.raw.md', '' %}
{% assign prov = provenance[raw_stem] %}
{% capture raw_page %}/kmd_owner_direction/raw_updates/{{ raw_name }}{% endcapture %}
<article class="history-item">
  <h2>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span></h2>
  {% if prov %}
  <p><strong><span class="lang zh">归档状态：</span><span class="lang en">Archive status: </span></strong><span class="lang zh">{{ prov.label_zh }}</span><span class="lang en">{{ prov.label_en }}</span></p>
  <p class="task-meta lang zh">{{ prov.detail_zh }}</p><p class="task-meta lang en">{{ prov.detail_en }}</p>
  {% endif %}
  <p><a href="{{ raw_page | relative_url }}"><span class="lang zh">打开该期归档记录 →</span><span class="lang en">Open this run archive record →</span></a></p>
</article>
{% endfor %}
