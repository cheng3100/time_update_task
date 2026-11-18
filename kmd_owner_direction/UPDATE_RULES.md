# GPU KMD Weekly Update Rules

This document defines task-local rules for the scheduled **GPU KMD owner direction / weekly update** workflow under `kmd_owner_direction/`. These rules do not apply globally to unrelated scheduled tasks in this repository.

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

## 10. Task scope
These rules apply only to the GPU KMD weekly task. Other scheduled tasks must maintain their own task-local rules and must not inherit this file implicitly.

## 11. Confirmed chat-output depth and structure rules

### 11.1 Depth classification

GPU KMD Weekly does not distribute equal depth across all Owner domains. Depth is selected by relevance to the user's current Memory/UVM ownership and learning value.

- **L4 — Owner Design Transfer**
  - Default for **Memory / UVM / HMM / SVM / fault / migration / replay / GPUVM / page-table / TLB / residency / reclaim / eviction** topics.
  - Must go beyond upstream-news explanation into mechanism, Linux/kernel/driver structures, call paths or state/data flow, correctness/race/lifetime analysis, self-developed KMD architecture mapping, and validation/test implications.
  - Memory/UVM topics default to L4 unless there is a concrete reason to downgrade.

- **L3 — Learning Guide / Deep Technical Background**
  - Default for topics strongly coupled to Memory, especially **DMA-BUF, PCIe P2P, peer memory, IOMMU/IOMMUFD, VFIO, virtualization memory paths, address-space and mapping models**.
  - Must first build the reader's mental model before discussing the current patch/proposal.
  - Prefer architecture diagrams, object relationships, address-space diagrams, legacy/current/planned model comparisons, sequence flows, kernel object/API/callback relationships, and concrete driver examples.
  - L3 does not always need to become a full self-developed-KMD HLD.

- **L1 — Industry Radar / Awareness**
  - Default for other domains such as Power, RAS, Observability, Firmware, compiler/runtime, or ecosystem changes when they are not directly coupled to the current Memory/UVM learning goal.
  - Keep concise: what changed, why it matters, one concrete implication, and primary source links.
  - Do not mechanically expand these topics into HLD-level treatment.

A topic may be promoted above its default level when it exposes an important knowledge gap or directly changes the Memory/UVM architecture assumptions.

### 11.2 Deep-dive budget

Each weekly chat report should contain **no more than 3 deep-dive topics** at L3/L4.

The purpose is to preserve depth and learning value without turning every weekly update into a broad encyclopedia.

Preferred selection order:
1. Memory/UVM L4 topics with direct architecture/correctness value;
2. strongly Memory-coupled L3 topics needed to understand those changes;
3. only then other unusually high-value topics.

### 11.3 GPU KMD Weekly chat-output skeleton

The old A–P structure is retired for the chat report. The default weekly conversation output should use this simpler structure:

#### Opening — 本期重点
- Keep a short opening summary of the most important upstream/industry developments.
- Usually 2–4 items.
- Focus on what changed and why this week is worth reading.

#### A. L3/L4 Key Topic List
- A contains only the week's **L3/L4 candidate topics**.
- N is variable; do not force a fixed count.
- Every topic selected for Section B **must also appear in A** and must be placed first, in the **same order** as B.
- After the B-selected topics, A may include additional L3/L4 candidates that are worth tracking but are not selected for deep dive this week.
- Each A item should be concise: topic title, 1–3 sentence summary of what changed / why it matters, depth tag (L3/L4), and at least one direct primary/reference link.
- Do not expand architecture, code paths, race matrices or HLD detail in A; those belong in B.
- L1 topics do not belong in A.

#### B. Deep Dive：Memory / UVM 与强相关主题
- Select **up to 3 topics from A** for detailed analysis.
- The selected B topics must be the first items in A and preserve the same order.
- Merge all deep technical analysis here; do **not** create separate sections for “feature deep dive”, “Leader Memory deep dive”, or similar duplicate analysis.
- B follows the Key Topic Detail template defined in Section 11.6 and the reference sample at `kmd_owner_direction/sample/web_output/key_topic_detail_demo.md`.

