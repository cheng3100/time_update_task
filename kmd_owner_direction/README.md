# KMD Owner Direction

This directory is the long-term source-of-truth for the scheduled **GPU KMD owner direction** task.

## Stability policy

- `HOME.md` defines the stable owner-domain taxonomy. Update it only when the owner explicitly adds, removes, merges, or redefines a top-level direction.
- Each owner archive keeps a stable `Summary` and a living `Current focus / Candidate features / Industry updates / Update history` section.
- `_data/kmd_owner_guides.json` is the stable **Detailed Owner Guide** presentation data: beginner introduction, why the Owner exists, core objects, architecture/data-control flow, staged 3–5 year development path, and cross-Owner boundary.
- `_data/kmd_owner_interactions.json` is the stable cross-Owner contract map. It explains how each Owner consumes or provides lifecycle, topology, telemetry, memory, recovery and firmware services to the other six Owners.
- Scheduled runs should not rewrite stable definitions, detailed guides, interaction maps, or onboarding paths just because a new patchset or article appears.
- Existing baseline KMD structure (basic probe/init, execution/submission, context/queue, basic scheduling, interrupts, MMIO/PCIe) is treated as the existing foundation, not as a new owner direction.
- Every owner direction must have: a clear independent problem domain, 3–5 year growth space, concrete KMD feature candidates, and at least one practical entry feature.

## Current top-level owner domains

1. GPU Memory / Virtual Memory / Unified Memory
2. GPU Virtualization / Security
3. GPU Power / Performance
4. GPU Reliability / Recovery / RAS
5. Multi-GPU / P2P / Fabric
6. GPU Observability / Profiling / Programmable Driver Infrastructure
7. GPU Firmware / Control Plane Architecture

A separate non-owner public topic tracks future Linux DRM / Accel / uAPI / upstream / kernel evolution.

## Jekyll / archive filename separation

The repository deliberately separates **content/archive Markdown** from **Jekyll presentation pages** at the filename level so the two cannot accidentally produce the same output path.

Naming convention:

- Owner source-of-truth: `*.archive.md`
- Long-term sub-direction learning material: `*.resource.md`
- Complete original task output: `*.raw.md`
- Curated dated update: `*.update.md`
- Jekyll presentation page source: normal page Markdown under `pages/` (with explicit `permalink`)

Example:

```text
kmd_owner_direction/owners/memory.archive.md
pages/owner-memory.md
        ↓ Jekyll permalink
/kmd_owner_direction/owners/memory.html
```

## Stable Detailed Owner Guide

The Pages layer includes a beginner-friendly stable guide for all seven Owners. The guide is intentionally separate from weekly Living updates.

Each Owner page should explain, in this order:

1. what problem the Owner solves in plain language;
2. why a basic working KMD still needs this capability domain;
3. the core KMD/HW/FW objects a new reader must recognize;
4. a visual architecture/data-control flow;
5. a staged path from the current entry feature to a mature independent Owner;
6. ownership boundaries plus an explicit interaction map with the other six Owners;
7. stable sub-directions, each rendered as **Prerequisite → Core mechanism → Capability**, followed by its durable learning-resource page;
8. current Living Industry Updates.

The task home additionally renders a top-to-bottom GPU software-stack architecture view so readers can understand where the seven capability domains sit relative to applications, UMD/runtime, shared KMD foundations and GPU HW/FW.

The interaction map and sub-direction learning path are intended to make the site usable as a **GPU KMD onboarding technology map**, not only as an Owner planning dashboard. Cross-Owner diagrams describe collaboration contracts; they do not merge ownership domains. The three-step sub-direction route is a concise orientation layer, while the independent `*.resource.md` page remains the durable deep-learning source.

## Current Feature HLD layer

Current entry features are maintained as an independent design/HLD-like presentation layer under `/kmd_owner_direction/features/`.

This layer is intentionally separate from:
- Stable Owner Guide: long-term domain definition and boundary;
- Weekly update: time-sensitive evidence and priority changes;
- Durable resources: stable learning material.

