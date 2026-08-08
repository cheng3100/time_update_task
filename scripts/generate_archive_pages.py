#!/usr/bin/env python3
from pathlib import Path
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated_archive_pages"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1)
    return fallback


def linkify_bare_urls(text: str) -> str:
    """Make bare http(s) URLs clickable without changing archive source files.

    Kramdown does not reliably autolink a URL that appears after labels such as
    `- **链接:** https://...`.  Generated Pages therefore normalize bare URLs to
    Markdown autolinks (`<https://...>`). Existing Markdown links/autolinks are
    left untouched.
    """
    url_re = re.compile(r"(?<!\()(?<!<)(https?://[^\s<>]+)")

    def repl(match: re.Match) -> str:
        url = match.group(1)
        trailing = ""
        while url and url[-1] in ".,;:!?，。；：！？":
            trailing = url[-1] + trailing
            url = url[:-1]
        return f"<{url}>{trailing}"

    return url_re.sub(repl, text)


def emit(source: Path, permalink: str, back_url: str, back_zh: str, back_en: str) -> None:
    text = source.read_text(encoding="utf-8")
    title = first_heading(text, source.name)
    target = OUT / permalink.lstrip("/")
    target = target.with_suffix(".md")
    target.parent.mkdir(parents=True, exist_ok=True)
    front = "\n".join([
        "---",
        "layout: default",
        f"title: {yaml_string(title)}",
        f"hero_title: {yaml_string(title)}",
        f"permalink: {yaml_string(permalink)}",
        f"back_url: {yaml_string(back_url)}",
        f"back_zh: {yaml_string(back_zh)}",
        f"back_en: {yaml_string(back_en)}",
        "---",
        "",
    ])
    target.write_text(front + linkify_bare_urls(text), encoding="utf-8")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    # Durable learning resources: keep source archives untouched, render wrappers.
    resource_root = ROOT / "kmd_owner_direction" / "resources"
    for source in sorted(resource_root.rglob("*.resource.md")):
        rel = source.relative_to(resource_root)
        stem = source.name.removesuffix(".resource.md")
        if len(rel.parts) >= 2:
            owner = rel.parts[0]
            permalink = f"/kmd_owner_direction/resources/{owner}/{stem}.html"
            back_url = f"/kmd_owner_direction/owners/{owner}.html"
            back_zh = "返回 Owner 页面"
            back_en = "Back to Owner"
        else:
            permalink = f"/kmd_owner_direction/resources/{stem}.html"
            back_url = "/kmd_owner_direction/resources.html"
            back_zh = "长期资料总索引"
            back_en = "Learning Resources"
        emit(source, permalink, back_url, back_zh, back_en)

    # Complete raw snapshots.
    raw_root = ROOT / "kmd_owner_direction" / "raw_updates"
    for source in sorted(raw_root.glob("*.raw.md")):
        stem = source.name.removesuffix(".raw.md")
        emit(
            source,
            f"/kmd_owner_direction/raw_updates/{stem}.html",
            "/kmd_owner_direction/raw-updates.html",
            "原始更新归档",
            "Raw Update Archive",
        )

    # Curated dated updates.
    update_root = ROOT / "kmd_owner_direction" / "updates"
    for source in sorted(update_root.glob("*.update.md")):
        stem = source.name.removesuffix(".update.md")
        emit(
            source,
            f"/kmd_owner_direction/updates/{stem}.html",
            "/kmd_owner_direction/",
            "GPU KMD Owner 主页",
            "GPU KMD Owner Home",
        )

    count = len(list(OUT.rglob("*.md")))
    print(f"Generated {count} archive page wrappers under {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
