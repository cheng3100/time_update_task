#!/usr/bin/env python3
from pathlib import Path
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_generated"
HISTORY_PATH = ROOT / "_data" / "kmd_history.json"
RECENT_HISTORY_PATH = ROOT / "_data" / "kmd_recent_history.json"
RAW_PROVENANCE_PATH = ROOT / "_data" / "kmd_raw_provenance.json"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1)
    return fallback


def linkify_bare_urls(text: str) -> str:
    url_re = re.compile(r"(?<!\()(?<!<)(https?://[^\s<>]+)")

    def repl(match: re.Match) -> str:
        url = match.group(1)
        trailing = ""
        while url and url[-1] in ".,;:!?，。；：！？":
            trailing = url[-1] + trailing
            url = url[:-1]
        return f"<{url}>{trailing}"

    return url_re.sub(repl, text)


def front_matter(title: str, permalink: str, back_url: str, back_zh: str, back_en: str,
                 subtitle_zh: str = "", subtitle_en: str = "") -> str:
    rows = [
        "---",
        "layout: default",
        f"title: {yaml_string(title)}",
        f"permalink: {yaml_string(permalink)}",
        f"back_url: {yaml_string(back_url)}",
        f"back_zh: {yaml_string(back_zh)}",
        f"back_en: {yaml_string(back_en)}",
    ]
    if subtitle_zh:
        rows.append(f"hero_subtitle_zh: {yaml_string(subtitle_zh)}")
    if subtitle_en:
        rows.append(f"hero_subtitle_en: {yaml_string(subtitle_en)}")
    rows += ["---", ""]
    return "\n".join(rows)


def write_page(permalink: str, text: str) -> None:
    target = OUT / permalink.lstrip("/")
    target = target.with_suffix(".md")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def liquid_href(url: str) -> str:
    if url.startswith("/"):
        escaped = url.replace("'", "\\'")
        return "{{ '" + escaped + "' | relative_url }}"
    return url


def render_highlights(run: dict, lang: str) -> str:
    highlights = run.get("highlights", [])
    if not highlights:
        return ""
    title_key = f"title_{lang}"
    body_key = f"body_{lang}"
    out = []
    for i, item in enumerate(highlights):
        title = item.get(title_key) or item.get("title_zh") or "Update"
        body = item.get(body_key) or item.get("body_zh") or ""
        href = liquid_href(item.get("url", "#"))
        label = "本期最有价值更新" if lang == "zh" and i == 0 else (
            "Most Valuable Update" if lang == "en" and i == 0 else ""
        )
        if label:
            out.append(f"## {label}\n")
        elif i == 1:
            out.append("## 其他关键更新\n" if lang == "zh" else "## Other Key Updates\n")
        out.append(f"### [{title}]({href})\n")
        if body:
            out.append(body + "\n")
        if lang == "zh":
            out.append("**为何值得关注：** 这一条影响当前 KMD feature 的接口、生命周期、数据模型或后续演进边界。\n")
        else:
            out.append("**Why it matters:** This item affects current KMD feature interfaces, lifetimes, data models, or future evolution boundaries.\n")
    return "\n".join(out)


def render_related_links(run: dict, lang: str) -> str:
    highlights = run.get("highlights", [])
    if not highlights:
        return ""
    title_key = f"title_{lang}"
    heading = "## 关联资料与来源" if lang == "zh" else "## Related References"
    rows = [heading, ""]
    seen = set()
    for item in highlights:
        url = item.get("url")
        if not url or url in seen:
            continue
        seen.add(url)
        title = item.get(title_key) or item.get("title_zh") or url
        rows.append(f"- [{title}]({liquid_href(url)})")
    return "\n".join(rows) + "\n"


def load_history() -> tuple[list[dict], dict[str, dict], dict[str, dict]]:
    runs = []
    for path in (RECENT_HISTORY_PATH, HISTORY_PATH):
        if path.exists():
            runs.extend(json.loads(path.read_text(encoding="utf-8")).get("runs", []))
    by_raw = {}
    by_curated = {}
    for run in runs:
        raw = run.get("raw", "")
        curated = run.get("curated", "")
        if raw:
            by_raw[Path(raw).stem] = run
        if curated:
            by_curated[Path(curated).stem] = run
    return runs, by_raw, by_curated


def load_raw_provenance() -> dict[str, dict]:
    if not RAW_PROVENANCE_PATH.exists():
        return {}
    return json.loads(RAW_PROVENANCE_PATH.read_text(encoding="utf-8"))


def emit_generic(source: Path, permalink: str, back_url: str, back_zh: str, back_en: str) -> None:
    text = source.read_text(encoding="utf-8")
    title = first_heading(text, source.name)
    page = front_matter(title, permalink, back_url, back_zh, back_en)
    page += linkify_bare_urls(text)
    write_page(permalink, page)