Each current feature keeps a stable URL and is updated incrementally rather than recreated every week. A feature HLD should first make the topic understandable to a reader who does not already know it, then move toward implementation detail. It should cover: definition and motivation; position in the GPU stack; use cases; core objects/terms; architecture and data/control flow; HW/FW/KMD/UMD/kernel boundaries; lifecycle/state machine; correctness/race/lifetime/performance challenges; failure/debug model; minimum capability loop; 3–6 month implementation path; 1–2 year evolution; cross-Owner contracts; upstream/vendor references; and hardware/open-question gates.

Current index: `/kmd_owner_direction/features/`.

## Three-layer archive model

### 1. `owners/` — stable owner definitions and long-term roadmaps
Contains the current source-of-truth for each owner domain. Owner archive files use the `.archive.md` suffix. Stable summaries remain unchanged unless an explicit owner-direction decision is made. Living sections can evolve.

### 2. `updates/` — curated dated update reports
Contains structured reports distilled from each run. New/migrated files use the `.update.md` suffix.

### 3. `raw_updates/` — complete per-run source snapshots
Contains one Markdown snapshot for every scheduled/test run. New/migrated files use the `.raw.md` suffix.

Rules:
- save the complete run output here before curating it into `updates/` or owner Living sections;
- historical raw snapshots are append-only by default;
- do not silently rewrite an old raw run to match a newer taxonomy;
- when the exact chat transcript cannot be recovered, preserve the earliest complete archived snapshot and label its provenance explicitly.

## Long-term resources

Stable learning resources live under `resources/<owner>/`. Each stable sub-direction should use one independent `*.resource.md` source-of-truth file so Jekyll presentation pages and durable learning archives remain separate.

## Weekly technical-depth contract

Weekly reports are evidence-driven technical reports, not short owner summaries. For every high-value Industry Update, preserve a primary/original source index and explain, when available: date, series/RFC version and patch count, problem statement, key mechanism/data structure/state machine/API or patch layering, delta from the previous revision, extracted design principle, concrete impact on the self-developed KMD, validation experiments and priority. If no high-value new item exists, say so explicitly.

Every current entry feature listed by the weekly report must link to one stable HLD-like page under `/kmd_owner_direction/features/`. The page is incrementally maintained across runs and must be **problem-first**: explain what the topic is, why it exists, what fails without it, typical scenarios, core objects, end-to-end flow, HW/FW/KMD/UMD/kernel boundaries, lifecycle/state machine, correctness/race/lifetime/performance challenges, failure/debug model, minimum capability loop, 3–6 month implementation path, 1–2 year evolution, cross-Owner contracts, upstream/vendor evidence and hardware/open-question gates. Architecture/sequence/state diagrams should be used when they improve understanding.

The four layers remain distinct:
1. Stable Owner Guide — long-term taxonomy/boundary;
2. Feature HLD — stable problem/design explanation for the current entry feature;
3. Weekly Industry Update — time-sensitive evidence and decisions;
4. Durable Resources — long-lived learning material.

## Update model

Each scheduled run should:

1. keep the stable taxonomy, Detailed Owner Guide, interaction maps and onboarding routes unless an explicit stable-guide change was requested;
2. produce and save the **complete original run Markdown** under `raw_updates/`;
3. refresh candidate features and industry progress for each domain;
4. select one entry feature for deeper analysis, including prerequisites, KMD/FW/UMD/HW boundaries, 3–6 month deliverables, and 1–2 year expansion path;
5. append/update a curated dated record under `updates/`;
6. refresh each owner's Living Industry Updates while leaving stable guide content unchanged;
7. update `_data/` consumed by Jekyll; presentation pages/layouts should not duplicate the content model.

## GitHub Pages

GitHub Pages is generated by Jekyll from `_data/`, `_layouts/` and `pages/`. The legacy `docs/` static site is excluded from the build.

- Task home: `/kmd_owner_direction/`
- Independent Owner pages: `/kmd_owner_direction/owners/<owner>.html`
- Detailed Memory roadmap: `/kmd_owner_direction/memory-roadmap.html`
- Raw task-update archive: `/kmd_owner_direction/raw-updates.html`
- Durable resources index: `/kmd_owner_direction/resources.html`
