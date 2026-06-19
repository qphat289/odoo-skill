---
name: odoo-17.0
description: Odoo 17 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 17.0 or when manifest/config detection resolves to 17.0.
---

# Odoo 17.0

Use this skill only for Odoo 17.0 work.

## Load order

1. Read `../odoo-development/references/odoo-version-knowledge-17.md`.
2. Read `../odoo-development/references/odoo-module-generator-17.md` for scaffolding and manifest work.
3. Read `../odoo-development/references/odoo-model-patterns-17.md` for ORM/model logic.
4. Read `../odoo-development/references/odoo-security-guide-17.md` for ACL and rules.
5. Read domain references only as needed.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` for cross-cutting review criteria.

## Domain references

- Views: `../odoo-development/references/xml-view-patterns.md`
- Reports: `../odoo-development/references/report-patterns.md`
- OWL: `../odoo-development/references/odoo-owl-components-17.md`
- Tests: `../odoo-development/references/odoo-test-patterns.md`
- Performance: `../odoo-development/references/odoo-performance-guide.md`
- Troubleshooting: `../odoo-development/references/odoo-troubleshooting-guide.md`

## Critical version notes

- Use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- Use `@api.model_create_multi` for `create()`.
- Prefer version-specific examples from Odoo 17 references over generic Odoo patterns.
