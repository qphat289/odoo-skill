# Odoo Model Patterns - Version Dispatcher

Use this file as the routing entrypoint for version-specific model implementation guidance.

## Mandatory version matching

Use the model-pattern file that matches the target Odoo version. Mixing model patterns across versions can introduce ORM bugs, deprecated APIs, or incorrect CRUD behavior.

Before implementing model code:
1. Identify the target Odoo version.
2. Load the matching version-specific model-pattern file.
3. Load shared rules when manifest ordering, security, or style also matter.

## Version-specific files

| Target Version | File to Use | Status |
|----------------|-------------|--------|
| Odoo 14.0 | `odoo-model-patterns-14.md` | Legacy |
| Odoo 15.0 | `odoo-model-patterns-15.md` | Legacy |
| Odoo 16.0 | `odoo-model-patterns-16.md` | Supported |
| Odoo 17.0 | `odoo-model-patterns-17.md` | Supported |
| Odoo 18.0 | `odoo-model-patterns-18.md` | Current |
| Odoo 19.0 | `odoo-model-patterns-19.md` | Current |
| All versions | `odoo-model-patterns-all.md` | Shared concepts |

## Migration guides

| Migration Path | File |
|----------------|------|
| 14.0 -> 15.0 | `odoo-model-patterns-14-15.md` |
| 15.0 -> 16.0 | `odoo-model-patterns-15-16.md` |
| 16.0 -> 17.0 | `odoo-model-patterns-16-17.md` |
| 17.0 -> 18.0 | `odoo-model-patterns-17-18.md` |
| 18.0 -> 19.0 | `odoo-model-patterns-18-19.md` |

## Quick reference by version

### v14
- `@api.multi` still appears in legacy code
- `track_visibility='onchange'`
- Single-record `create(vals)`

### v15
- `@api.multi` removed
- `tracking=True` replaces `track_visibility`

### v16
- `Command` class becomes the preferred x2many pattern
- `@api.model_create_multi` should already be preferred

### v17
- `@api.model_create_multi` mandatory in normal create flows
- ORM and view expectations assume newer patterns

### v18
- `_check_company_auto = True` for company-aware models
- `check_company=True` on appropriate relations
- Type hints recommended
- `SQL()` builder preferred

### v19
- Type hints preferred in maintained code
- `SQL()` preferred for new or refactored raw SQL

## Version detection hints

| Indicator | Version |
|-----------|---------|
| `@api.multi` decorator | 14.0 |
| `track_visibility` | 14.0 |
| `tracking=True` | 15.0+ |
| Tuple syntax for x2many | 14.0-15.0 |
| `Command` class | 16.0+ |
| `_check_company_auto` | 18.0+ |
| Type hints on fields or methods | 18.0+ |
| Full type annotations | 19.0+ |

## Related sources

- `odoo-version-routing.md`
- `rules/coding-style.md`
- `rules/security.md`

Always load the matching version-specific file before implementing model patterns.
