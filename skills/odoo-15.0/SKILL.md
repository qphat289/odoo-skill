---
name: odoo-15.0
description: Odoo 15 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 15.0 or when manifest/config detection resolves to 15.0.
---

# Odoo 15.0

Use this skill only for Odoo 15.0 work.

## Domain map

| Topic | File | When to use |
|---|---|---|
| Version deltas | `../odoo-upgrade/references/odoo-version-knowledge-15.md` | Confirm 15.0 syntax and deltas |
| Module scaffolding | `../odoo-module-generation/references/odoo-module-generator-15.md` | New module, manifest, install order |
| Models | `../odoo-models/references/odoo-model-patterns-15.md` | ORM logic and field design |
| Security | `../odoo-security/references/odoo-security-guide-15.md` | ACL, groups, record rules |
| Views and reports | `../odoo-views/references/xml-view-patterns.md`, `../odoo-views/references/report-patterns.md` | XML, actions, menus, reports |
| OWL | `../odoo-owl/references/odoo-owl-components-15.md` | Frontend and widget work |
| Integrations | `../odoo-integrations/references/controller-api-patterns.md`, `../odoo-integrations/references/import-export-patterns.md` | Controllers, APIs, import/export, attachments |
| Automation | `../odoo-automation/references/cron-automation-patterns.md`, `../odoo-automation/references/sequence-numbering-patterns.md` | Cron, mail, sequence flows |
| Business flows | `../odoo-business-domains/references/sale-crm-patterns.md`, `../odoo-business-domains/references/stock-inventory-patterns.md` | Reuse core business-domain patterns |
| Operations | `../odoo-operations/references/config-settings-patterns.md`, `../odoo-operations/references/logging-debugging-patterns.md` | Settings, debugging, operational checks |
| Quality | `../odoo-quality/references/odoo-test-patterns.md`, `../odoo-quality/references/odoo-performance-guide.md` | Tests, review, performance |
| Troubleshooting | `../odoo-upgrade/references/odoo-troubleshooting-guide.md` | Debugging and recovery |

## Critical version notes

- `@api.multi` is removed, but many 17+ rules do not apply yet.
- Prefer Odoo 15 references over generic upgrade assumptions from later versions.
