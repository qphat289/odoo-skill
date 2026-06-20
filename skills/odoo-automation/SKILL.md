---
name: odoo-automation
description: Domain skill for Odoo cron jobs, mail-driven flows, sequences, and background automation patterns across Odoo 14-19.
---

# Odoo Automation

Use this skill when the task involves `ir.cron`, background jobs, automatic notifications, or controlled numbering and sequencing.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Scheduled automation | `references/cron-automation-patterns.md` | `ir.cron`, recurring jobs, unattended logic |
| Mail and notifications | `references/mail-notification-patterns.md` | Chatter, activities, email alerts, mail templates |
| Sequence numbering | `references/sequence-numbering-patterns.md` | Custom sequences, numbering rules, generated references |

## Rules

1. Pair with `odoo-models` when automation mutates business data or computes values.
2. Pair with `odoo-views` when the user-facing workflow needs buttons, statusbars, or wizard triggers.
3. Pair with `odoo-quality` when the automation needs test planning or performance checks.
