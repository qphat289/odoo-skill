# Odoo Development Workspace

Use this repository in Claude Code as an Odoo skill-pack workspace.

## Integration rule

Opening this repository loads `CLAUDE.md`, but that alone does not register every helper file as a native Claude feature.

Native Claude skills must live under `.claude/skills/<name>/SKILL.md` or a plugin `skills/<name>/SKILL.md` layout. In this repository, the shared router skill is `skills/odoo-development/`, the version skills are `skills/odoo-14.0/` through `skills/odoo-19.0/`, the core domain skills are `skills/odoo-module-generation/`, `skills/odoo-models/`, `skills/odoo-security/`, `skills/odoo-views/`, `skills/odoo-owl/`, `skills/odoo-upgrade/`, and `skills/odoo-quality/`, and the extended domain skills are `skills/odoo-integrations/`, `skills/odoo-automation/`, `skills/odoo-business-domains/`, and `skills/odoo-operations/`.

## Required workflow

1. Detect or confirm the target Odoo version.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Switch to the matching version skill when the version is known.
5. Load the smallest relevant domain skill for the task.
6. Read the relevant file from `workflows/`.
7. Read only the needed references from the selected domain skill.
8. Read `rules/security.md` and `rules/coding-style.md` when generating or reviewing code.
9. Verify uncertain syntax against official Odoo documentation or official Odoo source.
10. Validate security, manifest order, and tests before finishing.
