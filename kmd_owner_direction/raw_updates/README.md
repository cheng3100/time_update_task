# GPU KMD Owner Direction — Raw Update Archive

This directory stores the **complete per-run update snapshots** separately from the curated `updates/` summaries and the stable `owners/` roadmap files.

## Archive policy

- One `*.raw.md` file per scheduled/test run.
- Raw files are append-only snapshots: do not silently rewrite a historical run to match the latest owner taxonomy.
- `owners/*.archive.md` contains the current stable owner definition and long-term roadmap.
- `updates/*.update.md` contains structured/curated dated summaries used to refresh the living website.
- `raw_updates/*.raw.md` contains the complete original update text (or, where the exact chat transcript is no longer recoverable, the earliest complete archived run snapshot with provenance explicitly marked).
- Every future scheduled update must create the raw Markdown snapshot first, then derive/update the curated owner pages from it.

## Runs

| Run | Raw Markdown | Provenance |
|---|---|---|
| 2026-08-08 Test #3 · Resource Model R2 | [`2026-08-08-test-3-r2.raw.md`](./2026-08-08-test-3-r2.raw.md) | Complete archived output for Resource Model R2. |
| 2026-08-08 Test #3 | [`2026-08-08-test-3.raw.md`](./2026-08-08-test-3.raw.md) | Complete Test #3 snapshot. |
| 2026-08-08 Test #2 | [`2026-08-08-test-2.raw.md`](./2026-08-08-test-2.raw.md) | Earliest complete Test #2 archive; provenance is documented in the file. |
| 2026-08-08 Test #1 | [`2026-08-08-test-1.raw.md`](./2026-08-08-test-1.raw.md) | Reconstructed from the complete assistant output preserved in the conversation. |

## Web archive

GitHub Pages archive: `/kmd_owner_direction/raw-updates.html`
