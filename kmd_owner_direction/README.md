# GPU KMD Owner Direction

This directory contains the task-local rules and reviewed output templates for the **GPU KMD Owner Direction** scheduled update task.

## Current GitHub Pages information architecture

The repository Pages root is **Time Update Tasks** at `/`. GPU KMD Owner Direction is one update task beneath that root.

The visible KMD Pages tree is intentionally reset starting from **Weekly #13 · 2026-11-07**:

```text
Time Update Tasks
└── GPU KMD Owner Direction
    ├── GPU Memory / Virtual Memory / Unified Memory
    │   ├── Timeline
    │   └── Focus
    │       ├── 2026-11-07 · TLB invalidation completion 与 BO lifetime
    │       ├── 2026-11-07 · DMA-BUF Mapping Types
    │       └── 2026-11-07 · PCIe P2P addressability
    ├── Other Topic
    │   └── Timeline
    └── Web Update Archive
        └── 2026-11-07 · Weekly #13
```

### Page roles

- **Task root**: explains the update task, depth policy, and content flow.
- **Memory root**: stable introduction to GPU Memory / Virtual Memory / Unified Memory.
- **Memory Timeline**: append-only timeline of every weekly A-section L3/L4 topic. Each topic title links directly to its primary source; topics selected for B additionally link to their Focus page.
- **Memory Focus**: detailed L3/L4 Key Topic pages. Focus page dates use the actual weekly update date.
- **Other Topic Timeline**: append-only timeline of C-section L1 updates, grouped by weekly date; directions with no meaningful update are omitted.
- **Web Update Archive**: index of complete reviewed weekly web outputs; each weekly entry links to the full original web output for that run.

## Baseline reset

All pre-Weekly-#13 KMD history, old owner/resource trees, old HLD pages, and old KMD data-model artifacts were deliberately removed because they were not reviewed against the current content standard. They must not be used as source material for future weekly outputs.

## Rules and template

Before modifying this task, read:

1. `kmd_owner_direction/UPDATE_RULES.md`
2. `kmd_owner_direction/sample/web_output/key_topic_detail_demo.md`
