---
name: odoo-14.0
description: Odoo 14 skill pack for module generation, review, debugging, XML/view fixes, security, reports, tests, and migrations. Use when the target version is Odoo 14.0 or when manifest/config detection resolves to 14.0.
---

# Odoo 14.0

Use this skill only for Odoo 14.0 work.

## Domain map

| Topic | File | When to use |
|---|---|---|
| Version deltas | `../odoo-upgrade/references/odoo-version-knowledge-14.md` | Confirm legacy syntax and limits |
| Module scaffolding | `../odoo-module-generation/references/odoo-module-generator-14.md` | New module, manifest, install order |
| Models | `../odoo-models/references/odoo-model-patterns-14.md` | ORM logic and field design |
| Security | `../odoo-security/references/odoo-security-guide-14.md` | ACL, groups, record rules |
| Views and reports | `../odoo-views/references/xml-view-patterns.md`, `../odoo-views/references/report-patterns.md` | XML, actions, menus, reports |
| Integrations | `../odoo-integrations/references/controller-api-patterns.md`, `../odoo-integrations/references/import-export-patterns.md` | Controllers, APIs, import/export, attachments |
| Automation | `../odoo-automation/references/cron-automation-patterns.md`, `../odoo-automation/references/sequence-numbering-patterns.md` | Cron, mail, sequence flows |
| Business flows | `../odoo-business-domains/references/sale-crm-patterns.md`, `../odoo-business-domains/references/stock-inventory-patterns.md` | Reuse core business-domain patterns |
| Operations | `../odoo-operations/references/config-settings-patterns.md`, `../odoo-operations/references/logging-debugging-patterns.md` | Settings, debugging, operational checks |
| Quality | `../odoo-quality/references/odoo-test-patterns.md`, `../odoo-quality/references/odoo-performance-guide.md` | Tests, review, performance |
| Troubleshooting | `../odoo-upgrade/references/odoo-troubleshooting-guide.md` | Debugging and recovery |

## Critical version notes

- Expect older API and XML patterns before applying later-version fixes.
- Review decorators, tracking fields, and view visibility against Odoo 14 references first.
