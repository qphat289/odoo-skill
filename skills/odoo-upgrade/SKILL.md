---
name: odoo-upgrade
description: Domain skill for Odoo version deltas, upgrade planning, migration references, and troubleshooting across Odoo 14-19.
---

# Odoo Upgrade

Use this skill when the task is about version differences, migration planning, troubleshooting after upgrade, or refactoring from one Odoo version to another.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Shared routing | `references/odoo-version-routing.md` | Decide which version files to load |
| Version knowledge | `references/odoo-version-knowledge-<version>.md` | Syntax and API deltas for one version |
| Upgrade deltas | `references/odoo-version-knowledge-<from>-<to>.md` | Cross-version changes |
| Migration patterns | `references/data-migration-patterns.md` | Data migration and hooks |
| Troubleshooting | `references/odoo-troubleshooting-guide.md` | Tracebacks, recovery, debugging |
| Upgrade checkpoints | `references/odoo-upgrade-breakpoints.md` | Common breakage points |

## Rules

1. Always state source version and target version before loading upgrade references.
2. Pair with `odoo-module-generation`, `odoo-models`, and `odoo-security` for migration execution work.
3. Use `odoo-quality` at the end for regression review and test planning.
