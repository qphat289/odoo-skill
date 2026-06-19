---
name: odoo-16.0
description: Odoo 16 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 16.0 or when manifest/config detection resolves to 16.0.
---

# Odoo 16.0

Use this skill only for Odoo 16.0 work.

## Load order

1. Read `../odoo-development/references/odoo-version-knowledge-16.md`.
2. Read `../odoo-development/references/odoo-module-generator-16.md` for scaffolding and manifest work.
3. Read `../odoo-development/references/odoo-model-patterns-16.md` for ORM/model logic.
4. Read `../odoo-development/references/odoo-security-guide-16.md` for ACL and rules.
5. Read domain references only as needed.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` for cross-cutting review criteria.

## Domain references

- Views: `../odoo-development/references/xml-view-patterns.md`
- Reports: `../odoo-development/references/report-patterns.md`
- OWL: `../odoo-development/references/odoo-owl-components-16.md`
- Tests: `../odoo-development/references/odoo-test-patterns.md`
- Performance: `../odoo-development/references/odoo-performance-guide.md`
- Troubleshooting: `../odoo-development/references/odoo-troubleshooting-guide.md`

## Critical version notes

- Prefer `Command` patterns for x2many operations.
- Treat Odoo 16 as a transition point: some later syntax is not yet mandatory.
