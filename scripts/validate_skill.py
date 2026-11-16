#!/usr/bin/env python3
"""Dependency-free structural checks for Adaptive Onboarding agent skill."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skill = root / "adaptive-onboarding" / "SKILL.md"
required = [
    root / "README.md",
    root / "LICENSE",
    root / "CONTRIBUTING.md",
    skill,
    *[root / "adaptive-onboarding" / "references" / name for name in (
        "evidence.md", "product-archetypes.md", "pattern-decision-guide.md",
        "instrumentation-and-experiments.md", "accessibility-and-safety.md"
    )],
    *[root / "adaptive-onboarding" / "assets" / name for name in (
        "onboarding-brief.md", "audit-template.md", "experiment-plan.md"
    )],
    *[root / "adaptive-onboarding" / "examples" / name for name in (
        "learning-app.md", "enterprise-saas.md", "security-sensitive-app.md"
    )],
]
errors = []
for path in required:
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"Missing or empty: {path.relative_to(root)}")
if skill.is_file():
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md missing YAML frontmatter")
    else:
        header = text.split("---", 2)[1]
        for field in ("name", "description"):
            if not re.search(rf"(?m)^{field}:\s*\S+", header):
                errors.append(f"SKILL.md missing '{field}'")
    for target in re.findall(r"\]\(([^)]+\.md)\)", text):
        if not (skill.parent / target).is_file():
            errors.append(f"Broken skill link: {target}")
if errors:
    print("Validation failed:\n" + "\n".join("- " + e for e in errors))
    sys.exit(1)
print(f"Validation passed: {len(required)} required files and skill references")
