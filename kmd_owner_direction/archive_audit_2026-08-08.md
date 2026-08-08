# KMD Owner Direction Archive Audit — 2026-08-08

Purpose: verify that the information from the 2026-08-08 test updates has been persisted in GitHub and identify gaps between chat output, curated reports, stable owner pages and GitHub Pages.

## Audit result

| Item | GitHub status | Location / action |
|---|---|---|
| Stable 7-owner taxonomy + public future topic | ✅ Present | `HOME.md` + owner files |
| Per-owner stable summary | ✅ Present | `owners/*.md` |
| Per-owner current entry feature | ✅ Present | `owners/*.md` + Pages |
| Per-owner Industry Updates | ✅ Present | `owners/*.md` + Pages |
| Current 5–6 person feature-project mapping | ✅ Present | `updates/2026-08-08.md`, `updates/2026-08-08-test-2.md` |
| Firmware Control Plane detailed entry design | ✅ Present | `updates/2026-08-08.md` + raw Test #1 |
| Migration-granularity detailed entry design | ✅ Present | `updates/2026-08-08-test-2.md` + raw Test #2 |
| VFIO/SR-IOV project conditions | ✅ Present | curated updates + Virtualization owner |
| Power/Performance priority | ✅ Present | `updates/2026-08-08.md` + owner page |
| Reliability/RAS priority | ✅ Present | `updates/2026-08-08.md` + owner page |
| Multi-GPU owner boundary vs Memory | ✅ Present | update + Memory/Multi-GPU owner pages |
| Observability/eBPF/PMU/Profiling boundary | ✅ Present | update + owner page |
| Firmware vs Reliability boundary | ✅ Present | `updates/2026-08-08.md` + Memory/FW/RAS related owner docs |
| Public DRM/Accel/uAPI/upstream evolution topic | ✅ Present | shared future topic + updates |
| Future 8–10 person owner split nodes | ✅ Present in curated archive | `updates/2026-08-08.md` |
| Leader Memory deep-dive topic (`drm_pagemap` ownership/lifetime) | ✅ Present | `updates/2026-08-08.md` + raw Test #1 |
| Detailed Memory **Entry → Deepen → Expand → Evolve** owner roadmap | ✅ Fixed in this audit | expanded `owners/memory.md` + `docs/kmd_owner_direction/memory-roadmap.html` |
| Complete original/raw run archive | ✅ Archive framework added | `raw_updates/` + Pages raw archive |
| Test #1 complete raw snapshot | ✅ Added | `raw_updates/2026-08-08-test-1.md` |
| Test #2 raw snapshot | ⚠️ Provenance-limited but preserved | exact copy of earliest complete archived Test #2 snapshot; current context did not expose an exact original chat transcript |

## Previously missing information fixed by this audit

### 1. Memory long-term growth path was too compressed
Before this audit, `owners/memory.md` only contained the entry fault/migration closure and a flat list of sub-directions. It did not preserve the detailed owner progression discussed in the task updates.

Fixed by adding four explicit phases:

1. **Entry** — Recoverable fault + HMM + migration + replay
2. **Deepen** — GPUVM + migration granularity + oversubscription/eviction
3. **Expand** — IOMMU/SVA/ATS/PRI + NUMA + cross-device memory
4. **Evolve** — multi-GPU UVM + tiered/CXL memory + placement/migration/QoS policy

A dedicated bilingual Pages page now presents this roadmap.

### 2. Curated update files were not the same thing as raw output archives
The existing `updates/` directory contained structured reports, but there was no explicit rule that every run's full original output must be retained.

Fixed by creating the `raw_updates/` append-only archive and documenting the three-layer model:

```text
owners/      stable source-of-truth + long-term owner roadmap
updates/     curated dated reports / living summaries
raw_updates/ complete per-run source snapshots
```

## Remaining limitation

The exact Test #2 chat transcript is not available in the current conversation context. The earliest complete Test #2 Markdown already stored in the repository has therefore been copied into `raw_updates/` with an explicit provenance note. This avoids falsely claiming a verbatim chat transcript while still preserving the complete historical run snapshot that is available.

## Rule for all future runs

Every new run should persist artifacts in this order:

```text
1. complete assistant output
       ↓
2. raw_updates/YYYY-MM-DD[-run-N].md
       ↓
3. curated updates/YYYY-MM-DD[-run-N].md
       ↓
4. refresh owners/* Living sections
       ↓
5. refresh GitHub Pages
```

Stable summaries and owner taxonomy remain protected from routine update churn.
