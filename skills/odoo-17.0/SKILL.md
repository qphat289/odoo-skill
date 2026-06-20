---
name: odoo-17.0
description: Odoo 17 skill pack for module generation, review, debugging, XML/view fixes, security, OWL, reports, tests, and migrations. Use when the target version is Odoo 17.0 or when manifest/config detection resolves to 17.0.
---

# Odoo 17.0

Use this skill only for Odoo 17.0 work.

## Domain map

| Topic | File | When to use |
|---|---|---|
| Version deltas | `../odoo-upgrade/references/odoo-version-knowledge-17.md` | Confirm 17.0 syntax and migration deltas |
| Module scaffolding | `../odoo-module-generation/references/odoo-module-generator-17.md` | New module, manifest, install order |
| Models | `../odoo-models/references/odoo-model-patterns-17.md` | ORM logic and field design |
| Security | `../odoo-security/references/odoo-security-guide-17.md` | ACL, groups, record rules |
| Views and reports | `../odoo-views/references/xml-view-patterns.md`, `../odoo-views/references/report-patterns.md` | XML, actions, menus, reports |
| OWL | `../odoo-owl/references/odoo-owl-components-17.md` | Frontend and widget work |
| Integrations | `../odoo-integrations/references/controller-api-patterns.md`, `../odoo-integrations/references/api-version-notes-17.md`, `../odoo-integrations/references/import-export-patterns.md` | Controllers, APIs, import/export, attachments |
| Automation | `../odoo-automation/references/cron-automation-patterns.md`, `../odoo-automation/references/sequence-numbering-patterns.md` | Cron, mail, sequence flows |
| Business flows | `../odoo-business-domains/references/sale-crm-patterns.md`, `../odoo-business-domains/references/stock-inventory-patterns.md` | Reuse core business-domain patterns |
| Operations | `../odoo-operations/references/config-settings-patterns.md`, `../odoo-operations/references/logging-debugging-patterns.md` | Settings, debugging, operational checks |
| Quality | `../odoo-quality/references/odoo-test-patterns.md`, `../odoo-quality/references/odoo-performance-guide.md` | Tests, review, performance |
| Troubleshooting | `../odoo-upgrade/references/odoo-troubleshooting-guide.md` | Debugging and recovery |

## Critical version notes

- Use direct XML attributes such as `invisible="expr"` instead of `attrs`.
- Use `@api.model_create_multi` for `create()`.
- Prefer version-specific examples from Odoo 17 references over generic Odoo patterns.
