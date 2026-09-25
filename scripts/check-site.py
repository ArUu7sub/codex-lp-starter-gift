#!/usr/bin/env python3
"""Dependency-free checks for the Codex LP Starter v2 static prototype."""

from __future__ import annotations

import hashlib
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ZIP = ROOT / "assets" / "codex-lp-starter-v2.0.2.zip"
EXPECTED_SIZE = 21274
EXPECTED_SHA256 = "315e9b19e44377c10054299d215b288b1a7d061776b800fc0894f0639be368e1"
EXPECTED_LOGO_SHA256 = "8d65d237cc9ab1642fd574f331c182a233e84fa6110d2311e8c1db3a0adcead2"
EXPECTED_ZIP_FILES = {
    "codex-lp-starter/CHANGELOG.md",
    "codex-lp-starter/README.md",
    "codex-lp-starter/SKILL.md",
    "codex-lp-starter/VERSION",
    "codex-lp-starter/agents/openai.yaml",
    "codex-lp-starter/assets/lp実装.md",
    "codex-lp-starter/assets/セットアップ.md",
    "codex-lp-starter/references/lp-quality-checklist.md",
}
HTML_FILES = [
    ROOT / "index.html",
    ROOT / "help" / "index.html",
    ROOT / "changelog" / "index.html",
    ROOT / "privacy" / "index.html",
    ROOT / "404.html",
]
MARKDOWN_FILES = [
    ROOT / "assets" / "セットアップ.md",
    ROOT / "assets" / "lp実装.md",
]
REQUIRED_FILES = HTML_FILES + MARKDOWN_FILES + [
    ROOT / "assets" / "styles.css",
    ROOT / "assets" / "site.js",
    ROOT / "assets" / "codex-ai-creator-logo.png",
    EXPECTED_ZIP,
    ROOT / "README.md",
]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.lang = ""
        self.has_viewport = False
        self.has_icon = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        if tag == "html":
            self.lang = values.get("lang") or ""
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "link" and "icon" in (values.get("rel") or "").split():
            self.has_icon = True
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.links.append((attribute, value))


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def relative_luminance(hex_color: str) -> float:
    channels = []
    for offset in (1, 3, 5):
        channel = int(hex_color[offset : offset + 2], 16) / 255
        channels.append(
            channel / 12.92
            if channel <= 0.04045
            else ((channel + 0.055) / 1.055) ** 2.4
        )
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast_ratio(first: str, second: str) -> float:
    first_luminance = relative_luminance(first)
    second_luminance = relative_luminance(second)
    lighter = max(first_luminance, second_luminance)
    darker = min(first_luminance, second_luminance)
    return (lighter + 0.05) / (darker + 0.05)


def local_target(source: Path, raw_url: str) -> tuple[Path, str] | None:
    parsed = urlsplit(raw_url)
    if parsed.scheme in {"http", "https", "mailto", "tel", "data"} or raw_url.startswith("//"):
        return None
    path_part = unquote(parsed.path)
    if path_part.startswith("/"):
        target = ROOT / path_part.lstrip("/")
    elif path_part:
        target = source.parent / path_part
    else:
        target = source
    target = target.resolve()
    if target.is_dir() or path_part.endswith("/"):
        target = target / "index.html"
    return target, unquote(parsed.fragment)


def parse_page(path: Path, failures: list[str]) -> PageParser:
    parser = PageParser()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
    except Exception as error:
        fail(f"{path.relative_to(ROOT)} could not be parsed: {error}", failures)
    return parser


