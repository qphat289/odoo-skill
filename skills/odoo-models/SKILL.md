---
name: odoo-models
description: Domain skill for Odoo ORM, models, fields, inheritance, compute logic, domains, and CRUD patterns across Odoo 14-19.
---

# Odoo Models

Use this skill when the task is mainly about Python models, ORM methods, field definitions, business logic, or domain expressions.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Shared overview | `references/odoo-model-patterns.md` | Pick the right version file |
| Field types | `references/field-type-reference.md` | Choosing field classes and parameters |
| Decorators | `references/decorator-decision-patterns.md` | `@api.model_create_multi`, `@api.depends`, `@api.ondelete`, `@api.onchange` |
| Computed fields | `references/computed-field-patterns.md` | Compute, inverse, store, depends |
| Constraints | `references/constraint-patterns.md` | SQL and Python validation |
| Inheritance | `references/inheritance-patterns.md` | `_inherit`, delegation, extension |
| Mixins | `references/mixin-composition-patterns.md` | Chatter, activities, portal, alias, rating, avatars |
| Advanced ORM performance | `references/advanced-orm-performance-patterns.md` | Prefetch, batching, `_read_group`, cache safety, query scaling |
| Version files | `references/odoo-model-patterns-<version>.md` | Version-specific ORM patterns |

## Rules

1. Load the exact version file before writing model code.
2. Use this skill together with `odoo-security` when access rules affect the model.
3. For XML/UI behavior, switch to `odoo-views` instead of overloading model references.
4. When performance work touches cache, batching, or query-shape decisions, also load `references/advanced-orm-performance-patterns.md`.
