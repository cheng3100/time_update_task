---
layout: default
title: Raw Update Archive
parent: GPU KMD Owner Direction
nav_order: 10
permalink: /kmd_owner_direction/raw-updates.html
---

{% assign recent = site.data.kmd_recent_history.runs %}
{% for run in recent %}
<article class="history-item{% if run.latest %} latest{% endif %}">
  <h2>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span>{% if run.latest %} <span class="badge"><span class="lang zh">最新</span><span class="lang en">Latest</span></span>{% endif %}</h2>
  <p class="lang zh">{{ run.intro_zh }}</p><p class="lang en">{{ run.intro_en }}</p>
  <p><a href="{{ run.raw | relative_url }}"><span class="lang zh">打开完整原始输出 →</span><span class="lang en">Open complete raw output →</span></a></p>
</article>
{% endfor %}

{% assign kmd = site.data.kmd_owner_direction %}
{% for run in kmd.history %}
{% assign raw_name = run.raw | split: '/' | last | replace: '.raw.md', '.html' %}
{% capture raw_page %}/kmd_owner_direction/raw_updates/{{ raw_name }}{% endcapture %}
<article class="history-item">
  <h2>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span></h2>
  <p><a href="{{ raw_page | relative_url }}"><span class="lang zh">打开完整原始输出 →</span><span class="lang en">Open complete raw output →</span></a></p>
</article>
{% endfor %}
