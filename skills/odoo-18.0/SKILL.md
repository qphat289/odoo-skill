---
name: odoo-18.0
description: Odoo 18 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 18.0 or when manifest/config detection resolves to 18.0.
---

# Odoo 18.0

Use this skill only for Odoo 18.0 work.

## Domain map

| Topic | File | When to use |
|---|---|---|
| Version deltas | `../odoo-upgrade/references/odoo-version-knowledge-18.md` | Confirm 18.0 syntax and migration deltas |
| Module scaffolding | `../odoo-module-generation/references/odoo-module-generator-18.md` | New module, manifest, install order |
| Models | `../odoo-models/references/odoo-model-patterns-18.md` | ORM logic and field design |
| Security | `../odoo-security/references/odoo-security-guide-18.md` | ACL, groups, record rules |
| Views and reports | `../odoo-views/references/xml-view-patterns.md`, `../odoo-views/references/report-patterns.md` | XML, actions, menus, reports |
| OWL | `../odoo-owl/references/odoo-owl-components-18.md` | Frontend and widget work |
| Integrations | `../odoo-integrations/references/controller-api-patterns.md`, `../odoo-integrations/references/api-version-notes-18.md`, `../odoo-integrations/references/import-export-patterns.md` | Controllers, APIs, import/export, attachments |
| Automation | `../odoo-automation/references/cron-automation-patterns.md`, `../odoo-automation/references/sequence-numbering-patterns.md` | Cron, mail, sequence flows |
| Business flows | `../odoo-business-domains/references/sale-crm-patterns.md`, `../odoo-business-domains/references/stock-inventory-patterns.md` | Reuse core business-domain patterns |
| Operations | `../odoo-operations/references/config-settings-patterns.md`, `../odoo-operations/references/logging-debugging-patterns.md` | Settings, debugging, operational checks |
| Quality | `../odoo-quality/references/odoo-test-patterns.md`, `../odoo-quality/references/odoo-performance-guide.md` | Tests, review, performance |
| Troubleshooting | `../odoo-upgrade/references/odoo-troubleshooting-guide.md` | Debugging and recovery |

## Critical version notes

- Use `_check_company_auto = True` where company scoping applies.
- Use `check_company=True` on relevant relational fields.
- Keep record-rule domains on `company_ids`; use `allowed_company_ids` in Python/context only when active company scope must be forwarded explicitly.
- Prefer `SQL()` builder and v18 examples over older generic patterns.
