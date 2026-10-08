"""Check an HTML deck against the machine-checkable rules in DESIGN.md.

Standard library only:

    python scripts/check_deck.py path/to/deck.html [--contract path/to/contract.yaml]

Deck markup convention:

- Each slide is an element whose class list contains "slide".
- Optional slide attributes: data-density (LOW | MEDIUM | HIGH),
  data-energy (CALM | FOCUSED | BOLD), data-energy-override (reason, see C14).
- Elements marked data-chrome (eyebrow, footer, nav; see 3.7) are not counted as content.

It also scans the source for offline and theme problems (3.2, 3.5): external resources,
prefers-color-scheme, and Ming or serif faces in font stacks; and for the keyboard
navigation runtime from templates/deck.html (3.7).

Font sizes, overflow, safe margins and contrast need a rendered page and are reported as
NOT CHECKED, so a PASS here is not a visual-quality verdict.
"""

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# C10: hard ceiling and per-density suggested ranges.
CONTENT_MAX = 120
DENSITY_RANGES = {"LOW": (20, 40), "MEDIUM": (40, 80), "HIGH": (80, 120)}
# C14: warn after this many consecutive non-BOLD slides.
BOLD_GAP = 5

# C13: absolutes that need sample size or accuracy behind them.
ABSOLUTES = ["都能", "完全", "一定", "絕對", "百分之百"]
# 3.13: forward-reference sentences.
PREVIEWS = ["接下來會", "接下來將", "後面幾頁", "後面兩頁", "下一頁將"]
DASHES = re.compile(r"—|──")
EMOJI = re.compile("[☀-➿⭐⭕⏩-⏺\U0001F000-\U0001FAFF]")

CJK = re.compile(r"[㐀-䶿一-鿿豈-﫿぀-ヿ]")
WORD = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)*")
NUMBER = re.compile(r"\d+(?:[.,]\d+)*")

# 3.5: offline single file, fixed theme. 3.2: system fonts only, never a Ming or serif face.
EXTERNAL_RESOURCE = re.compile(
    r"<(?:link|script|img|iframe|source|video|audio|embed)\b[^>]*\b(?:src|href)\s*=\s*[\"']\s*(?:https?:)?//"
    r"|@import\b|url\(\s*[\"']?\s*(?:https?:)?//", re.IGNORECASE)
COLOR_SCHEME_QUERY = re.compile(r"prefers-color-scheme", re.IGNORECASE)
STYLE_BLOCK = re.compile(r"<style\b[^>]*>(.*?)</style>|font-family\s*=\s*\"([^\"]*)\"", re.IGNORECASE | re.DOTALL)
# Generic "serif" only as a font name: not sans-serif, a custom property (--serif) or a class (.serif).
MING_OR_SERIF = re.compile(r"MingLiU|PMingLiU|新細明體|細明體|Songti|Serif TC|(?<![-.\w])serif\b", re.IGNORECASE)
COMMENTS = re.compile(r"/\*.*?\*/|<!--.*?-->", re.DOTALL)

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


def text_units(text):
    """C10 units: one per CJK character, English word, or run of digits."""
    return len(CJK.findall(text)) + len(WORD.findall(text)) + len(NUMBER.findall(text))


def banned_phrases(design):
    """Read the banned-phrase list from the '## 禁用詞' block of DESIGN.md 3.13."""
    match = re.search(r"^## 禁用詞\s*\n+(.+)$", design, flags=re.MULTILINE)
    if not match:
        return []
    return [p.strip() for p in match.group(1).rstrip("。").split("、") if p.strip()]


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []
        self.stack = []  # (tag, is_slide, is_hidden)

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        attrs = dict(attrs)
        is_slide = "slide" in (attrs.get("class") or "").split()
        hidden = tag in ("script", "style") or "data-chrome" in attrs
        if is_slide:
            self.slides.append({
                "content": [],
                "density": (attrs.get("data-density") or "").upper(),
                "energy": (attrs.get("data-energy") or "").upper(),
                "override": attrs.get("data-energy-override") or "",
            })
        self.stack.append((tag, is_slide, hidden))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        if not any(is_slide for _, is_slide, _ in self.stack):
            return
        if any(hidden for _, _, hidden in self.stack):
            return
        self.slides[-1]["content"].append(data)


QUALITY_FLOORS = {"C03", "C13"}


def contract_slide_max(path):
    text = Path(path).read_text(encoding="utf-8")
    match = re.search(r"^\s*slide_count_max:\s*(\d+)", text, flags=re.MULTILINE)
    return int(match.group(1)) if match else None


def contract_overrides(path):
    """canon_overrides entries as {id: reason}; an entry without a reason maps to ''."""
    text = Path(path).read_text(encoding="utf-8")
    block = re.search(r"^canon_overrides:[ \t]*\n((?:[ \t]+.*\n?)*)", text, flags=re.MULTILINE)
    if not block:
        return {}
    overrides = {}
    for entry in re.split(r"^\s*-\s+", block.group(1), flags=re.MULTILINE)[1:]:
        ident = re.search(r"id:\s*(\S+)", entry)
        reason = re.search(r"reason:\s*(.+)", entry)
        if ident:
            overrides[ident.group(1)] = reason.group(1).strip() if reason else ""
    return overrides