def emit_raw(source: Path, stem: str, run: dict | None, provenance: dict[str, dict]) -> None:
    source_text = source.read_text(encoding="utf-8")
    recovered = ROOT / "kmd_owner_direction" / "raw_recovered_zh" / f"{stem}.zh.md"
    prov = provenance.get(stem, {})
    status = prov.get("status", "unverified")
    label_zh = prov.get("label_zh", "历史 raw（未验证逐字一致）")
    label_en = prov.get("label_en", "Historical raw (verbatim equality unverified)")
    detail_zh = prov.get("detail_zh", "该历史文件未经过聊天 transcript 的独立逐字校验。")
    detail_en = prov.get("detail_en", "This historical file has not been independently verified against the chat transcript.")

    if recovered.exists():
        zh_text = recovered.read_text(encoding="utf-8")
        en_text = source_text
    elif status == "mismatch":
        # Never pretend an English reconstruction is the Chinese original.
        zh_text = (
            "# 本期真实聊天原文未能从当前归档中恢复\n\n"
            "仓库中的历史文件不是本期实际中文聊天输出。为避免继续把重构内容冒充 raw，"
            "此处不生成伪造的中文原文。下面的英文页仅展示当时错误写入 Git 的历史归档记录。\n"
        )
        en_text = source_text
    else:
        zh_text = source_text
        curated_url = (run or {}).get("curated", "/kmd_owner_direction/")
        en_text = (
            "# English reading note\n\n"
            "A complete English translation was not archived. The Chinese view shows the available historical record. "
            "For a structured English reading version, open the curated update:\n\n"
            f"[{curated_url}]({liquid_href(curated_url)})\n"
        )

    title = first_heading(zh_text, first_heading(source_text, source.name))
    permalink = f"/kmd_owner_direction/raw_updates/{stem}.html"
    page = front_matter(
        title, permalink, "/kmd_owner_direction/raw-updates.html",
        "Raw Update Archive", "Raw Update Archive", label_zh, label_en,
    )
    page += '<section class="archive-provenance">\n'
    page += f'<p><strong><span class="lang zh">归档状态：</span><span class="lang en">Archive status: </span></strong><span class="lang zh">{label_zh}</span><span class="lang en">{label_en}</span></p>\n'
    page += f'<p class="lang zh">{detail_zh}</p>\n<p class="lang en">{detail_en}</p>\n</section>\n\n'

    page += '<div class="lang zh archive-language-body" markdown="1">\n\n'
    page += linkify_bare_urls(zh_text) + "\n\n"
    if run:
        page += render_related_links(run, "zh")
    page += "\n</div>\n\n"

    page += '<div class="lang en archive-language-body" markdown="1">\n\n'
    page += linkify_bare_urls(en_text) + "\n\n"
    if run:
        page += render_related_links(run, "en")
    page += "\n</div>\n"
    write_page(permalink, page)


def emit_curated(source: Path, stem: str, run: dict | None) -> None:
    source_text = source.read_text(encoding="utf-8")
    title = first_heading(source_text, source.name)
    permalink = f"/kmd_owner_direction/updates/{stem}.html"
    page = front_matter(
        title, permalink, "/kmd_owner_direction/",
        "GPU KMD Owner 主页", "GPU KMD Owner Home",
        "每期摘要按“最有价值更新 → 关键更新 → 完整结构化正文”组织，并直接提供来源链接。",
        "Each run is organized as Most Valuable Update → Key Updates → full structured archive, with direct references.",
    )

    if run:
        page += '<div class="lang zh run-summary" markdown="1">\n\n'
        intro = run.get("intro_zh", "")
        if intro:
            page += "## 本期摘要\n\n" + intro + "\n\n"
        page += render_highlights(run, "zh")
        page += f"\n## 归档入口\n\n- [查看该期归档记录]({liquid_href(run.get('raw', '/kmd_owner_direction/raw-updates.html'))})\n"
        page += "\n</div>\n\n"

        page += '<div class="lang en run-summary" markdown="1">\n\n'
        intro = run.get("intro_en", "")
        if intro:
            page += "## Run Summary\n\n" + intro + "\n\n"
        page += render_highlights(run, "en")
        page += f"\n## Archive Entry\n\n- [Open this run archive record]({liquid_href(run.get('raw', '/kmd_owner_direction/raw-updates.html'))})\n"
        page += "\n</div>\n\n"

    page += '<div class="lang en structured-source" markdown="1">\n\n'
    page += "## Full Structured Archive\n\n" + linkify_bare_urls(source_text) + "\n\n</div>\n"
    write_page(permalink, page)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)

    _, history_by_raw, history_by_curated = load_history()
    provenance = load_raw_provenance()

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
        emit_generic(source, permalink, back_url, back_zh, back_en)

    raw_root = ROOT / "kmd_owner_direction" / "raw_updates"
    for source in sorted(raw_root.glob("*.raw.md")):
        stem = source.name.removesuffix(".raw.md")
        emit_raw(source, stem, history_by_raw.get(stem), provenance)

    update_root = ROOT / "kmd_owner_direction" / "updates"
    for source in sorted(update_root.glob("*.update.md")):
        stem = source.name.removesuffix(".update.md")
        emit_curated(source, stem, history_by_curated.get(stem))

    count = len(list(OUT.rglob("*.md")))
    print(f"Generated {count} Jekyll collection documents under {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
