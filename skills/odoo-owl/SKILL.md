---
name: odoo-owl
description: Domain skill for Odoo OWL components, frontend assets, and web client customization across Odoo 15-19.
---

# Odoo OWL

Use this skill when the task is about OWL components, services, frontend assets, or web client customizations.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Shared overview | `references/odoo-owl-components.md` | Pick the right version file |
| Asset bundles | `references/assets-bundling-patterns.md` | Manifest assets and bundle wiring |
| Version files | `references/odoo-owl-components-<version>.md` | Real OWL patterns per version |
| Upgrade deltas | `references/odoo-owl-components-<from>-<to>.md` | OWL migration and frontend breakages |

## Rules

1. Use this skill only for versions that support the referenced OWL patterns.
2. Pair with `odoo-views` when XML templates and actions are part of the same feature.
3. Pair with `odoo-quality` when frontend changes need test or performance review.
