---
layout: default
title: GPU KMD Learning Resources
hero_title: GPU KMD Learning Resources
hero_subtitle_zh: 按 Owner → 稳定子方向组织的长期高价值资料索引。每个子方向都有独立 Markdown 归档。
hero_subtitle_en: Durable high-value learning resources organized by Owner → stable sub-direction, with one Markdown archive per sub-direction.
permalink: /kmd_owner_direction/resources.html
back_url: /kmd_owner_direction/
back_zh: GPU KMD Owner Direction
back_en: GPU KMD Owner Direction
---

{% assign kmd = site.data.kmd_owner_direction %}
{% assign resource_map = site.data.kmd_resources %}
<div class="owner-grid">
{% for owner in kmd.owners %}
<section class="owner-card">
  <h2><a href="{{ '/kmd_owner_direction/owners/' | append: owner.id | append: '.html' | relative_url }}">{{ owner.name }}</a></h2>
  {% assign resources = resource_map[owner.id] %}
  <ul class="resource-list">
  {% for resource in resources %}
    <li><strong>{{ resource.title }}</strong><br><a href="https://github.com/cheng3100/time_update_task/blob/main/kmd_owner_direction/resources/{{ owner.id }}/{{ resource.slug }}.resource.md"><span class="lang zh">独立长期资料档案 →</span><span class="lang en">Dedicated durable resource archive →</span></a></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
</div>
