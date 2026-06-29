from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read(rel_path: str) -> str:
    return (REPO_ROOT / rel_path).read_text(encoding="utf-8")


def require_contains(rel_path: str, needles: list[str]) -> None:
    text = read(rel_path)
    for needle in needles:
        if needle not in text:
            fail(f"Missing expected contract text in {rel_path}: {needle}")


def main() -> None:
    required_files = [
        "skills/odoo-development/references/skill-pack-harness-guide.md",
        "skills/odoo-development/references/eval-campaign-guide.md",
        "skills/odoo-development/references/route-pressure-scenarios.md",
        "evals/routing-workflow-evals.json",
        "scripts/validate_layout.py",
        "scripts/validate_harness_evals.py",
        "scripts/run_harness_eval_campaign.py",
        "scripts/validate_no_stale_refs.py",
        "docs/CORRECTIONS_LOG.md",
        "docs/ARTIFACT_ID_GLOSSARY.md",
        "docs/HARNESS_EVAL_LOG.md",
        "docs/HARNESS_EVAL_RUNBOOK.md",
        "docs/SKILL_PACK_OPTIMIZATION_PLAN.md",
    ]

    for rel_path in required_files:
        if not (REPO_ROOT / rel_path).exists():
            fail(f"Missing required contract file: {rel_path}")

    require_contains(
        "AGENTS.md",
        [
            "Default routing workflow",
            "default playbooks, not rigid rails",
            "Treat canonical artifacts as the default output for formal delivery work",
            "skills/odoo-development/references/skill-pack-harness-guide.md",
            "evals/routing-workflow-evals.json",
            "docs/HARNESS_EVAL_LOG.md",
            "skills/odoo-documents/",
            "skills/odoo-spreadsheets/",
            "Clarification Register.xlsx",
        ],
    )

    require_contains(
        "SKILL.md",
        [
            "## Flexible routing rules",
            "Workflows are default playbooks, not rigid rails.",
            "Do not force the full artifact chain for simple review, comparison, fix, or status-update tasks.",
            "If the task touches `.docx` or spreadsheet files",
        ],
    )

    require_contains(
        "skills/odoo-development/SKILL.md",
        [
            "## Adaptive procedure",
            "## Flexibility rules",
            "Treat workflows as default playbooks, not rigid rails.",
            "Keep `.docx` and spreadsheet handling attached to the active route",
            "../odoo-documents/SKILL.md",
            "../odoo-spreadsheets/SKILL.md",
        ],
    )

    require_contains(
        "workflows/orchestrator.md",
        [
            "If no workflow fits exactly:",
            "partial or hybrid routing still preserves the key traceability needed for the task",
            "office-file handling is recognized when relevant without distorting the primary workflow choice",
        ],
    )

    require_contains(
        "workflows/skill-maintenance.md",
        [
            "skill-pack-harness-guide.md",
            "eval-campaign-guide.md",
            "route-pressure-scenarios.md",
            "routing-workflow-evals.json",
            "HARNESS_EVAL_LOG.md",
            "HARNESS_EVAL_RUNBOOK.md",
            "python scripts/validate_skill_pack_contracts.py",
            "python scripts/validate_harness_evals.py",
            "python scripts/validate_no_stale_refs.py",
            "routing or loop fixes update the harness layer when needed",
        ],
    )

    require_contains(
        "docs/CORRECTIONS_LOG.md",
        [
            "## Loophole / routing entry guideline",
            "agent-behavior loophole",
        ],
    )

    require_contains(
        "docs/HARNESS_EVAL_LOG.md",
        [
            "## Eval entries",
            "RED/GREEN/REFACTOR",
        ],
    )

    require_contains(
        "docs/HARNESS_EVAL_RUNBOOK.md",
        [
            "run_harness_eval_campaign.py",
            "Operator flow",
        ],
    )

    require_contains(
        "docs/SKILL_PACK_OPTIMIZATION_PLAN.md",
        [
            "## Optimized architecture",
            "## Office-file capability rule",
            "## Success definition",
        ],
    )

    require_contains(
        "docs/ARTIFACT_ID_GLOSSARY.md",
        [
            "`RQ-xxx`",
            "`CL-xxx`",
            "`FG-xxx`",
            "`TP-xxx`",
            "`T-xxx`",
        ],
    )

    require_contains(
        "skills/odoo-documents/SKILL.md",
        [
            "This skill does not replace the primary presales, design, QA/QC, or tracking workflow.",
            "references/docx-working-guide.md",
        ],
    )

    require_contains(
        "skills/odoo-spreadsheets/SKILL.md",
        [
            "This skill supports the primary workflow; it does not replace presales, QA/QC, or tracking routing.",
            "references/xlsx-working-guide.md",
        ],
    )

    require_contains(
        "skills/odoo-module-generation/references/technical-design-template.md",
        [
            "| Requirement Analysis |",
            "| Clarification Register |",
            "| Req ID | Fit/Gap ID | Functional Section | Solution Decision | Technical Section | Test Plan Hint | Tracking Hint | Build Treatment |",
            "### 4.1 Build order / dependency order",
        ],
    )

    require_contains(
        "skills/odoo-quality/references/test-plan-template.md",
        [
            "| Requirement Analysis |",
            "| Clarification Register |",
            "| Fit/Gap Analysis |",
            "Artifact sync rule:",
            "Reopen rule:",
        ],
    )

    require_contains(
        "skills/odoo-module-generation/references/project-tracking-template.md",
        [
            "| Requirement Analysis |",
            "| Clarification Register |",
            "| Fit/Gap Analysis |",
            "Link each task to Requirement Analysis, Fit-Gap, Functional Design, Solution Design, Technical Design, or Test Plan references as appropriate.",
        ],
    )

    print("Skill-pack contracts OK")


if __name__ == "__main__":
    main()
