---
name: odoo-development
description: Project-mode router for this Odoo skill repository. Use when working inside this repository or when a tool is guided by the root SKILL.md before loading the packaged Odoo skill and its workflow documents.
---

# Odoo Development Router

This root file is the project-mode entrypoint for the repository.

## Required order

1. Detect or confirm the target Odoo version before writing code. If it is not explicit, run `python scripts/detect_odoo_version.py`.
2. Read `skills/odoo-development/SKILL.md`.
3. Read the relevant file from `workflows/`.
4. Read only the needed references from the smallest matching domain skill under `skills/`.
5. Read the relevant helper prompt from `agents/` when needed.
6. Read `rules/security.md` and `rules/coding-style.md` for generation, review, and upgrade work.
7. Verify uncertain syntax against official Odoo sources.
8. Validate security, manifest order, and tests before finishing.

Use `skills/odoo-presales/` before coding when the task is still about discovery, fit-gap, estimation, proposal, or business-to-implementation handoff.

## Hard rules

- Never guess the Odoo version when the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- For Odoo 16+, prefer `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, and `allowed_company_ids` where applicable.
- Every model needs access rights in `security/ir.model.access.csv`.
