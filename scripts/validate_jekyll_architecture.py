#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

# Legacy parallel static-site trees must never return.
for legacy in (
    ROOT / "docs",
    ROOT / "generated_archive_pages",
):
    if legacy.exists():
        errors.append(f"legacy/non-Jekyll presentation path exists: {legacy.relative_to(ROOT)}")

legacy_names = {"topic.html", "topic-view.js", "site.css"}
for path in ROOT.rglob("*"):
    if path.is_file() and path.name in legacy_names and "_site" not in path.parts:
        errors.append(f"legacy static frontend artifact exists: {path.relative_to(ROOT)}")


def front_matter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end]


def fm_value(fm: str, key: str) -> str | None:
    m = re.search(rf"(?m)^\s*{re.escape(key)}:\s*[\"']?([^\n\"']+)[\"']?\s*$", fm)
    return m.group(1).strip() if m else None

# Explicit page shells must be real Jekyll pages.
for path in sorted((ROOT / "pages").glob("*.page.md")):
    text = path.read_text(encoding="utf-8")
    fm = front_matter(text)
    if fm is None:
        errors.append(f"missing YAML front matter: {path.relative_to(ROOT)}")
        continue
    if not fm_value(fm, "layout"):
        errors.append(f"missing layout in front matter: {path.relative_to(ROOT)}")
    if not fm_value(fm, "permalink"):
        errors.append(f"missing explicit permalink: {path.relative_to(ROOT)}")

# Detect collisions across normal Jekyll pages and build-generated collection docs.
permalinks: dict[str, list[str]] = {}
for base in (ROOT / "pages", ROOT / "_generated"):
    if not base.exists():
        continue
    for path in sorted(base.rglob("*.md")):
        fm = front_matter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        permalink = fm_value(fm, "permalink")
        if permalink:
            permalinks.setdefault(permalink, []).append(str(path.relative_to(ROOT)))

for permalink, paths in permalinks.items():
    if len(paths) > 1:
        errors.append(f"duplicate permalink {permalink}: {', '.join(paths)}")

# Shared KMD navigation should be componentized, not copied into pages/layouts.
nav_markup = '<nav class="nav-tabs"'
for base in (ROOT / "pages", ROOT / "_layouts"):
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".html"}:
            continue
        if path.name == "kmd-nav.html":
            continue
        if nav_markup in path.read_text(encoding="utf-8"):
            errors.append(f"copied KMD nav markup instead of include: {path.relative_to(ROOT)}")

if errors:
    print("Jekyll architecture validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Jekyll architecture validation passed; {len(permalinks)} explicit permalinks are unique.")
