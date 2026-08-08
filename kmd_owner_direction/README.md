# KMD Owner Direction

This directory is the long-term source-of-truth for the scheduled **GPU KMD owner direction** task.

## Stability policy

- `HOME.md` defines the stable owner-domain taxonomy. Update it only when the owner explicitly adds, removes, merges, or redefines a top-level direction.
- Each owner page keeps a stable `Summary` and a living `Current focus / Candidate features / Industry updates / Update history` section.
- Scheduled runs should not rewrite stable definitions just because a new patchset or article appears.
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

## Three-layer archive model

### 1. `owners/` — stable owner definitions and long-term roadmaps
Contains the current source-of-truth for each owner domain. Stable summaries remain unchanged unless an explicit owner-direction decision is made. Living sections can evolve.

### 2. `updates/` — curated dated update reports
Contains structured reports distilled from each run. These are allowed to summarize/reorganize the original output for long-term readability and Pages rendering.

### 3. `raw_updates/` — complete per-run source snapshots
Contains one Markdown snapshot for every scheduled/test run.

Rules:
- save the complete run output here before curating it into `updates/` or owner Living sections;
- historical raw snapshots are append-only by default;
- do not silently rewrite an old raw run to match a newer taxonomy;
- when the exact chat transcript cannot be recovered, preserve the earliest complete archived snapshot and label its provenance explicitly;
- every future run should add one new raw Markdown file and update `raw_updates/README.md`.

## Update model

Each scheduled run should:

1. keep the stable taxonomy unless an explicit direction change was requested;
2. produce and save the **complete original run Markdown** under `raw_updates/`;
3. refresh candidate features and industry progress for each domain;
4. select one entry feature for deeper analysis, including prerequisites, KMD/FW/UMD/HW boundaries, 3–6 month deliverables, and 1–2 year expansion path;
5. append/update a curated dated record under `updates/`;
6. refresh each owner's Living Industry Updates while leaving Stable Summary unchanged;
7. update GitHub Pages to expose the current living view and the raw archive.

## GitHub Pages

- Main KMD owner page: `docs/kmd_owner_direction/index.html`
- Detailed Memory owner roadmap: `docs/kmd_owner_direction/memory-roadmap.html`
- Raw task-update archive: `docs/kmd_owner_direction/raw-updates.html`
