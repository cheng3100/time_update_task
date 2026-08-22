---
layout: default
title: Learning Resources
parent: GPU KMD Owner Direction
nav_order: 9
permalink: /kmd_owner_direction/resources.html
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
    {% capture resource_url %}/kmd_owner_direction/resources/{{ owner.id }}/{{ resource.slug }}.html{% endcapture %}
    <li><strong>{{ resource.title }}</strong><br><a href="{{ resource_url | relative_url }}"><span class="lang zh">独立长期资料网页 →</span><span class="lang en">Dedicated durable resource page →</span></a></li>
  {% endfor %}
  </ul>
</section>
{% endfor %}
</div>
