#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

# Legacy parallel static-site trees must never return.
for legacy in (ROOT / "docs", ROOT / "generated_archive_pages"):
    if legacy.exists():
        errors.append(f"legacy/non-Jekyll presentation path exists: {legacy.relative_to(ROOT)}")

legacy_names = {"topic.html", "topic-view.js", "site.css"}
for path in ROOT.rglob("*"):
    if path.is_file() and path.name in legacy_names and "_site" not in path.parts:
        errors.append(f"legacy static frontend artifact exists: {path.relative_to(ROOT)}")

config = (ROOT / "_config.yml").read_text(encoding="utf-8")
if "remote_theme: just-the-docs/just-the-docs@v0.12.0" not in config:
    errors.append("Just the Docs v0.12.0 must remain the pinned presentation theme")
if "theme: jekyll-theme-architect" in config:
    errors.append("legacy Architect theme configuration remains")
if (ROOT / "_layouts" / "default.html").exists():
    errors.append("local _layouts/default.html shadows the native Just the Docs default layout")
if (ROOT / "assets" / "css" / "style.scss").exists():
    errors.append("legacy standalone stylesheet remains; use _sass/custom/custom.scss")


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

# Main navigation is owned by Just the Docs. Do not re-introduce a parallel tab bar.
for base in (ROOT / "pages", ROOT / "_layouts", ROOT / "_includes"):
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".html"}:
            continue
        text = path.read_text(encoding="utf-8")
        if 'class="nav-tabs"' in text or "kmd-nav.html" in text:
            errors.append(f"parallel horizontal KMD navigation remains: {path.relative_to(ROOT)}")

if errors:
    print("Jekyll architecture validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Just the Docs architecture validation passed; {len(permalinks)} explicit permalinks are unique.")
