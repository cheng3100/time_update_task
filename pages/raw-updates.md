---
layout: default
title: Raw Update Archive
hero_title: Raw Update Archive
hero_subtitle_zh: 所有定时任务的完整原始输出归档，按任务主题分组。
hero_subtitle_en: Complete raw outputs for all scheduled tasks, grouped by task topic.
permalink: /raw-updates.html
back_url: /
back_zh: 所有任务
back_en: All tasks
---

{% for task in site.data.tasks.tasks %}
<section class="archive-group">
  <h2><span class="lang zh">{{ task.title_zh }}</span><span class="lang en">{{ task.title_en }}</span></h2>
  <p><a href="{{ task.raw_archive_url | relative_url }}"><span class="lang zh">打开该任务原始更新归档 →</span><span class="lang en">Open this task's raw archive →</span></a></p>
</section>
{% endfor %}
