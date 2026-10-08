"""Check the integrity of the Eric Presentation Design System specification.

Standard library only. Run from anywhere:

    python scripts/check_repo.py
"""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [".gitignore", "README.md", "DESIGN.md"]

EXPECTED_IDS = {
    "Canon": [f"C{n:02d}" for n in range(1, 16)],
    "Pattern": [f"P{n:02d}" for n in range(1, 16)],
    "Motif": [f"M-{letter}" for letter in "ABCDEFGH"],
    "Smell": [f"S{n:02d}" for n in range(1, 16)],
}

LOCAL_ONLY_FILES = [
    "AI_Playbook_DesignSystem_v1.1.html",
    "知識庫Playbook-母文件.md",
    "DECK_MAP.md",
]

CANON_FIELDS = ["RULE", "WHEN", "CHECK", "SEVERITY"]
PATTERN_FIELDS = ["Use when", "Do not use when", "Default motif", "Density"]
PATTERN_DENSITIES = ["LOW", "MEDIUM", "HIGH"]
SMELL_FIELDS = ["觸發條件"]

ID_TOKEN = re.compile(r"\b(C\d{2}|P\d{2}|S\d{2}|M-[A-H])\b")


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def sections(text, pattern):
    """Split text into (id, body) pairs for every '## <id>' heading matching pattern."""
    heads = list(re.finditer(r"^## (.+)$", text, flags=re.MULTILINE))
    result = []
    for index, head in enumerate(heads):
        match = re.match(pattern, head.group(1))
        if not match:
            continue
        end = heads[index + 1].start() if index + 1 < len(heads) else len(text)
        result.append((match.group(1), text[head.end():end]))
    return result


def check_canon(design, errors):
    found = {}
    for ident, body in sections(design, r"^(C\d{2})\b"):
        found[ident] = body
        for field in CANON_FIELDS:
            if not re.search(rf"^\*\*{field}\*\*", body, flags=re.MULTILINE):
                errors.append(f"Canon {ident} is missing the {field} field")
        if "**SEVERITY**" in body:
            # The severity may be a bare word or a sentence ending in one, so search the block.
            block = body.split("**SEVERITY**", 1)[1].split("\n---", 1)[0]
            if not re.search(r"\b(ERROR|WARNING)\b", block):
                errors.append(f"Canon {ident} SEVERITY names neither ERROR nor WARNING")
    return found


def check_pattern(design, errors):
    for ident, body in sections(design, r"^(P\d{2})\b"):
        for field in PATTERN_FIELDS:
            if not re.search(rf"^{field}\s*[:：]", body, flags=re.MULTILINE):
                errors.append(f"Pattern {ident} is missing the '{field}' field")
        density = re.search(r"^Density\s*[:：]\s*\n+-\s*(\S+)", body, flags=re.MULTILINE)
        if density and not any(d in density.group(1) for d in PATTERN_DENSITIES):
            errors.append(f"Pattern {ident} has unknown Density {density.group(1)!r}")


def check_smell(design, errors):
    for ident, body in sections(design, r"^(S\d{2})\b"):
        for field in SMELL_FIELDS:
            if field not in body:
                errors.append(f"Smell {ident} is missing the '{field}' block")


def check_changelog(design, title_version, errors):
    changelog = design.split("# 10. CHANGELOG", 1)
    if len(changelog) != 2:
        errors.append("DESIGN.md has no '# 10. CHANGELOG' section")
        return
    latest = re.search(r"^## v(\d+\.\d+)", changelog[1], flags=re.MULTILINE)
    if not latest:
        errors.append("CHANGELOG has no version entries")
    elif latest.group(1) != title_version:
        errors.append(
            f"CHANGELOG latest entry is v{latest.group(1)}; title is v{title_version}"
        )


def check_references(files, ids, errors):
    """Every C/P/S/M ID mentioned in the docs must exist in the expected lists."""
    known = {ident for group in ids.values() for ident in group}
    for name, text in files.items():
        for token in sorted(set(ID_TOKEN.findall(text))):
            if token not in known:
                errors.append(f"{name} references unknown ID {token}")


def check_links(name, text, errors):
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = target.split("#", 1)[0]
        if path and not (ROOT / path).is_file():
            errors.append(f"{name} links to missing file: {path}")


def main():
    errors = []

    for path in REQUIRED_FILES:
        if not (ROOT / path).is_file():
            errors.append(f"missing required file: {path}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    design = read("DESIGN.md")
    readme = read("README.md")
    gitignore = [line.strip() for line in read(".gitignore").splitlines()]

    version_match = re.search(r"^# Eric Presentation Design System v(\d+\.\d+)$", design, flags=re.MULTILINE)
    if not version_match:
        errors.append("DESIGN.md has no semantic version in its title")
        version = None
    else:
        version = version_match.group(1)
        if f"Eric Presentation Design System v{version}" not in readme:
            errors.append(f"README version does not match DESIGN.md v{version}")
        check_changelog(design, version, errors)

    actual_ids = {
        "Canon": [i for i, _ in sections(design, r"^(C\d{2})\b")],
        "Pattern": [i for i, _ in sections(design, r"^(P\d{2})\b")],
        "Motif": [i for i, _ in sections(design, r"^(M-[A-H])\b")],
        "Smell": [i for i, _ in sections(design, r"^(S\d{2})\b")],
    }
    for group, expected in EXPECTED_IDS.items():
        if actual_ids[group] != expected:
            errors.append(f"{group} IDs are {actual_ids[group]}; expected {expected}")

    check_canon(design, errors)
    check_pattern(design, errors)
    check_smell(design, errors)

    check_references({"DESIGN.md": design, "README.md": readme}, EXPECTED_IDS, errors)

    for path in LOCAL_ONLY_FILES:
        if f"/{path}" not in gitignore:
            errors.append(f"local-only file is not ignored: {path}")

    check_links("README.md", readme, errors)
    check_links("DESIGN.md", design, errors)

    if errors:
        print(f"REVISE: {len(errors)} problem(s) found:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"PASS: README and DESIGN.md versions match at v{version}.")
    for group, ids in EXPECTED_IDS.items():
        print(f"PASS: {group} IDs are complete ({ids[0]}-{ids[-1]}).")
    print("PASS: Canon, Pattern, and Smell entries have their required fields.")
    print("PASS: CHANGELOG latest entry matches the DESIGN.md version.")
    print("PASS: every C/P/S/M reference resolves to a defined ID.")
    print("PASS: project-specific examples are ignored.")
    print("PASS: local links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
