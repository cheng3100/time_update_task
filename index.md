---
layout: default
title: Time Update Tasks
nav_order: 1
permalink: /
---

# Time Update Tasks

<span class="lang zh">技术更新任务的 GitHub Pages 根节点。每个更新任务拥有独立的内容树与归档。</span><span class="lang en">GitHub Pages root for technical update tasks. Each update task owns an independent content tree and archive.</span>

## <span class="lang zh">更新任务</span><span class="lang en">Update Tasks</span>

{% for task in site.data.tasks.tasks %}
<article class="owner-card">
  <h2><a href="{{ task.url | relative_url }}"><span class="lang zh">{{ task.title_zh }}</span><span class="lang en">{{ task.title_en }}</span></a></h2>
  <p class="lang zh">{{ task.summary_zh }}</p>
  <p class="lang en">{{ task.summary_en }}</p>
</article>
{% endfor %}
