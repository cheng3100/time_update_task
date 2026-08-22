# Global Scheduled Update Rules

This document defines repository-wide rules shared by **all scheduled update tasks** in `cheng3100/time_update_task`.

## 1. Complete chat report + GitHub archive are both mandatory
Every scheduled run must produce the task's **complete report in the current ChatGPT conversation**. GitHub archival is an additional persistence layer, never a replacement for the full chat report.

### Canonical raw invariant
For every run, there must be exactly one canonical report body, conceptually `REPORT_BODY`.

The task must follow this order:
1. research and compose the complete final report in the task's required chat language;
2. freeze that exact Markdown/text as `REPORT_BODY`;
3. send `REPORT_BODY` to the ChatGPT conversation without shortening, translating, reorganizing or replacing it with an archive notice;
4. write the **same `REPORT_BODY` byte-for-byte in content semantics** to the run's `*.raw.md` snapshot (the only allowed archive-only difference is a clearly separated provenance/front-matter header if the repository format requires one; the report body itself must be unchanged);
5. only after the raw snapshot is committed may the task derive curated updates, translations, Home summaries, Living data or resource changes.

Forbidden:
- independently regenerating or summarizing the report for `*.raw.md`;
- translating the raw body when the chat report was in another language;
- compressing sections, removing source links, changing heading structure, or replacing detailed paragraphs with bullets in raw;
- constructing raw from the curated update or from `_data`;
- calling a reconstruction, translation or summary “raw/original/verbatim”.

If the exact chat report cannot be persisted, the task must mark the archive as **unverified/reconstructed**, never as canonical raw.

## 2. Inspect the current task layout before every GitHub write
Repository layouts may evolve independently of the scheduled-task prompt. Before writing an archive, the task must inspect the current task README / archive policy, current filenames, `_data`/layouts/generator when relevant, and follow the **current repository structure** rather than a stale hard-coded path convention.

Rules:
- task-local README/archive policy is authoritative for current filenames and source-of-truth locations;
- do not recreate retired static-page trees if the repository has moved to a generated/Jekyll model;
- update source-of-truth archives/data and let the repository's current page generator produce presentation output;
- preserve current suffix/naming conventions (for example `.archive.md`, `.resource.md`, `.raw.md`, `.update.md`) when the task defines them;
- when layout and an old task prompt conflict, preserve content intent but adapt the write path to the current repository model.

## 3. Separate dynamic industry updates from durable learning knowledge
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

### Durable-resource source mix
A high-value learning library should not collapse into an official-document link list. Prefer a complementary source stack where quality material exists:
1. **Canonical / specification** — official subsystem documentation, standards and upstream design documents define authoritative semantics and boundaries.
2. **Deep explanation** — LWN, high-quality independent engineering blogs, maintainer articles and strong vendor technical blogs build intuition and explain why the mechanism exists.
3. **Implementation / practice** — source walkthroughs, production tooling, debugging/profiling articles and implementation case studies show how the design behaves in real systems.
4. **Research** — papers are retained when they expose durable future architecture ideas or measurements not covered by production documentation.

Do **not** force one source of every type into every sub-topic. Quality beats quota: a canonical spec alone is preferable to a shallow SEO/tutorial article. Add explanatory blogs only when they materially improve understanding.

## 4. One independently maintained learning document per stable sub-direction
For any task that has stable sub-directions, each sub-direction must own an independent long-term learning document instead of being only one bullet inside a large Owner/category resource file.

Recommended conceptual structure (task-specific naming/suffixes may differ):
```text
<task>/resources/<top-level-category>/<sub-direction>.<resource-suffix>.md
```

Rules:
- each file is a stable source-of-truth for that sub-direction's learning path and durable references;
- files use **stable growth**: additions are preferred over rewrites;
- do not mix short-lived Industry Updates into these sub-direction learning files;
- top-level category resource files, if retained, should mainly act as indexes/compatibility pointers.

## 5. Stable structure vs living content
Stable content includes top-level taxonomy, owner/category definitions, scope boundaries, **detailed owner descriptions, sub-direction definitions/descriptions**, long-term capability loops and enduring roadmap stages. It changes only on explicit user direction.

Living content includes current entry feature/recommendation, near-term priorities, Industry Updates, current projects and dated judgments. Weekly news must not silently rewrite stable structure.

Additional rules for stable direction definitions:
- keep a dedicated source-of-truth data/document layer when the site supports it;
- the task homepage should summarize every stable top-level direction and its stable sub-directions;
- each direction page should give the fuller long-term responsibility, ownership boundary, and a detailed description of every stable sub-direction;
- routine scheduled runs may update entry features, news, references and history, but must not rewrite these descriptions just because new sources or projects appeared;
- only explicit taxonomy/scope/boundary changes justify editing the stable descriptions.

## 6. GitHub archival model
Every task should maintain equivalent logical layers, while exact filenames/paths are determined by that task's **current README/layout**:
- stable owner/category sources;
- append-only complete raw run snapshots;
- curated dated updates;
- stable-growth per-subdirection resource documents;
- page data/layout/generator inputs when the task uses generated Pages.

`raw_updates/`-equivalent content is append-only historical evidence. Durable resources are cumulative knowledge, not news.

## 7. GitHub Pages rules
Each task should have an independent Pages view when practical.
- Pages is presentation, not the only source of truth;
- keep Stable and Living content visually distinct;
- show fresh Industry Updates at the relevant top-level category/Owner;
- every stable sub-direction must have a corresponding Pages view/unique URL backed by its own learning document;
- the Pages sub-direction view should display the resource annotations (what it is / value / focus / cautions / link), not only a naked URL list;
- keep access to raw update history where useful;
- if Pages are generated, edit their source data/content and generator inputs rather than generated output.

### Bilingual support
For pages supporting Chinese/English, use the same page/DOM/layout and one language-toggle button; do not maintain two drifting page trees. Default Chinese unless task-specific rules say otherwise; persist selection when practical.

## 8. Source quality
Dynamic updates prioritize primary/upstream/high-authority sources. Durable resources prioritize authority, depth, explanatory value and durability; an older canonical reference or classic engineering article may be better than a newer superficial article.

## 9. Traceability
Every run gets a dated/unique raw snapshot; keep links between current curated views and history where practical; never claim verbatim provenance when only a reconstruction exists.

For tasks with a Pages raw-archive view, provenance must be rendered explicitly when a historical file is not verified as the exact chat report. A Pages renderer must never silently “repair” a raw mismatch by translating or summarizing it and then label the result original/raw.

## 10. Repository-wide vs task-specific rules
This file contains cross-task behavior only. Task-specific taxonomy, owner boundaries, report sections and domain-specific sources belong in the task directory/prompt.