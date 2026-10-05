#!/usr/bin/env python3
"""Structural HTML QA; does not verify facts or replace browser inspection."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

REQUIRED_PHRASES = ("Executive Summary", "Sources & Reliability", "GTM", "Conversion", "Positioning")
UNFINISHED = re.compile(
    r"\b(?:TODO|TBD|PLACEHOLDER|YYYY-MM-DD)\b|\{\{[^}]+\}\}|"
    r"补充真实内容|建议核心定位：……|关键指标\s*\d|这里必须是判断|"
    r"用 1[–-]2 句话解释|\[A\] 官方来源", re.I)


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags, self.ids, self.duplicate_ids = [], set(), set()
        self.text, self.css = [], []
        self.current_style, self.hidden = False, 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                self.duplicate_ids.add(attrs["id"])
            self.ids.add(attrs["id"])
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "style":
            self.current_style = True

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)
        if tag == "style":
            self.current_style = False

    def handle_data(self, data):
        if self.current_style:
            self.css.append(data)
        if not self.hidden:
            self.text.append(data)


def validate(path: Path, allow_scaffold=False):
    errors, warnings = [], []
    try:
        text = path.read_bytes().decode("utf-8-sig")
    except UnicodeDecodeError:
        return ["File is not UTF-8"], []
    except OSError as exc:
        return [f"Cannot read file: {exc}"], []
    doc = Document()
    doc.feed(text)
    css = "\n".join(doc.css) + "\n" + "\n".join(a.get("style", "") for _, a in doc.tags)
    visible = " ".join(doc.text)
    metas = [a for t, a in doc.tags if t == "meta"]
    if not any(a.get("charset", "").lower() == "utf-8" for a in metas):
        errors.append("Missing UTF-8 charset meta tag")
    if not any(a.get("name", "").lower() == "viewport" for a in metas):
        errors.append("Missing viewport meta tag")
    if not doc.css:
        errors.append("Missing inline CSS")
    if not re.search(r"position\s*:\s*sticky", css, re.I):
        errors.append("Sticky navigation not detected")
    if not re.search(r"@media\s+print", css, re.I):
        errors.append("Missing print stylesheet")
    if not re.search(r"@media[^{}]*\(\s*max-width\s*:", css, re.I):
        errors.append("Responsive media query not detected")
    if not any(t == "nav" for t, _ in doc.tags):
        errors.append("Missing navigation element")
    for tag, attrs in doc.tags:
        if tag == "link" and "stylesheet" in attrs.get("rel", "").lower().split():
            errors.append("Non-inline stylesheet dependency detected")
        if tag == "script" and "src" in attrs:
            errors.append("Non-inline script dependency detected")
        if tag in ("img", "source", "video", "audio", "iframe", "embed", "object", "image", "use"):
            for attr in ("src", "srcset", "poster", "data", "href", "xlink:href"):
                value = attrs.get(attr, "").strip()
                if value and not value.lower().startswith(("data:", "#")):
                    errors.append(f"Non-embedded {tag} resource detected ({attr})")
        if tag == "a" and attrs.get("href", "").startswith("#"):
            anchor = attrs["href"][1:]
            if anchor and anchor not in doc.ids:
                errors.append(f"Broken navigation anchor: #{anchor}")
    if re.search(r"@import\b", css, re.I):
        errors.append("CSS import dependency detected")
    for value in re.findall(r"url\(\s*['\"]?([^)'\"]+)", css, re.I):
        if not value.strip().lower().startswith(("data:", "#")):
            errors.append("Non-embedded CSS resource detected")
    if doc.duplicate_ids:
        errors.append("Duplicate HTML id(s): " + ", ".join(sorted(doc.duplicate_ids)))
    scaffold = any(a.get("name") == "competitive-report-stage" and a.get("content") == "scaffold" for a in metas)
    if scaffold or UNFINISHED.search(visible):
        (warnings if allow_scaffold else errors).append("Unfinished scaffold content detected")
    if re.search(r"\{\{[^}]+\}\}", text):
        (warnings if allow_scaffold else errors).append("Unresolved template token detected")
    sections = sum(t == "section" for t, _ in doc.tags)
    if sections < 10:
        errors.append(f"Too few report sections: {sections} (need >=10)")
    sources = sum(t == "a" and a.get("href", "").lower().startswith(("http://", "https://")) for t, a in doc.tags)
    if sources < 5:
        warnings.append(f"Only {sources} clickable source URL(s); review evidence coverage without padding")
    for phrase in REQUIRED_PHRASES:
        if phrase.lower() not in visible.lower():
            errors.append(f"Required report concept missing: {phrase}")
    if not re.search(r"\b[A-C]\b", visible):
        warnings.append("A/B/C source grading not clearly detected")
    if not re.search(r"研究边界|免责声明|边界|caveat", visible, re.I):
        warnings.append("Research boundary/caveat not clearly detected")
    if "window.print" not in text:
        errors.append("Print/export affordance not detected")
    return list(dict.fromkeys(errors)), list(dict.fromkeys(warnings))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--allow-scaffold", action="store_true", help="Draft QA only; never use for delivery")
    args = parser.parse_args()
    errors, warnings = validate(args.report, args.allow_scaffold)
    for item in errors:
        print("ERROR:", item)
    for item in warnings:
        print("WARN:", item)
    print(f"RESULT: {len(errors)} error(s), {len(warnings)} warning(s)")
    if args.allow_scaffold:
        print("DRAFT CHECK ONLY: this result does not certify a completed report")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
