# Odoo Development Workspace

Use this repository as an Odoo skill-pack workspace.

## Meaning

- `SKILL.md` is the project-mode router.
- `skills/odoo-development/` is the canonical packaged skill.
- `skills/odoo-14.0/` through `skills/odoo-19.0/` are version-specific skill packs.
- `skills/odoo-module-generation/`, `skills/odoo-models/`, `skills/odoo-security/`, `skills/odoo-views/`, `skills/odoo-owl/`, `skills/odoo-upgrade/`, and `skills/odoo-quality/` are the main domain skills.
- `skills/odoo-integrations/`, `skills/odoo-automation/`, `skills/odoo-business-domains/`, and `skills/odoo-operations/` hold specialized references that were previously crowded into the shared router.
- `workflows/` contains execution playbooks.
- `rules/` contains cross-version coding and security rules.
- `agents/` contains optional helper prompts.
- `scripts/` contains installer and validation helpers.

## Required workflow

1. Detect or confirm the target Odoo version before writing code.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Prefer the matching version skill once the target version is known.
5. Load the smallest relevant domain skill for the task.
6. Read the relevant file from `workflows/`.
7. Read only the needed references from the selected domain skill.
8. Read `rules/security.md` and `rules/coding-style.md` when generating or reviewing code.
9. Verify uncertain syntax against official Odoo sources.
10. Validate security, manifest order, and tests before finishing.
