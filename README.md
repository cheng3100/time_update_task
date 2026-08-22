# time_update_task

Long-term archive for scheduled task outputs. Each scheduled task lives in its own subdirectory and has an independent GitHub Pages view.

## Repository-wide rules

All scheduled tasks follow the shared behavior and archival rules in [`UPDATE_RULES.md`](UPDATE_RULES.md).

Task-specific subdirectories should only add domain-specific taxonomy, priorities, report sections and research sources.

## GitHub Pages architecture

The published site is **Jekyll-only**. There is no parallel static `docs/` site.

```text
_config.yml                 Jekyll site configuration
_data/                      structured stable/living/history data
_layouts/                   shared page layouts
_includes/                  reusable Jekyll UI components
assets/css/                 site/theme styles
assets/js/                  shared progressive UI behavior
pages/*.page.md             explicit Jekyll page shells + permalinks
index.md                    repository Pages home
kmd_owner_direction/        canonical task archives/source-of-truth
scripts/generate_archive_pages.py
                             build adapter for immutable archive Markdown
_generated/                 build-only Jekyll collection (not canonical source)
_site/                      final GitHub Pages artifact
```

### Source-of-truth boundary

- `kmd_owner_direction/**/*.archive.md`, `*.resource.md`, `*.raw.md`, and `*.update.md` are canonical archival content.
- canonical archive files are not published directly by path and are not rewritten just to satisfy presentation needs.
- `scripts/generate_archive_pages.py` creates build-only documents in the `_generated` Jekyll collection, adding front matter/permalinks while preserving canonical archive bodies.
- layouts, navigation, language switching, theme styling, and final URLs are controlled by Jekyll.
- shared UI must live in `_layouts`, `_includes`, or `assets`; do not add standalone static HTML/JS page trees.

### Presentation rules

- use `relative_url` for internal links so project Pages baseurl remains correct;
- reuse `_includes/kmd-nav.html` for KMD navigation rather than copying tab markup;
- use `assets/js/site.js` for shared language behavior rather than page-local scripts;
- stable definitions live in stable `_data` sources; scheduled Living updates/history must not rewrite stable taxonomy by accident.
