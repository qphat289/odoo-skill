# Odoo Development for Hermes

This repository is designed for project-guided Odoo work in Hermes.

## Integration rule

Do not assume Hermes auto-registers every helper folder as a native feature. Treat `SKILL.md` as the entry point, then load only the referenced files you need.

## Required workflow

1. Load `SKILL.md`.
2. Load `skills/odoo-development/SKILL.md`.
3. Switch to the matching version skill when the target version is known.
4. Load the relevant file from `workflows/`.
5. Load only the needed references from `skills/odoo-development/references/`.
6. Load `rules/security.md` and `rules/coding-style.md` when generating, reviewing, or upgrading code.
7. Load the relevant helper prompt from `agents/` when needed.
8. Verify uncertain syntax against official Odoo documentation or official Odoo source.

## File paths

- `./SKILL.md` -> repository router entry point
- `./skills/` -> packaged Odoo skills
- `./workflows/` -> execution playbooks
- `./agents/` -> helper prompts
- `./rules/` -> cross-version rules
- `./scripts/` -> validators and helper scripts