def main() -> int:
    failures: list[str] = []
    parsed_pages: dict[Path, PageParser] = {}

    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)

    if failures:
        return 1

    actual_size = EXPECTED_ZIP.stat().st_size
    actual_sha256 = hashlib.sha256(EXPECTED_ZIP.read_bytes()).hexdigest()
    if actual_size != EXPECTED_SIZE:
        fail(f"artifact size {actual_size} != {EXPECTED_SIZE}", failures)
    else:
        print(f"PASS: artifact size = {actual_size} bytes")
    if actual_sha256 != EXPECTED_SHA256:
        fail(f"artifact SHA-256 {actual_sha256} != expected value", failures)
    else:
        print(f"PASS: artifact SHA-256 = {actual_sha256}")

    with ZipFile(EXPECTED_ZIP) as archive:
        actual_zip_files = {name for name in archive.namelist() if not name.endswith("/")}
        if actual_zip_files != EXPECTED_ZIP_FILES:
            fail("artifact contents do not match the published file list", failures)
        else:
            print(f"PASS: artifact contains {len(EXPECTED_ZIP_FILES)} published files")

        for markdown in MARKDOWN_FILES:
            archive_name = f"codex-lp-starter/assets/{markdown.name}"
            if archive.read(archive_name) != markdown.read_bytes():
                fail(f"{markdown.name} differs between site asset and ZIP", failures)
            else:
                print(f"PASS: {markdown.name} matches ZIP content")

    logo = ROOT / "assets" / "codex-ai-creator-logo.png"
    actual_logo_sha256 = hashlib.sha256(logo.read_bytes()).hexdigest()
    if actual_logo_sha256 != EXPECTED_LOGO_SHA256:
        fail("brand logo hash differs from the supplied master", failures)
    else:
        print(f"PASS: brand logo SHA-256 = {actual_logo_sha256}")

    for page in HTML_FILES:
        parser = parse_page(page, failures)
        parsed_pages[page.resolve()] = parser
        relative = page.relative_to(ROOT)
        if parser.lang != "ja":
            fail(f"{relative}: html lang must be ja", failures)
        if not parser.has_viewport:
            fail(f"{relative}: viewport meta is missing", failures)
        if not parser.has_icon:
            fail(f"{relative}: favicon link is missing", failures)

    for source, parser in tuple(parsed_pages.items()):
        for attribute, raw_url in parser.links:
            resolved = local_target(source, raw_url)
            if resolved is None:
                continue
            target, fragment = resolved
            if not target.is_file():
                fail(f"{source.relative_to(ROOT)}: broken {attribute}={raw_url!r}", failures)
                continue
            if fragment and target.suffix.lower() in {".html", ".htm"}:
                target_parser = parsed_pages.get(target.resolve())
                if target_parser is None:
                    target_parser = parse_page(target, failures)
                    parsed_pages[target.resolve()] = target_parser
                if fragment not in target_parser.ids:
                    fail(
                        f"{source.relative_to(ROOT)}: missing fragment #{fragment} in "
                        f"{target.relative_to(ROOT)}",
                        failures,
                    )

    index_text = (ROOT / "index.html").read_text(encoding="utf-8")
    required_copy = [
        "2つの制作ファイルを受け取る",
        "セットアップ.mdをダウンロード",
        "セットアップ.mdをコピー",
        "lp実装.mdをダウンロード",
        "lp実装.mdをコピー",
        "Skillの設置や5項目の一括入力は不要です",
        "「AIっぽい装飾」ではなく、案件の中身から決める",
        "JavaScriptが無効でもダウンロードできます",
        EXPECTED_SHA256,
        f"{EXPECTED_SIZE} bytes",
    ]
    for text in required_copy:
        if text not in index_text:
            fail(f"index.html: required copy missing: {text}", failures)

    workflow_start = index_text.find('<ol class="steps workflow-steps">')
    workflow_end = index_text.find("</ol>", workflow_start)
    workflow_markup = index_text[workflow_start:workflow_end]
    if workflow_start < 0 or workflow_end < 0:
        fail("index.html: workflow list is missing", failures)
    elif workflow_markup.count("<li>") != 6:
        fail("index.html: public workflow must contain exactly 6 steps", failures)
    else:
        print("PASS: public workflow contains exactly 6 steps")
    for text in (
        "対話ヒアリング",
        "HTML/CSS/JSをレスポンシブ実装",
        "明示承認することが次の段階へ進む必須条件",
    ):
        if text not in workflow_markup:
            fail(f"index.html: six-step workflow marker missing: {text}", failures)
    if "<h3>プランを承認</h3>" in workflow_markup:
        fail("index.html: approval gate must not be a separate seventh step", failures)

    forbidden_primary_flow = [
        "Codex用Skillを取得する",
        "Skillをダウンロード",
        "5項目の依頼テンプレートをコピー",
        "Skillフォルダへ配置",
    ]
    for text in forbidden_primary_flow:
        if text in index_text:
            fail(f"legacy primary-flow copy found: {text}", failures)

    forbidden_promises = [
        "売れるLP",
        "一発で完成",
        "完全自動",
        "修正不要",
        "全環境対応",
        "ワンクリック設置",
    ]
    all_html_text = "\n".join(page.read_text(encoding="utf-8") for page in HTML_FILES)
    for text in forbidden_promises:
        if text in all_html_text:
            fail(f"forbidden promise found: {text}", failures)

    if "ZIP_SIZE_PLACEHOLDER" in all_html_text or "ZIP_SHA_PLACEHOLDER" in all_html_text:
        fail("artifact placeholder remains in HTML", failures)

    css_text = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    for rule in (
        "min-width: 20rem",
        "body :focus-visible",
        "--focus-inner: #ffffff",
        "--focus-outer: #7a1748",
        "outline: 0.1875rem solid var(--focus-outer)",
        "outline-offset: 0.1875rem",
        "box-shadow: 0 0 0 0.1875rem var(--focus-inner)",
        "prefers-reduced-motion",
        ".workflow-steps",
        ".file-grid",
        ".file-card",
        "max-width: 100%",
        ".site-footer .fine-print",
    ):
        if rule not in css_text:
            fail(f"styles.css: required responsive/accessibility rule missing: {rule}", failures)

    focus_contrast_pairs = {
        "outer ring on white": ("#7a1748", "#ffffff"),
        "outer ring on soft surface": ("#7a1748", "#f2f8fd"),
        "outer ring on warning surface": ("#7a1748", "#fff8e6"),
        "inner ring on navy header": ("#ffffff", "#0b1b35"),
        "inner ring on darkest section": ("#ffffff", "#061126"),
        "inner ring on code surface": ("#ffffff", "#07162c"),
    }
    for label, colors in focus_contrast_pairs.items():
        ratio = contrast_ratio(*colors)
        if ratio < 3:
            fail(f"focus contrast below 3:1 for {label}: {ratio:.2f}:1", failures)
        else:
            print(f"PASS: focus contrast {label} = {ratio:.2f}:1")

    script_text = (ROOT / "assets" / "site.js").read_text(encoding="utf-8")
    for behavior in (
        "data-copy-url",
        "codex_lp_file_copy",
        "codex_lp_copy_failure",
        "codex_lp_package_download",
        "setStatus(status",
        'button.setAttribute("aria-busy", "true")',
        'button.removeAttribute("aria-busy")',
        "button.focus({ preventScroll: true })",
    ):
        source_text = index_text if behavior == "data-copy-url" else script_text
        if behavior not in source_text:
            fail(f"required interaction marker missing: {behavior}", failures)
    if "button.disabled = true" in script_text:
        fail("copy button must not be disabled because disabling drops keyboard focus", failures)

    for markdown in MARKDOWN_FILES:
        if not markdown.read_text(encoding="utf-8").strip():
            fail(f"{markdown.name} is empty", failures)

    if failures:
        print(f"\nRESULT: FAIL ({len(failures)} issue(s))")
        return 1

    print(f"PASS: {len(HTML_FILES)} HTML pages parsed")
    print("PASS: all local links, assets, and fragments resolve")
    print("PASS: individual downloads, copy controls, JS-off fallback, and v2 flow markers found")
    print("\nRESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
