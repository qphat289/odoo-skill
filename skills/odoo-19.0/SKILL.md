---
name: odoo-19.0
description: Odoo 19 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 19.0 or when manifest/config detection resolves to 19.0.
---

# Odoo 19.0

Use this skill only for Odoo 19.0 work.

## Load order

1. Read `../odoo-development/references/odoo-version-knowledge-19.md`.
2. Read `../odoo-development/references/odoo-module-generator-19.md` for scaffolding and manifest work.
3. Read `../odoo-development/references/odoo-model-patterns-19.md` for ORM/model logic.
4. Read `../odoo-development/references/odoo-security-guide-19.md` for ACL and rules.
5. Read domain references only as needed.
6. Read `../../rules/security.md` and `../../rules/coding-style.md` for cross-cutting review criteria.

## Domain references

- Views: `../odoo-development/references/xml-view-patterns.md`
- Reports: `../odoo-development/references/report-patterns.md`
- OWL: `../odoo-development/references/odoo-owl-components-19.md`
- Tests: `../odoo-development/references/odoo-test-patterns.md`
- Performance: `../odoo-development/references/odoo-performance-guide.md`
- Troubleshooting: `../odoo-development/references/odoo-troubleshooting-guide.md`

## Critical version notes

- Prefer the Odoo 19 references first; do not reuse 17/18 snippets without checking deltas.
- Watch for newer SQL constraint and typing conventions documented in the 19.x references.
- Review security and OWL examples against 19.x-specific references before copying.
