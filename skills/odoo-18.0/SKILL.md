---
name: odoo-18.0
description: Odoo 18 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 18.0 or when manifest/config detection resolves to 18.0.
---

# Odoo 18.0

Use this skill only for Odoo 18.0 work.

## Load order

1. Read `../odoo-development/references/odoo-version-knowledge-18.md`.
2. Read `../odoo-development/references/odoo-module-generator-18.md` for scaffolding and manifest work.
3. Read `../odoo-development/references/odoo-model-patterns-18.md` for ORM/model logic.
4. Read `../odoo-development/references/odoo-security-guide-18.md` for ACL and rules.
5. Read domain references only as needed.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` for cross-cutting review criteria.

## Domain references

- Views: `../odoo-development/references/xml-view-patterns.md`
- Reports: `../odoo-development/references/report-patterns.md`
- OWL: `../odoo-development/references/odoo-owl-components-18.md`
- Tests: `../odoo-development/references/odoo-test-patterns.md`
- Performance: `../odoo-development/references/odoo-performance-guide.md`
- Troubleshooting: `../odoo-development/references/odoo-troubleshooting-guide.md`

## Critical version notes

- Use `_check_company_auto = True` where company scoping applies.
- Use `check_company=True` on relevant relational fields.
- Prefer `allowed_company_ids` for rule context where applicable.
- Prefer `SQL()` builder and v18 examples over older generic patterns.
