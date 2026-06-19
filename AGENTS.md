# Odoo Development Workspace

Use this repository as an Odoo skill-pack workspace.

## Meaning

- `SKILL.md` is the project-mode router.
- `skills/odoo-development/` is the canonical packaged skill.
- `skills/odoo-14.0/` through `skills/odoo-19.0/` are version-specific skill packs.
- `skills/odoo-development/references/` is the Odoo knowledge base.
- `workflows/` contains execution playbooks.
- `rules/` contains cross-version coding and security rules.
- `agents/` contains optional helper prompts.
- `scripts/` contains installer and validation helpers.

## Required workflow

1. Detect or confirm the target Odoo version before writing code.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Prefer the matching version skill once the target version is known.
5. Read the relevant file from `workflows/`.
6. Read only the needed references from `skills/odoo-development/references/`.
7. Read `rules/security.md` and `rules/coding-style.md` when generating or reviewing code.
8. Verify uncertain syntax against official Odoo sources.
9. Validate security, manifest order, and tests before finishing.
