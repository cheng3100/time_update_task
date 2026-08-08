# Global Scheduled Update Rules

This document defines repository-wide rules shared by **all scheduled update tasks** in `cheng3100/time_update_task`.

Task-specific prompts and subdirectories may add domain-specific rules, but should not duplicate or contradict these global rules.

## 1. Chat output and GitHub archive are both required

Every scheduled run must produce a **complete report in the current ChatGPT conversation**.

- GitHub archival is an additional persistence layer, not a replacement for the chat response.
- Do not respond only with “archived to GitHub” or a short summary when the task normally produces a full report.
- The chat report should preserve the same level of detail as the task's normal/manual test updates.
- If the task has a fixed report structure, all required sections should still appear in chat.

At the same time, every run should be persisted to GitHub when that task is configured for archival.

## 2. Preserve two different knowledge layers

Each task should distinguish between two fundamentally different information classes.

### A. Industry / ecosystem updates — fresh and dynamic

These are time-sensitive signals such as:
- new upstream patchsets, RFCs, merge-window changes
- new releases, driver architecture changes, uAPI changes
- vendor/open-source implementation changes
- new projects, papers, tools or standards work

Rules:
- refresh every run;
- group at the task's natural top-level direction/category;
- prefer primary or high-authority engineering sources;
- explain what changed, why it matters, expected impact and recommended follow-up priority;
- if there is no meaningful new development, explicitly state that instead of filling space with stale news.

### B. Long-term high-value learning resources — stable and cumulative

These are durable materials for deep understanding, such as:
- Linux kernel / subsystem official documentation
- open-source driver design documentation
- specifications and standards
- canonical LWN articles or high-quality engineering blogs
- foundational or especially useful papers

Rules:
- organize by **stable sub-topic/sub-direction**, not by update date;
- keep them relatively stable across runs;
- only add or replace a resource when a clearly better, more authoritative or more complete reference is found;
- attach a short note explaining why the resource is worth reading and what to focus on;
- treat the resource library as cumulative long-term study infrastructure rather than news.

## 3. Stable structure vs living content

For tasks with a long-term taxonomy, roadmap or category model:

### Stable content
Examples:
- top-level directions/categories
- owner/domain definitions
- scope boundaries
- long-term capability loops
- enduring roadmap stages

Stable content should change only when the user explicitly asks to add, remove, merge or redefine it.

### Living content
Examples:
- current entry feature / current recommendation
- near-term priorities
- industry updates
- current project suggestions
- dated judgments

Living content may refresh every run.

Do not let weekly news silently rewrite stable task structure.

## 4. GitHub archive layout

Each scheduled task should own a dedicated subdirectory in this repository.

Recommended structure:

```text
<task>/
├── README.md
├── HOME.md                    # stable overview when applicable
├── raw_updates/               # complete run snapshots; append-only
├── updates/                   # structured/curated dated updates
├── resources/                 # stable long-term learning/resource library
└── ... task-specific files
```

Rules:
- `raw_updates/` is append-only historical evidence;
- do not silently rewrite old raw snapshots because later conclusions changed;
- `updates/` may contain structured summaries derived from the raw report;
- `resources/` is cumulative and organized by stable topic/sub-topic;
- task-specific stable files should be edited only when their stable definition actually changes.

## 5. GitHub Pages rules

Each task should have an independent GitHub Pages view when practical.

General rules:
- Pages is a presentation layer over the archived knowledge, not the only source of truth;
- preserve a clear separation between Stable content and Living updates;
- show fresh industry updates in the relevant top-level category/page;
- show long-term learning-resource links beside or beneath the corresponding stable sub-topic;
- retain access to full raw-update history when useful.

### Bilingual support

For task pages that support Chinese and English:
- use the **same page, same DOM structure and same layout**;
- provide a single language-toggle button;
- do not maintain independent Chinese and English pages that can drift apart;
- default to Chinese unless the task specifies otherwise;
- persist the user's language selection when practical.

## 6. Source quality and freshness

For dynamic updates:
- prefer upstream mailing lists/RFCs/patchsets, kernel docs, official project docs, vendor open-source drivers and authoritative engineering sources;
- use secondary articles primarily for context, not as the only evidence for technical architectural claims;
- distinguish new developments from older background material.

For long-term resources:
- freshness is less important than authority, depth and durability;
- an older but canonical document can be better than a newer superficial article.

## 7. Update history and traceability

Every run should remain traceable.

- store a dated or uniquely identified raw snapshot;
- keep links between the current curated view and historical runs where practical;
- never claim an exact verbatim historical transcript if only a reconstruction is available; record provenance explicitly;
- do not destroy historical context merely because the current recommendation changed.

## 8. Repository-wide vs task-specific rules

This file contains only **cross-task behavior rules**.

Task-specific documents should define:
- domain taxonomy
- topic priorities
- owner boundaries
- task-specific report sections
- domain-specific research sources
- task-specific roadmap logic

If a behavior should apply to all scheduled tasks, add it here rather than duplicating it in every task directory.
