# GPU KMD Owner Direction — Raw Update Archive

This directory stores the **complete per-run update snapshots** separately from the curated `updates/` summaries and the stable `owners/` roadmap files.

## Archive policy

- One Markdown file per scheduled/test run.
- Raw files are append-only snapshots: do not silently rewrite a historical run to match the latest owner taxonomy.
- `owners/` contains the current stable owner definition and long-term roadmap.
- `updates/` contains structured/curated dated summaries used to refresh the living website.
- `raw_updates/` contains the complete original update text (or, where the exact chat transcript is no longer recoverable, the earliest complete archived run snapshot with provenance explicitly marked).
- Every future scheduled update must create the raw Markdown snapshot first, then derive/update the curated owner pages from it.

## Runs

| Run | Raw Markdown | Provenance |
|---|---|---|
| 2026-08-08 Test #1 | [`2026-08-08-test-1.md`](./2026-08-08-test-1.md) | Reconstructed from the complete assistant output preserved in the current conversation. |
| 2026-08-08 Test #2 | [`2026-08-08-test-2.md`](./2026-08-08-test-2.md) | Exact copy of the earliest complete Test #2 archive already stored in `updates/2026-08-08-test-2.md`; exact chat-transcript source was not recoverable from current conversation context, so this provenance is intentionally explicit. |

## Web archive

GitHub Pages archive: `docs/kmd_owner_direction/raw-updates.html`
