---
name: odoo-development
description: Odoo development workflow for module generation, review, upgrade, security, OWL, reports, testing, and performance across Odoo 14-19. Use when Codex or Claude needs a native packaged skill for Odoo addons, manifests, XML views, ORM logic, migrations, tracebacks, or addon code review.
---

# Odoo Development

Use this skill as the version router and shared Odoo pack entrypoint. Prefer the matching version-specific skill `odoo-14.0` through `odoo-19.0` once the target version is known.

## Mandatory procedure

1. Detect or confirm the target Odoo version before writing code. If needed, run `python ../../scripts/detect_odoo_version.py`.
2. Switch to the matching version-specific skill when possible:
   - `../odoo-14.0/SKILL.md`
   - `../odoo-15.0/SKILL.md`
   - `../odoo-16.0/SKILL.md`
   - `../odoo-17.0/SKILL.md`
   - `../odoo-18.0/SKILL.md`
   - `../odoo-19.0/SKILL.md`
3. Read the matching workflow in `../../workflows/`.
4. Read only the references needed for the version and task.
5. Read `../../rules/security.md` and `../../rules/coding-style.md` when generating or reviewing code.
6. Use helper prompts from `../../agents/` only when they materially improve the task.
7. Verify uncertain syntax against official Odoo docs or source.
8. Validate security, manifest order, and tests before finishing.

## Version routing

- Odoo 14: `references/odoo-*-14.md`, `references/odoo-*-14-15.md`
- Odoo 15: `references/odoo-*-15.md`, `references/odoo-*-15-16.md`
- Odoo 16: `references/odoo-*-16.md`, `references/odoo-*-16-17.md`
- Odoo 17: `references/odoo-*-17.md`, `references/odoo-*-17-18.md`
- Odoo 18: `references/odoo-*-18.md`, `references/odoo-*-18-19.md`
- Odoo 19: `references/odoo-*-19.md`, `references/odoo-*-18-19.md`

## Reference map

- Module scaffolding: `references/odoo-module-generator-<version>.md`
- Model patterns: `references/odoo-model-patterns-<version>.md`
- Security: `references/odoo-security-guide-<version>.md`
- Version deltas: `references/odoo-version-knowledge-<version>.md`
- OWL: `references/odoo-owl-components-<version>.md`
- Views: `references/xml-view-patterns.md`
- Reports: `references/report-patterns.md`
- Tests: `references/odoo-test-patterns.md`
- Performance: `references/odoo-performance-guide.md`
- Troubleshooting: `references/odoo-troubleshooting-guide.md`

## Hard rules

- Never guess the Odoo version when the manifest is missing or unclear.
- For Odoo 17+, use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- For Odoo 16+, prefer `Command` for x2many operations.
- For Odoo 17+, use `@api.model_create_multi` for `create()`.
- For Odoo 18+, use `_check_company_auto = True`, `check_company=True`, and `allowed_company_ids` where applicable.
- Every model needs access rights in `security/ir.model.access.csv`.
