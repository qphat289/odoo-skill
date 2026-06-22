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
        REPO_ROOT / "docs" / "correct-log" / "CORRECTIONS_LOG.md",
        REPO_ROOT / "workflows",
        REPO_ROOT / "agents",
        REPO_ROOT / "rules",
        REPO_ROOT / "scripts",
        REPO_ROOT / ".claude-plugin" / "plugin.json",
        REPO_ROOT / ".codex-plugin" / "plugin.json",
        SKILL_ROOT / "SKILL.md",
        SKILL_ROOT / "agents" / "openai.yaml",
        SKILL_ROOT / "references",
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