For **L4 Memory/UVM** topics, prefer the following building blocks when relevant:
- upstream problem statement and concrete bug/limitation;
- architecture/data-flow diagram;
- key kernel/driver objects and call path;
- PTE/TLB/residency/lifetime relationships;
- state machine or ordering constraints;
- race/lifetime matrix;
- mapping to self-developed KMD objects/contracts;
- validation/fault-injection/test plan;
- primary source/code references.

For **L3 strongly coupled** topics, prefer:
- why the legacy model exists;
- legacy architecture diagram;
- current architecture/object model;
- what limitation triggered the new proposal;
- planned/new architecture diagram;
- kernel objects/APIs/callbacks and address representation;
- concrete GPU/driver/P2P/IOMMU example;
- how it connects back to Memory/UVM.

#### C. 其他方向 Topic List / Radar
- C contains the week's **remaining L1 topics**, grouped by direction/Owner.
- Include all meaningful L1 updates found for those directions; do not force a fixed number per direction.
- If a direction has no worthwhile update in the weekly time window, **omit that direction entirely** instead of writing “no update”.
- Each listed topic must include at least **one direct reference link**, preferably the primary patch/RFC/commit/thread or authoritative source.
- Keep each topic concise: title + short description of what changed / why it matters + reference link.
- Do not expand C items into deep architecture analysis; promotion to L3/L4 should move the topic into A and potentially B.

#### 总结回顾
Keep a short review at the end, focused on:
1. **本周最值得记住什么？**
2. **本周补了什么关键知识？**
3. **下一步最值得继续深挖什么？**

### 11.4 Removed/rejected sections for the chat report

Do not restore these as independent mandatory sections unless the user explicitly asks:
- old Owner radar table;
- early “all Owners HLD” section;
- durable-resources delta as a standalone chat section;
- team-size/project-allocation section;
- separate feature-deep-dive section;
- separate VFIO/Power/RAS/Multi-GPU/Observability/Firmware/Future sections;
- separate Leader Memory section;
- separate “本期对 Memory Owner 的结论” section.

Relevant conclusions from these areas should be folded into A, B, C, or 总结回顾 as appropriate.

### 11.5 Weekly #13 is the current reference sample

During the current redesign phase, use **2026-11-07 Weekly #13** as the reference sample for iterating the GPU KMD Weekly format.

Do not resume automatic weekly execution merely because this section exists. The automation remains paused until the user explicitly confirms that:
- chat output format is satisfactory;
- GitHub Pages presentation is satisfactory;
- content-selection/depth rules are satisfactory;
- the finalized rules have been fixed in repository instructions and automation prompt.

### 11.6 Key Topic Detail / B-module web-output template

The confirmed reference implementation for B-module deep-dive output is:

- `kmd_owner_direction/sample/web_output/key_topic_detail_demo.md`
- https://github.com/cheng3100/time_update_task/blob/main/kmd_owner_direction/sample/web_output/key_topic_detail_demo.md

Future L3/L4 Bx sections should use this file as the primary style/content-depth reference unless the user explicitly changes the template.

#### Mandatory opening: problem background + direct links

Every Key Topic must start with a **Section 0** that establishes the problem before entering mechanism or code.

Section 0 should normally answer:
1. what the problem/change is;
2. where it appears and what scenario triggers it;
3. what the impact is;
4. what the current upstream solution/proposal is;
5. what revision/status/progress exists within the weekly time window;
6. which primary sources should be read next.

The reference/index subsection must provide **direct clickable URLs**, not only patch titles, filenames, function names, or vague references.

Preferred reference order:
1. primary patch/RFC/commit/thread;
2. review/discussion thread;
3. relevant upstream source file(s);
4. later revision(s), clearly marked as outside the current weekly window when applicable.

#### Kernel/KMD implementation grounding

When a topic touches Linux kernel or GPU KMD implementation, the explanation must be grounded in real code locations.

