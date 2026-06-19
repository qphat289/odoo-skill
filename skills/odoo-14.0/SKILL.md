---
name: odoo-14.0
description: Odoo 14 skill pack for module generation, review, debugging, XML/view fixes, security, reports, tests, and migrations. Use when the target version is Odoo 14.0 or when manifest/config detection resolves to 14.0.
---

# Odoo 14.0

Use this skill only for Odoo 14.0 work.

## Load order

1. Read `../odoo-development/references/odoo-version-knowledge-14.md`.
2. Read `../odoo-development/references/odoo-module-generator-14.md` for scaffolding and manifest work.
3. Read `../odoo-development/references/odoo-model-patterns-14.md` for ORM/model logic.
4. Read `../odoo-development/references/odoo-security-guide-14.md` for ACL and rules.
5. Read domain references only as needed.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` for cross-cutting review criteria.

## Domain references

- Views: `../odoo-development/references/xml-view-patterns.md`
- Reports: `../odoo-development/references/report-patterns.md`
- Tests: `../odoo-development/references/odoo-test-patterns.md`
- Performance: `../odoo-development/references/odoo-performance-guide.md`
- Troubleshooting: `../odoo-development/references/odoo-troubleshooting-guide.md`

## Critical version notes

- Expect older API and XML patterns in references before applying later-version fixes.
- Review decorators, tracking fields, and view visibility against Odoo 14 references first.
