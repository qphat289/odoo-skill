# Odoo Development Workspace

Use this repository in Gemini or Antigravity as a project-guided Odoo workspace.

## Integration rule

Treat `GEMINI.md` as the project instruction file.

Do not assume `gemini-extension.json`, root `agents/`, root `workflows/`, root `rules/`, or every file under `skills/` is automatically registered as a native Gemini feature. Unless the runtime explicitly documents that behavior, those files are repository content to read on demand.

## Required workflow

1. Detect or confirm the target Odoo version.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Switch to the matching version skill when the version is known.
5. Read the relevant file from `workflows/`.
6. Read only the needed references from `skills/odoo-development/references/`.
7. Read `rules/security.md` and `rules/coding-style.md` when generating, reviewing, or upgrading code.
8. Read the relevant helper prompt from `agents/` when needed.
9. Verify uncertain syntax against official Odoo documentation or official Odoo source.
10. Validate security, manifest order, and tests before finishing.

## Odoo rules

- Never guess the Odoo version if the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes instead of `attrs`.
- For Odoo 16+, use `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, and `allowed_company_ids` where applicable.
- Every model needs access rights in `security/ir.model.access.csv`.