Prefer this pattern:
- source file path;
- function / struct / field name;
- direct source URL;
- one short explanation of why that location matters.

Use small code excerpts only when they materially explain the mechanism. As a default, keep any one excerpt to roughly **5–15 relevant lines** and avoid copying whole functions. The goal is to expose the critical implementation relationship while leaving the full source available through direct links.

A Key Topic should usually contain no more than a few critical code excerpts. Prefer source-navigation pointers over large code dumps.

#### Mechanism before patch diff

Do not explain a complex patch only from its diff. First build the reader's mental model:
- architecture/data-flow diagram;
- object relationship;
- address-space relationship;
- state/lifetime/ordering model;
- legacy behavior when relevant.

Then explain how the current upstream patch changes that model.

ASCII diagrams are acceptable and preferred in chat/web output when they make the mechanism easier to understand.

#### Facts vs derived design guidance

Clearly separate:
- **upstream facts**: what the patch/source/review actually does;
- **derived guidance**: implications or recommendations for the self-developed KMD.

Do not present a suggested self-developed structure/field/state machine as though it already exists upstream.

#### Why the change matters

Each Key Topic must extract at least one reusable architecture/design principle. The analysis should not stop at “what lines changed”.

For example, the reference B1 extracts:

```text
page-table lifetime
    !=
translation-cache lifetime
    !=
memory-object lifetime
```

The reusable principle is the main reason the topic is worth retaining beyond the weekly news cycle.

#### L4 Memory/UVM requirements

For L4 Memory/UVM topics, include when relevant:
- real upstream issue/limitation;
- key code path and object/state references;
- lifetime / generation / ordering analysis;
- race or lifetime matrix;
- mapping to self-developed KMD contracts or objects;
- validation / fault-injection plan;
- required observability/debug state;
- long-lived invariant/design principle.

These are expected components for L4 unless the topic genuinely does not support one of them.

#### L3 Memory-adjacent requirements

For L3 DMA-BUF/P2P/Virtualization-memory/IOMMU-style topics, emphasize:
- legacy/current/planned architecture;
- object model and address representation;
- why the old abstraction is insufficient;
- real kernel APIs/callbacks/source locations;
- concrete GPU/peer-memory example;
- relationship back to Memory/UVM.

L3 does not require a complete self-developed-KMD HLD or full race matrix unless the topic naturally demands it.

#### Verification and observability

Where the topic describes a correctness or lifetime problem, the Key Topic should explain how to test it:
- how to enlarge the race window;
- what to inject/delay/reset;
- what result would demonstrate the bug;
- what result would prove the fix;
- what IDs/generations/timestamps/events should be traced.

#### Source-reading section

A Key Topic should end with a compact source-navigation section when kernel/KMD code is involved.

Preferred form:

```text
problem
  ↓
primary patch/RFC
  ↓
critical 5–15 line code excerpt
  ↓
source file
  ↓
function / struct / field
  ↓
review / later revision
```

This section is a learning index, not a bibliography dump.

#### Time-window integrity

The “current status” of a weekly Key Topic must stop at that weekly run's time boundary.

A later revision may be linked as “follow-up / later progress”, but must not be presented as if it was already current during the historical weekly run.

### 11.7 GitHub Pages timeline date-node linking

For every KMD GitHub Pages timeline page, each dated weekly node must itself be an internal link to that run's complete reviewed **Web Update Archive** page.

Required pattern:

```markdown
## [2026-11-07 · Weekly #13]({{ '/kmd_owner_direction/web-update-archive/2026-11-07-weekly-13/' | relative_url }})
```

This applies to:
- GPU Memory / Virtual Memory / Unified Memory → Timeline;
- Other Topic → Timeline;
- any future timeline introduced under this KMD task.

The roles of links are distinct:
- **date / weekly node** → internal Web Update Archive for the complete reviewed weekly output;
- **topic title** → direct primary/upstream/reference source;
- **Focus →** → internal detailed L3/L4 Focus page when that topic was selected for Section B.

Do not use a non-linked date heading on a timeline when a corresponding Web Update Archive page exists.

