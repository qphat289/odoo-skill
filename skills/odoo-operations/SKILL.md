---
name: odoo-operations
description: Domain skill for Odoo settings, validation, debugging, error handling, editions, i18n, and operational implementation guidance across Odoo 14-19.
---

# Odoo Operations

Use this skill when the task is about operational hardening: configuration, validation rules, diagnostics, translation, edition differences, or end-to-end execution examples.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Config settings | `references/config-settings-patterns.md` | `res.config.settings`, parameters, setup flows |
| Validation schema | `references/input-validation-schema.md` | Input contracts, validation rules, preflight checks |
| Error handling | `references/error-handling-patterns.md` | Exceptions, safe failure paths, recovery strategy |
| Transaction safety | `references/transaction-safety-patterns.md` | Savepoints, retries, rollbacks, raw SQL safety |
| Logging and debugging | `references/logging-debugging-patterns.md` | Logs, tracing, diagnostics, debugging patterns |
| Internationalization | `references/translation-i18n-patterns.md` | Translations, terms, i18n-safe implementation |
| Odoo editions | `references/odoo-editions.md` | Community vs Enterprise constraints |
| End-to-end examples | `references/end-to-end-examples.md` | High-value examples that connect multiple domains |

## Rules

1. Pair this skill with the active version skill when configuration or diagnostics depend on version-specific behavior.
2. Use `odoo-integrations` for API or controller specifics rather than overloading this skill.
3. Use `odoo-quality` when the operational task should end in explicit testing or review steps.
