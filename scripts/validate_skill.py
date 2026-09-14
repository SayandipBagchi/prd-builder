#!/usr/bin/env python3
"""Validate the prd-builder plugin package. No third-party dependencies.

Run from anywhere:  python3 scripts/validate_skill.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
SKILLS_DIR = ROOT / "skills"
COMMANDS_DIR = ROOT / "commands"
EVALS_DIR = ROOT / "evals"

FRONTMATTER_KEYS = {
    "name",
    "description",
    "metadata",
    "allowed-tools",
    "license",
    "disable-model-invocation",
}

# Version and author are declared once, in .claude-plugin/plugin.json.
# Nothing else in the package restates them, so a bump is a one-line edit.

EXPLICIT_ONLY = {"planning-task-breakdown", "publishing-prd"}

SKILLS = {
    "prd-builder": {
        "required": [
            "references/tenant-resolution.md",
            "references/dor-gate.md",
            "references/guardrails.md",
            "references/portability.md",
            "templates/tenant-profile.md",
            "templates/context-capsule.md",
            "profiles/example-saas.md",
        ],
        "markers": [
            "Routing table",
            "Resolve the tenant first",
            "definition-of-ready gate",
            "Context budget",
            "writing-prd",
            "reviewing-prd",
            "planning-task-breakdown",
            "writing-test-cases",
            "publishing-prd",
        ],
        "anti_markers": [
            "Check 5",          # the rubric belongs to reviewing-prd
            "Given:",           # template shapes belong to writing-prd
        ],
    },
    "writing-prd": {
        "required": [
            "references/source-and-resume-policy.md",
            "references/guided-clarification.md",
            "templates/prd-template.md",
            "examples/worked-prd.md",
        ],
        "markers": [
            "Source priority",
            "Loop control",
            "Resume",
            "reviewing-prd",
            "Interrogate",
        ],
        "anti_markers": [
            "Scorecard",        # review output shape belongs to reviewing-prd
            "Ownership",        # grouping belongs to planning-task-breakdown
        ],
    },
    "reviewing-prd": {
        "required": [
            "references/review-rules.md",
            "references/quality-checks.md",
            "examples/sample-review.md",
        ],
        "markers": [
            "Scorecard",
            "Definition-of-Ready Gaps",
            "Needs Clarification",
            "Optional Tightening",
            "not ready",
            "ready with conditions",
        ],
        "anti_markers": [
            "Guided Clarification",   # authoring flow belongs to writing-prd
        ],
    },
    "planning-task-breakdown": {
        "required": [
            "references/ownership-metadata.md",
            "references/ticket-write-policy.md",
        ],
        "markers": [
            "Group before you split",
            "Preview",
            "create metadata",
            "traceability",
            "override",
        ],
        "anti_markers": [
            "Scorecard",
        ],
    },
    "writing-test-cases": {
        "required": [
            "references/coverage-model.md",
            "templates/test-design.md",
        ],
        "markers": [
            "coverage",
            "boundary",
            "idempotency",
            "gaps",
            "undefined in source",
        ],
        "anti_markers": [
            "Scorecard",
        ],
    },
    "publishing-prd": {
        "required": [
            "references/confluence-api.md",
            "references/repo-publish.md",
        ],
        "markers": [
            "Resolve the destination",
            "override block",
            "one artefact per instruction",
        ],
        "anti_markers": [
            "Scorecard",
        ],
    },
}

COMMANDS = {
    "prd.md": "writing-prd",
    "review.md": "reviewing-prd",
    "breakdown.md": "planning-task-breakdown",
    "testcases.md": "writing-test-cases",
    "publish.md": "publishing-prd",
    "onboard.md": "prd-builder",
}

RUBRIC_CHECK_COUNT = 11
FATAL_CHECK_COUNT = 4

errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def parse_frontmatter(raw: str) -> dict:
    """Minimal YAML: top-level key: value plus one nesting level."""
    out: dict = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(("  ", "\t")):
            if current_key:
                sub = line.strip()
                if ":" in sub:
                    k, v = sub.split(":", 1)
                    if not isinstance(out.get(current_key), dict):
                        out[current_key] = {}
                    out[current_key][k.strip()] = v.strip()
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            current_key = k.strip()
            out[current_key] = v.strip()
    return out


CODE_FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`]*`")


def prose_lines(text: str):
    """Yield (lineno, line) for prose only: no code fences, no inline code,
    no table rows, no frontmatter, no horizontal rules."""
    body = CODE_FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    _, body = split_frontmatter(body) if body.startswith("---\n") else (None, body)
    for i, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("|"):
            continue
        if set(stripped) <= set("-*_") and len(stripped) >= 3:
            continue
        yield i, INLINE_CODE.sub("", line)


DASH_PATTERNS = [
    (re.compile(r"—"), "em dash"),
    (re.compile(r"–"), "en dash"),
    (re.compile(r"\w\s--\s?\w|\w\s?--\s\w"), "double hyphen used as a dash"),
    (re.compile(r"\w\s-\s\w"), "spaced hyphen used as a dash"),
]


def check_no_dashes(path: Path, text: str) -> None:
    for lineno, line in prose_lines(text):
        for pattern, label in DASH_PATTERNS:
            if pattern.search(line):
                fail(f"{path.relative_to(ROOT)}:{lineno} contains {label}: {line.strip()[:70]}")


def check_manifest() -> dict:
    if not MANIFEST.exists():
        fail("missing .claude-plugin/plugin.json")
        return {}
    data = json.loads(read(MANIFEST))
    for key in ("name", "version", "description", "author", "license", "keywords"):
        if key not in data:
            fail(f"manifest missing key: {key}")
    if data.get("name") != "prd-builder":
        fail(f"manifest name is {data.get('name')!r}, expected 'prd-builder'")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(data.get("version", ""))):
        fail(f"manifest version is not semver: {data.get('version')!r}")
    if len(data.get("description", "")) < 80:
        fail("manifest description is too short to be useful in a plugin list")
    if not isinstance(data.get("author"), dict) or "name" not in data.get("author", {}):
        fail("manifest author must be an object with a name")
    return data


def check_single_source_version(manifest: dict) -> None:
    version = str(manifest.get("version", ""))
    author = manifest.get("author", {}).get("name", "")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read(path)
        if version and version in text and path.name != "CHANGELOG.md":
            fail(f"{path.relative_to(ROOT)} restates the version; it belongs only in plugin.json")
    author_files = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        if author and author in read(path):
            author_files.append(path.relative_to(ROOT))
    allowed = {
        Path("README.md"),
        Path("LICENSE"),
        Path("hosts/openai.yaml"),
    }
    for rel in author_files:
        if rel in allowed:
            continue
        if rel.parts[0] == "skills" and rel.name == "SKILL.md":
            continue  # frontmatter metadata.author is the declared per-skill home
        fail(f"{rel} restates the author outside the allowed locations")


def check_skills() -> None:
    if not SKILLS_DIR.is_dir():
        fail("missing skills/ directory")
        return
    found = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    expected = set(SKILLS)
    if found != expected:
        fail(f"skill directories {sorted(found)} do not match expected {sorted(expected)}")

    for name, spec in SKILLS.items():
        sdir = SKILLS_DIR / name
        skill_md = sdir / "SKILL.md"
        if not skill_md.exists():
            fail(f"{name}: missing SKILL.md")
            continue
        text = read(skill_md)
        raw_fm, body = split_frontmatter(text)
        if raw_fm is None:
            fail(f"{name}: SKILL.md has no frontmatter")
            continue
        fm = parse_frontmatter(raw_fm)

        unknown = set(fm) - FRONTMATTER_KEYS
        if unknown:
            fail(f"{name}: unknown frontmatter keys {sorted(unknown)}")
        if fm.get("name") != name:
            fail(f"{name}: frontmatter name is {fm.get('name')!r}")
        desc = fm.get("description", "")
        if len(desc) < 200:
            fail(f"{name}: description is {len(desc)} chars; too thin to trigger reliably")
        if "Do not use" not in desc:
            fail(f"{name}: description has no negative case")
        if not isinstance(fm.get("metadata"), dict) or "author" not in fm.get("metadata", {}):
            fail(f"{name}: frontmatter metadata.author missing")
        if "version" in raw_fm:
            fail(f"{name}: version must not appear in skill frontmatter")

        dmi = str(fm.get("disable-model-invocation", "")).lower() == "true"
        if name in EXPLICIT_ONLY and not dmi:
            fail(f"{name}: writes outside the conversation, so it must be explicit-only")
        if name not in EXPLICIT_ONLY and dmi:
            fail(f"{name}: should be model-invocable but is marked explicit-only")

        for rel in spec["required"]:
            if not (sdir / rel).exists():
                fail(f"{name}: missing required file {rel}")

        for marker in spec["markers"]:
            if marker.lower() not in text.lower():
                fail(f"{name}: SKILL.md missing behaviour marker {marker!r}")
        for anti in spec["anti_markers"]:
            if anti.lower() in text.lower():
                fail(f"{name}: SKILL.md contains {anti!r}, which belongs to another skill")

        for path in sdir.rglob("*.md"):
            check_no_dashes(path, read(path))
            check_no_boundary_crossing(path)


LINK = re.compile(r"\]\(([^)]+)\)")


def check_no_boundary_crossing(path: Path) -> None:
    """No reference may resolve outside its own skill directory."""
    skill_root = path
    while skill_root.parent != SKILLS_DIR:
        skill_root = skill_root.parent
    text = read(path)
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (path.parent / target.split("#")[0]).resolve()
        try:
            resolved.relative_to(skill_root.resolve())
        except ValueError:
            fail(f"{path.relative_to(ROOT)} links outside its skill: {target}")
    for hit in re.findall(r"`(\.\./[^`]+)`", text):
        depth_out = hit.count("../")
        rel_depth = len(path.parent.relative_to(skill_root).parts)
        if depth_out > rel_depth:
            fail(f"{path.relative_to(ROOT)} references outside its skill: {hit}")


def check_rubric() -> None:
    path = SKILLS_DIR / "reviewing-prd" / "references" / "quality-checks.md"
    if not path.exists():
        return
    text = read(path)
    checks = set(re.findall(r"^### Check (\d+):", text, re.M))
    if len(checks) != RUBRIC_CHECK_COUNT:
        fail(f"rubric has {len(checks)} checks, expected {RUBRIC_CHECK_COUNT}")
    fatal = re.findall(r"^### Check (\d+):.*FATAL", text, re.M)
    if len(fatal) != FATAL_CHECK_COUNT:
        fail(f"rubric marks {len(fatal)} checks fatal, expected {FATAL_CHECK_COUNT}")
    if sorted(fatal) != ["1", "5", "7", "9"]:
        fail(f"fatal checks are {sorted(fatal)}, expected 1, 5, 7 and 9")
    gate = SKILLS_DIR / "prd-builder" / "references" / "dor-gate.md"
    if gate.exists() and "four fatal checks" not in read(gate).lower():
        fail("dor-gate.md does not name the four fatal checks")


def check_commands() -> None:
    if not COMMANDS_DIR.is_dir():
        fail("missing commands/ directory")
        return
    found = {p.name for p in COMMANDS_DIR.glob("*.md")}
    if found != set(COMMANDS):
        fail(f"commands {sorted(found)} do not match expected {sorted(COMMANDS)}")
    for filename, skill in COMMANDS.items():
        path = COMMANDS_DIR / filename
        if not path.exists():
            continue
        text = read(path)
        raw_fm, body = split_frontmatter(text)
        if raw_fm is None:
            fail(f"commands/{filename}: no frontmatter")
            continue
        fm = parse_frontmatter(raw_fm)
        if not fm.get("description"):
            fail(f"commands/{filename}: no description")
        if not fm.get("argument-hint"):
            fail(f"commands/{filename}: no argument-hint")
        if "$ARGUMENTS" not in body:
            fail(f"commands/{filename}: does not pass $ARGUMENTS through")
        if skill not in body:
            fail(f"commands/{filename}: does not name the {skill} skill")
        check_no_dashes(path, text)


def check_hosts() -> None:
    path = ROOT / "hosts" / "openai.yaml"
    if not path.exists():
        fail("missing hosts/openai.yaml")
        return
    text = read(path)
    for name in SKILLS:
        if f"name: {name}" not in text:
            fail(f"hosts/openai.yaml does not list skill {name}")
    for name in EXPLICIT_ONLY:
        block = text.split(f"name: {name}", 1)[-1].split("- name:", 1)[0]
        if "allow_implicit_invocation: false" not in block:
            fail(f"hosts/openai.yaml allows implicit invocation for {name}")
    if (ROOT / "agents").exists():
        fail("agents/ exists; host metadata belongs in hosts/ and agents/ means subagents")


def check_evals() -> None:
    if not EVALS_DIR.is_dir():
        fail("missing evals/ directory")
        return
    cases = [p for p in EVALS_DIR.iterdir() if p.is_dir()]
    if len(cases) < 12:
        fail(f"{len(cases)} eval cases, expected at least 12")
    known = set(SKILLS)
    for case in sorted(cases):
        for rel in ("prompt.md", "case.yaml", "graders/criteria.md", "graders/skill-fired.md"):
            if not (case / rel).exists():
                fail(f"evals/{case.name}: missing {rel}")
        cy = case / "case.yaml"
        if cy.exists():
            fm = parse_frontmatter(read(cy))
            ctx = fm.get("context", {})
            target = ctx.get("target_skill") if isinstance(ctx, dict) else None
            should = ctx.get("should_fire") if isinstance(ctx, dict) else None
            if target not in known:
                fail(f"evals/{case.name}: target_skill {target!r} is not a skill in this package")
            if should not in ("true", "false"):
                fail(f"evals/{case.name}: should_fire must be true or false, got {should!r}")
        crit = case / "graders" / "criteria.md"
        if crit.exists():
            boxes = read(crit).count("- [ ]")
            if boxes < 3:
                fail(f"evals/{case.name}: criteria has {boxes} checkboxes, expected at least 3")


def check_package_docs() -> None:
    for name in ("README.md", "CHANGELOG.md", "LICENSE"):
        if not (ROOT / name).exists():
            fail(f"missing {name}")
    for forbidden in (".mcp.json", "hooks", "settings.json", "bin"):
        if (ROOT / forbidden).exists():
            warn(f"{forbidden} present; this package is meant to need none")


def main() -> int:
    manifest = check_manifest()
    check_package_docs()
    check_skills()
    check_rubric()
    check_commands()
    check_hosts()
    check_evals()
    if manifest:
        check_single_source_version(manifest)

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} problem(s).")
        return 1
    print(f"ok    prd-builder {manifest.get('version', '?')}: "
          f"{len(SKILLS)} skills, {len(COMMANDS)} commands, "
          f"{len([p for p in EVALS_DIR.iterdir() if p.is_dir()]) if EVALS_DIR.is_dir() else 0} eval cases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
