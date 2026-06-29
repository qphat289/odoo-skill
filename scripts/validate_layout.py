from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_ROOT = REPO_ROOT / "skills" / "odoo-development"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    required_paths = [
        REPO_ROOT / "SKILL.md",
        REPO_ROOT / "SETUP.md",
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / "CLAUDE.md",
        REPO_ROOT / "docs" / "CORRECTIONS_LOG.md",
        REPO_ROOT / "docs" / "ARTIFACT_ID_GLOSSARY.md",
        REPO_ROOT / "docs" / "HARNESS_EVAL_LOG.md",
        REPO_ROOT / "docs" / "HARNESS_EVAL_RUNBOOK.md",
        REPO_ROOT / "docs" / "SKILL_PACK_OPTIMIZATION_PLAN.md",
        REPO_ROOT / "evals",
        REPO_ROOT / "evals" / "routing-workflow-evals.json",
        REPO_ROOT / "workflows",
        REPO_ROOT / "workflows" / "full-delivery-loop.md",
        REPO_ROOT / "workflows" / "requirements-analysis.md",
        REPO_ROOT / "workflows" / "functional-design.md",
        REPO_ROOT / "workflows" / "solution-design.md",
        REPO_ROOT / "workflows" / "technical-design.md",
        REPO_ROOT / "workflows" / "test-plan.md",
        REPO_ROOT / "workflows" / "project-tracking.md",
        REPO_ROOT / "agents",
        REPO_ROOT / "agents" / "odoo-code-reviewer.md",
        REPO_ROOT / "agents" / "odoo-code-tracer.md",
        REPO_ROOT / "agents" / "odoo-context-gatherer.md",
        REPO_ROOT / "agents" / "odoo-domain-selector.md",
        REPO_ROOT / "agents" / "odoo-presales-consultant.md",
        REPO_ROOT / "agents" / "odoo-skill-finder.md",
        REPO_ROOT / "agents" / "odoo-qa-qc.md",
        REPO_ROOT / "agents" / "odoo-technical-planner.md",
        REPO_ROOT / "agents" / "odoo-tester.md",
        REPO_ROOT / "agents" / "odoo-upgrade-analyzer.md",
        REPO_ROOT / "rules",
        REPO_ROOT / "scripts",
        REPO_ROOT / ".claude-plugin" / "plugin.json",
        REPO_ROOT / ".codex-plugin" / "plugin.json",
        SKILL_ROOT / "SKILL.md",
        SKILL_ROOT / "agents" / "openai.yaml",
        SKILL_ROOT / "references",
        SKILL_ROOT / "references" / "skill-pack-harness-guide.md",
        SKILL_ROOT / "references" / "eval-campaign-guide.md",
        SKILL_ROOT / "references" / "route-pressure-scenarios.md",
        REPO_ROOT / "skills" / "odoo-14.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-14.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-15.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-15.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-16.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-16.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-17.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-17.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-18.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-18.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-19.0" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-19.0" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-module-generation" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-module-generation" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-models" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-models" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-security" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-security" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-views" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-views" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-owl" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-owl" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-upgrade" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-upgrade" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-quality" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-quality" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-documents" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-documents" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-documents" / "references" / "docx-working-guide.md",
        REPO_ROOT / "skills" / "odoo-spreadsheets" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-spreadsheets" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-spreadsheets" / "references" / "xlsx-working-guide.md",
        REPO_ROOT / "skills" / "odoo-integrations" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-integrations" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-automation" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-automation" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-business-domains" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-business-domains" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-operations" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-operations" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-presales" / "SKILL.md",
        REPO_ROOT / "skills" / "odoo-presales" / "agents" / "openai.yaml",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "customer-input-file-handling.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "requirement-analysis-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "requirement-analysis-artifact-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "requirement-analysis-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "clarification-register-xlsx-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "clarification-register-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "fit-gap-analysis-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "fit-gap-analysis-xlsx-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "fit-gap-analysis-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "functional-design-docx-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "functional-design-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "solution-design-docx-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "solution-design-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "design-artifact-handoff-guide.md",
        REPO_ROOT / "skills" / "odoo-presales" / "references" / "process-swimlane-guide.md",
        REPO_ROOT / "skills" / "odoo-module-generation" / "references" / "technical-design-template.md",
        REPO_ROOT / "skills" / "odoo-module-generation" / "references" / "technical-design-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-module-generation" / "references" / "project-tracking-example-sale-approval.md",
        REPO_ROOT / "skills" / "odoo-quality" / "references" / "test-plan-template.md",
        REPO_ROOT / "skills" / "odoo-module-generation" / "references" / "project-tracking-template.md",
        REPO_ROOT / "scripts" / "validate_skill_pack_contracts.py",
        REPO_ROOT / "scripts" / "validate_harness_evals.py",
        REPO_ROOT / "scripts" / "run_harness_eval_campaign.py",
        REPO_ROOT / "scripts" / "validate_no_stale_refs.py",
    ]

    for path in required_paths:
        if not path.exists():
            fail(f"Missing required path: {path}")

    loose_skill_files = [
        path for path in (REPO_ROOT / "skills").iterdir()
        if path.is_file()
    ]
    if loose_skill_files:
        fail(f"Loose files found directly under skills/: {', '.join(p.name for p in loose_skill_files)}")

    if (REPO_ROOT / "references").exists():
        fail("Root references/ should not exist; references must live under skill folders.")

    print("Layout OK")


if __name__ == "__main__":
    main()
