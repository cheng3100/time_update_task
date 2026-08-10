# GPU KMD Owner Direction — Raw Update Archive

This directory stores the **complete per-run update snapshots** separately from the curated `updates/` summaries and the stable `owners/` roadmap files.

## Archive policy

- One `*.raw.md` file per scheduled/test run.
- **The canonical raw language is the language actually emitted by ChatGPT. For this task that is Chinese by default.**
- The raw snapshot must be written **before** translation, summarization, restructuring, Pages rendering, or Owner/Living-section updates.
- Raw files are append-only snapshots: do not silently rewrite a historical run to match the latest owner taxonomy.
- A translation is a derived reading artifact and must never overwrite the canonical raw snapshot.
- Source/reference links that appeared in the ChatGPT output belong in the canonical raw text. Additional archive-only references may be rendered separately by Pages metadata, but must not be inserted into the raw body and presented as if they were in the original transcript.
- `owners/*.archive.md` contains the current stable owner definition and long-term roadmap.
- `updates/*.update.md` contains structured/curated dated summaries used to refresh the living website.
- `raw_updates/*.raw.md` contains the complete original update text when it is recoverable.
- If an old verbatim transcript was never persisted, do **not** call a later English/curated reconstruction “exact raw”. Keep the historical reconstruction for provenance and expose a clearly labelled recovered Chinese reading version separately.
- Every future scheduled update must follow: `Chinese ChatGPT output → exact raw snapshot → translation/curation → Living data → Pages`.

## Historical provenance

| Run | Canonical/historical file | Status |
|---|---|---|
| 2026-08-08 Test #3 · Resource Model R2 | `2026-08-08-test-3-r2.raw.md` | Historical archive was not the verbatim Chinese transcript; Pages provides a clearly labelled Chinese recovered reading version. |
| 2026-08-08 Test #3 | `2026-08-08-test-3.raw.md` | Historical Git archive is an English reconstruction; Pages now defaults to a clearly labelled Chinese recovered reading version and keeps English separate. |
| 2026-08-08 Test #2 | `2026-08-08-test-2.raw.md` | Exact chat transcript was not persisted; Pages explicitly labels the Chinese recovery instead of claiming verbatim origin. |
| 2026-08-08 Test #1 | `2026-08-08-test-1.raw.md` | Chinese raw text is available; preserve it as the primary reading view. |

## Pages behaviour

- Raw archive pages default to Chinese.
- The site-wide language toggle switches to an English reading view when one exists; a derived English reading version is never presented as the canonical raw transcript.
- Each raw page may show a separate **Related References / 关联资料与来源** section derived from run metadata.

GitHub Pages archive: `/kmd_owner_direction/raw-updates.html`
