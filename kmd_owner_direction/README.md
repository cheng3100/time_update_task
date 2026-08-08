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

## Update model

Each scheduled run should:

1. keep the stable taxonomy unless an explicit direction change was requested;
2. refresh candidate features and industry progress for each domain;
3. select one entry feature for deeper analysis, including prerequisites, KMD/FW/UMD/HW boundaries, 3–6 month deliverables, and 1–2 year expansion path;
4. append a dated record under `updates/`.