def apply_overrides(issues, overrides):
    """Turn issues for validly overridden design constraints into INFO; reject floor overrides."""
    result = []
    for ident, reason in overrides.items():
        if ident in QUALITY_FLOORS:
            result.append(("deck", "ERROR", ident, "quality floor cannot be overridden by the Contract"))
        elif not reason:
            result.append(("deck", "ERROR", ident, "canon_overrides entry has no reason, so it is void"))
    valid = {i: r for i, r in overrides.items() if r and i not in QUALITY_FLOORS}
    for where, severity, rule, message in issues:
        if rule in valid and severity in ("ERROR", "WARNING"):
            result.append((where, "INFO", rule, f"overridden ({valid[rule]}): {message}"))
        else:
            result.append((where, severity, rule, message))
    return result


def check(deck_html, design, slide_max=None):
    parser = DeckParser()
    parser.feed(deck_html)
    slides = parser.slides
    issues = []  # (slide number or "deck", severity, rule, message)

    if not slides:
        issues.append(("deck", "ERROR", "markup", 'no elements with class "slide" found'))
        return slides, issues

    source = COMMENTS.sub("", deck_html)
    if EXTERNAL_RESOURCE.search(source):
        issues.append(("deck", "ERROR", "3.5", "loads an external resource; the deck will break offline"))
    if COLOR_SCHEME_QUERY.search(source):
        issues.append(("deck", "WARNING", "3.5", "follows prefers-color-scheme; use a fixed light theme"))
    if "data-deck-runtime" not in source:
        issues.append(("deck", "WARNING", "3.7", "no deck runtime; copy it from templates/deck.html for keyboard navigation"))
    styles = " ".join(a or b for a, b in STYLE_BLOCK.findall(source))
    ming = sorted({m.group(0) for m in MING_OR_SERIF.finditer(styles)})
    if ming:
        issues.append(("deck", "WARNING", "3.2", f"font stack includes a Ming or serif face: {', '.join(ming)}"))

    if slide_max is not None and len(slides) > slide_max:
        issues.append(("deck", "ERROR", "Contract",
                       f"{len(slides)} slides exceed slide_count_max {slide_max}"))

    banned = banned_phrases(design)
    for number, slide in enumerate(slides, start=1):
        text = "".join(slide["content"])
        units = text_units(text)
        slide["units"] = units

        if units > CONTENT_MAX:
            issues.append((number, "ERROR", "C10", f"{units} text units exceed {CONTENT_MAX}"))
        low_high = DENSITY_RANGES.get(slide["density"])
        if low_high and not low_high[0] <= units <= low_high[1]:
            issues.append((number, "WARNING", "C10",
                           f"{units} text units outside the {slide['density']} range {low_high[0]}-{low_high[1]}"))

        for phrase in banned:
            if phrase in text:
                issues.append((number, "WARNING", "3.13", f"banned phrase 「{phrase}」"))
        for phrase in PREVIEWS:
            if phrase in text:
                issues.append((number, "WARNING", "3.13", f"forward-reference sentence 「{phrase}」"))
        if DASHES.search(text):
            issues.append((number, "WARNING", "3.13", "dash used in slide text"))
        if EMOJI.search(text):
            issues.append((number, "WARNING", "3.11", "emoji used; label confidence in words"))
        for phrase in ABSOLUTES:
            if phrase in text:
                issues.append((number, "WARNING", "C13",
                               f"absolute 「{phrase}」: confirm sample size or accuracy supports it"))

    energies = [s["energy"] for s in slides]
    if all(energies):
        run = []
        for number, slide in enumerate(slides, start=1):
            if slide["energy"] == "BOLD":
                run = []
                continue
            run.append((number, slide["override"]))
            if len(run) == BOLD_GAP and not any(reason for _, reason in run):
                issues.append((run[0][0], "WARNING", "C14",
                               f"slides {run[0][0]}-{run[-1][0]} have no BOLD slide"))
    else:
        issues.append(("deck", "INFO", "C14", "not every slide declares data-energy; rhythm not checked"))

    return slides, issues


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("deck", help="HTML deck to check")
    parser.add_argument("--contract", help="Deck Contract YAML, for slide_count_max and canon_overrides")
    args = parser.parse_args()

    design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
    deck_html = Path(args.deck).read_text(encoding="utf-8")
    slide_max = contract_slide_max(args.contract) if args.contract else None

    slides, issues = check(deck_html, design, slide_max)
    if args.contract:
        issues = apply_overrides(issues, contract_overrides(args.contract))

    for number, slide in enumerate(slides, start=1):
        print(f"slide {number}: {slide.get('units', 0)} text units"
              f"{', ' + slide['density'] if slide['density'] else ''}"
              f"{', ' + slide['energy'] if slide['energy'] else ''}")
    for where, severity, rule, message in issues:
        label = "deck" if where == "deck" else f"slide {where}"
        print(f"{severity:<7} {rule:<8} {label}: {message}")

    print("NOT CHECKED: font size (C03, C04), overflow and clipping (P0), safe margins, contrast,"
          " accent count (C08), evidence mapping (1.4). These need a rendered page or human review.")

    errors = sum(1 for _, severity, _, _ in issues if severity == "ERROR")
    warnings = sum(1 for _, severity, _, _ in issues if severity == "WARNING")
    print(f"{'REVISE' if errors else 'PASS'} (text and source checks only): {errors} error(s), {warnings} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
