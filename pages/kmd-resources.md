---
layout: default
title: GPU KMD Learning Resources
hero_title: GPU KMD Learning Resources
hero_subtitle_zh: 按 Owner / 子方向组织的长期学习资料入口。源文档保存在 kmd_owner_direction/resources/。
hero_subtitle_en: Durable learning-resource index organized by Owner and sub-direction. Source documents live under kmd_owner_direction/resources/.
permalink: /kmd_owner_direction/resources.html
back_url: /kmd_owner_direction/
back_zh: GPU KMD Owner Direction
back_en: GPU KMD Owner Direction
---

{% assign kmd = site.data.kmd_owner_direction %}
<div class="owner-grid">
{% for owner in kmd.owners %}
<section class="owner-card">
  <h2>{{ owner.name }}</h2>
  <ul>{% for topic in owner.topics %}<li>{{ topic }}</li>{% endfor %}</ul>
  <p><a href="https://github.com/cheng3100/time_update_task/tree/main/kmd_owner_direction/resources"><span class="lang zh">查看长期资料 Markdown →</span><span class="lang en">Open durable resource Markdown →</span></a></p>
</section>
{% endfor %}
</div>
