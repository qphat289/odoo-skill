# Odoo Development Workspace

Use this repository in Claude Code as an Odoo skill-pack workspace.

## Integration rule

Opening this repository loads `CLAUDE.md`, but that alone does not register every helper file as a native Claude feature.

Native Claude skills must live under `.claude/skills/<name>/SKILL.md` or a plugin `skills/<name>/SKILL.md` layout. In this repository, the shared router skill is `skills/odoo-development/` and the preferred version skills are `skills/odoo-14.0/` through `skills/odoo-19.0/`.

## Required workflow

1. Detect or confirm the target Odoo version.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Switch to the matching version skill when the version is known.
5. Read the relevant file from `workflows/`.
6. Read only the needed references from `skills/odoo-development/references/`.
7. Read `rules/security.md` and `rules/coding-style.md` when generating or reviewing code.
8. Verify uncertain syntax against official Odoo documentation or official Odoo source.
9. Validate security, manifest order, and tests before finishing.
