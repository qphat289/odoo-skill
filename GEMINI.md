# Odoo Development Workspace

Use this repository in Gemini or Antigravity as a project-guided Odoo workspace.

## Integration rule

Treat `GEMINI.md` as the project instruction file.

Do not assume `gemini-extension.json`, root `agents/`, root `workflows/`, root `rules/`, or every file under `skills/` is automatically registered as a native Gemini feature. Unless the runtime explicitly documents that behavior, those files are repository content to read on demand.

The main discovery layout in this repository is:
- shared router: `skills/odoo-development/`
- version skills: `skills/odoo-14.0/` through `skills/odoo-19.0/`
- core domain skills: `skills/odoo-module-generation/`, `skills/odoo-models/`, `skills/odoo-security/`, `skills/odoo-views/`, `skills/odoo-owl/`, `skills/odoo-upgrade/`, `skills/odoo-quality/`
- extended domain skills: `skills/odoo-integrations/`, `skills/odoo-automation/`, `skills/odoo-business-domains/`, `skills/odoo-operations/`

## Required workflow

1. Detect or confirm the target Odoo version.
2. Read `SKILL.md`.
3. Read `skills/odoo-development/SKILL.md`.
4. Switch to the matching version skill when the version is known.
5. Load the smallest relevant domain skill for the task.
6. Read the relevant file from `workflows/`.
7. Read only the needed references from the selected domain skill.
8. Read `rules/security.md` and `rules/coding-style.md` when generating, reviewing, or upgrading code.
9. Read the relevant helper prompt from `agents/` when needed.
10. Verify uncertain syntax against official Odoo documentation or official Odoo source.
11. Validate security, manifest order, and tests before finishing.

## Odoo rules

- Never guess the Odoo version if the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes instead of `attrs`.
- For Odoo 16+, use `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, and `allowed_company_ids` where applicable.
- Every model needs access rights in `security/ir.model.access.csv`.
