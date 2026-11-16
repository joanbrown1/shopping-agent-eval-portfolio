#!/usr/bin/env python3
"""Validate structural consistency of scenario portfolio cases."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SCENARIOS = ROOT / "scenarios"
REQUIRED_FILES = [
    "task.md",
    "transcript.md",
    "review.md",
    "rubric_before.json",
    "rubric_after.json",
]
ALLOWED_DECISIONS = {"REPAIR", "REWORK_TASK", "MODEL_ERROR", "NO_MODEL_ERROR"}
REQUIRED_CRITERION_KEYS = {"id", "text", "required"}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_rubric(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")


def validate_criteria(path: Path, record: dict, *, require_source: bool) -> None:
    if "case_id" not in record or not str(record["case_id"]).strip():
        fail(f"{path}: missing case_id")
    criteria = record.get("criteria")
    if not isinstance(criteria, list) or not criteria:
        fail(f"{path}: criteria must be a non-empty list")
    ids = []
    for index, item in enumerate(criteria):
        missing = REQUIRED_CRITERION_KEYS - set(item)
        if missing:
            fail(f"{path}: criteria[{index}] missing {sorted(missing)}")
        cid = item["id"]
        if not isinstance(cid, str) or not cid.strip():
            fail(f"{path}: empty criterion id at {index}")
        if not isinstance(item["text"], str) or not item["text"].strip():
            fail(f"{path}: {cid}: empty text")
        if not isinstance(item["required"], bool):
            fail(f"{path}: {cid}: required must be boolean")
        if require_source:
            source = item.get("source")
            if not isinstance(source, str) or not source.strip():
                fail(f"{path}: {cid}: revised criteria need source")
        ids.append(cid)
    if len(ids) != len(set(ids)):
        fail(f"{path}: duplicate IDs {ids}")


def validate_case(folder: Path) -> None:
    for filename in REQUIRED_FILES:
        path = folder / filename
        if not path.exists() or path.stat().st_size == 0:
            fail(f"{folder.name}: missing/empty {filename}")
    before = load_rubric(folder / "rubric_before.json")
    after = load_rubric(folder / "rubric_after.json")
    validate_criteria(folder / "rubric_before.json", before, require_source=False)
    validate_criteria(folder / "rubric_after.json", after, require_source=True)
    decision = after.get("decision")
    if not isinstance(decision, str) or not decision.strip():
        fail(f"{folder.name}: missing decision")
    labels = {p.strip() for p in decision.replace("/", " ").replace("+", " ").split() if p.strip()}
    unknown = labels - ALLOWED_DECISIONS
    if unknown:
        fail(f"{folder.name}: unknown decision labels {sorted(unknown)}")
    review = (folder / "review.md").read_text(encoding="utf-8")
    if "Verdict" not in review:
        fail(f"{folder.name}: review.md needs a Verdict")
    print(f"{folder.name}: OK ({len(after['criteria'])} criteria, decision={decision})")


def main() -> None:
    if not SCENARIOS.is_dir():
        fail("scenarios/ directory missing")
    cases = sorted(p for p in SCENARIOS.iterdir() if p.is_dir() and not p.name.startswith("."))
    if len(cases) < 2:
        fail("expected multiple scenario folders")
    for folder in cases:
        validate_case(folder)
    print(f"All {len(cases)} scenarios validated.")


if __name__ == "__main__":
    main()
