# GPU KMD Owner Direction — Raw Update Archive

This directory stores the **per-run chat report snapshots** separately from the curated `updates/` summaries and the stable `owners/` roadmap files.

## Canonical raw invariant

For every future run there must be one canonical report body, conceptually `REPORT_BODY`:

```text
research / compose
      ↓
freeze REPORT_BODY (Chinese for this task)
      ├── send the same REPORT_BODY to ChatGPT conversation
      └── write the same REPORT_BODY to *.raw.md
                    ↓
          only then derive curated / Living / translation
```

The report body in chat and in `*.raw.md` must not be independently regenerated.

Forbidden raw transformations:
- summary or compression;
- Chinese→English translation;
- heading/section restructuring;
- deleting detailed explanation or source links;
- rebuilding raw from a curated update or `_data`;
- calling a reconstruction or translation “original/raw/verbatim”.

## Archive policy

- One `*.raw.md` file per scheduled/test run.
- **The canonical raw language is the language actually emitted by ChatGPT. For this task that is Chinese by default.**
- The raw snapshot must be frozen before translation, summarization, restructuring, Pages rendering, Owner/Living updates or resource curation.
- Raw files are append-only historical evidence. If a historical raw file is discovered to be wrong, preserve provenance and mark it as mismatch/unverified; do not silently rewrite history and pretend it was the original transcript.
- Source/reference links that appeared in the ChatGPT output belong in canonical raw. Additional archive-only references may be displayed separately by Pages but are not part of the original report body.
- `owners/*.archive.md` contains stable Owner definitions and long-term roadmaps.
- `updates/*.update.md` contains structured/curated dated summaries.
- `raw_updates/*.raw.md` is canonical raw **only when provenance is verified**.

## Historical provenance audit

| Run | File | Provenance status |
|---|---|---|
| 2026-08-22 Weekly #2 | `2026-08-22-weekly-2.raw.md` | **Mismatch confirmed.** File is an English compressed/reconstructed report while the task requires a complete Chinese chat report. It must not be labelled exact/original raw. |
| 2026-08-15 Weekly #1 | `2026-08-15-weekly-1.raw.md` | Chinese full-length report exists, but byte-for-byte equality with the historical chat transcript has not been independently verified from repository data alone. Mark as **unverified historical raw**, not proven verbatim. |
| 2026-08-08 Test #3 · Resource Model R2 | `2026-08-08-test-3-r2.raw.md` | Historical archive was not the verbatim Chinese transcript; Pages provides a clearly labelled recovered reading version. |
| 2026-08-08 Test #3 | `2026-08-08-test-3.raw.md` | Historical Git archive is an English reconstruction; not canonical raw. |
| 2026-08-08 Test #2 | `2026-08-08-test-2.raw.md` | Exact chat transcript was not persisted; not canonical raw. |
| 2026-08-08 Test #1 | `2026-08-08-test-1.raw.md` | Chinese historical report exists; preserve it, but do not claim byte-identical provenance without independent verification. |

## Pages behaviour

- Raw archive pages default to Chinese where a verified/recovered Chinese reading body exists.
- Pages must display provenance status explicitly: **Verified raw / Unverified historical raw / Mismatch or reconstruction**.
- An English reconstruction must never be shown under a Chinese `原始输出` label.
- A recovered/translated reading version is a separate derived view, never canonical raw.
- Related references may be rendered separately from raw body.

GitHub Pages archive: `/kmd_owner_direction/raw-updates.html`
