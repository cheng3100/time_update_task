---
layout: default
title: GPU KMD Raw Update Archive
hero_title: Raw Update Archive
hero_subtitle_zh: GPU KMD Owner 定时任务的完整原始输出历史；append-only。
hero_subtitle_en: Complete append-only output history for the GPU KMD Owner scheduled task.
permalink: /kmd_owner_direction/raw-updates.html
back_url: /kmd_owner_direction/
back_zh: GPU KMD Owner Direction
back_en: GPU KMD Owner Direction
---

{% assign kmd = site.data.kmd_owner_direction %}
{% for run in kmd.history %}
<article class="history-item{% if run.latest %} latest{% endif %}">
  <h2>{{ run.date }} · <span class="lang zh">{{ run.title_zh }}</span><span class="lang en">{{ run.title_en }}</span></h2>
  <p><a href="{{ run.raw }}"><span class="lang zh">打开完整原始输出 →</span><span class="lang en">Open complete raw output →</span></a></p>
</article>
{% endfor %}
