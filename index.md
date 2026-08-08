---
layout: default
title: Time Update Tasks
hero_title: Time Update Tasks
hero_subtitle_zh: 所有定时更新任务的长期归档与 GitHub Pages 入口。
hero_subtitle_en: Long-term archive and GitHub Pages index for scheduled update tasks.
---

<section>
  <h2 class="lang zh">定时任务</h2>
  <h2 class="lang en">Scheduled Tasks</h2>
  {% for task in site.data.tasks.tasks %}
  <article class="task-card">
    <h2><a href="{{ task.url | relative_url }}"><span class="lang zh">{{ task.title_zh }}</span><span class="lang en">{{ task.title_en }}</span></a></h2>
    <p class="lang zh">{{ task.summary_zh }}</p>
    <p class="lang en">{{ task.summary_en }}</p>
  </article>
  {% endfor %}
</section>

<hr>
<section>
  <h2 class="lang zh">原始更新输出归档</h2>
  <h2 class="lang en">Raw Update Archive</h2>
  <p class="lang zh">跨所有定时任务的完整原始输出入口，内部按任务主题分组。</p>
  <p class="lang en">Repository-wide archive of complete task outputs, grouped by scheduled-task topic.</p>
  <p><a href="{{ '/raw-updates.html' | relative_url }}"><span class="lang zh">打开原始更新归档 →</span><span class="lang en">Open Raw Update Archive →</span></a></p>
</section>
