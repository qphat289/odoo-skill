---
name: odoo-views
description: Domain skill for Odoo XML views, actions, menus, QWeb reports, widgets, and wizard UI patterns across Odoo 14-19.
---

# Odoo Views

Use this skill when the task is about XML views, actions, menus, reports, wizard UI, widgets, or QWeb templates.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| XML views | `references/xml-view-patterns.md` | Form, list, search, kanban, inheritance |
| Reports | `references/report-patterns.md` | QWeb reports and printable output |
| Actions and menus | `references/action-patterns.md`, `references/menu-navigation-patterns.md` | `ir.actions.*`, menus, navigation |
| Wizards | `references/wizard-patterns.md` | Dialogs and transient flows |
| Widgets and QWeb | `references/widget-field-patterns.md`, `references/qweb-template-patterns.md` | Field widgets and templates |

## Rules

1. Use exact version notes from the active version skill before copying XML syntax.
2. For business logic, switch back to `odoo-models`; for access control, switch to `odoo-security`.
3. Use `odoo-module-generation` for manifest ordering when views depend on data or security files.
