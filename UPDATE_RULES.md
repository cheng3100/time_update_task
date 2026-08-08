# Global Scheduled Update Rules

This document defines repository-wide rules shared by **all scheduled update tasks** in `cheng3100/time_update_task`.

## 1. Complete chat report + GitHub archive are both mandatory
Every scheduled run must produce the task's **complete report in the current ChatGPT conversation**. GitHub archival is an additional persistence layer, never a replacement for the full chat report.

## 2. Separate dynamic industry updates from durable learning knowledge
### Industry / ecosystem updates
- refresh every run;
- group at the task's natural top-level direction/category;
- prefer upstream patchsets/RFCs/kernel docs/vendor open-source implementations/high-authority sources;
- explain change, importance, impact and follow-up priority;
- explicitly state when there is no high-value new item instead of filling space with stale news.

### Long-term high-value learning resources
- organize under stable sub-topics/sub-directions, never by update date;
- remain relatively stable and grow cumulatively;
- only add/replace when a clearly better, more authoritative or more complete reference is found;
- every resource entry must explain: **what it is / why it is valuable / what to focus on / study cautions / source link**.

## 3. One independently maintained learning document per stable sub-direction
For any task that has stable sub-directions, each sub-direction must own an independent long-term learning document instead of being only one bullet inside a large Owner/category resource file.

Recommended structure:
```text
<task>/resources/<top-level-category>/<sub-direction>.md
```

Rules:
- each file is a stable source-of-truth for that sub-direction's learning path and durable references;
- files use **stable growth**: additions are preferred over rewrites;
- do not mix short-lived Industry Updates into these sub-direction learning files;
- top-level category resource files, if retained, should mainly act as indexes/compatibility pointers.

## 4. Stable structure vs living content
Stable content includes top-level taxonomy, owner/category definitions, scope boundaries, long-term capability loops and enduring roadmap stages. It changes only on explicit user direction.

Living content includes current entry feature/recommendation, near-term priorities, Industry Updates, current projects and dated judgments. Weekly news must not silently rewrite stable structure.

## 5. GitHub archival layout
```text
<task>/
├── README.md
├── HOME.md
├── raw_updates/        # complete run snapshots; append-only
├── updates/            # structured/curated dated updates
├── resources/
│   └── <category>/
│       ├── README.md
│       └── <sub-direction>.md
└── ... task-specific stable files
```

`raw_updates/` is append-only historical evidence. `resources/` is cumulative durable knowledge, not news.

## 6. GitHub Pages rules
Each task should have an independent Pages view when practical.
- Pages is presentation, not the only source of truth;
- keep Stable and Living content visually distinct;
- show fresh Industry Updates at the relevant top-level category/Owner;
- every stable sub-direction must have a corresponding Pages view/unique URL backed by its own learning document;
- the Pages sub-direction view should display the resource annotations (what it is / value / focus / cautions / link), not only a naked URL list;
- keep access to raw update history where useful.

### Bilingual support
For pages supporting Chinese/English, use the same page/DOM/layout and one language-toggle button; do not maintain two drifting page trees. Default Chinese unless task-specific rules say otherwise; persist selection when practical.

## 7. Source quality
Dynamic updates prioritize primary/upstream/high-authority sources. Durable resources prioritize authority, depth and durability; an older canonical reference may be better than a newer superficial article.

## 8. Traceability
Every run gets a dated/unique raw snapshot; keep links between current curated views and history where practical; never claim verbatim provenance when only a reconstruction exists.

## 9. Repository-wide vs task-specific rules
This file contains cross-task behavior only. Task-specific taxonomy, owner boundaries, report sections and domain-specific sources belong in the task directory/prompt.
