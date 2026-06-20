# Odoo Module Generator - Version Dispatcher

Use this file as the routing entrypoint for module generation references.

## Mandatory version matching

You must use the version-specific module generator that matches the target Odoo version. Using patterns from the wrong version can introduce deprecated code, broken syntax, or security issues.

Before generating any module code:
1. Identify the target Odoo version.
2. Load the matching version-specific generator file.
3. Load shared rules and ordering references when relevant.

## Version-specific files

| Target Version | File to Use | Status |
|----------------|-------------|--------|
| Odoo 14.0 | `odoo-module-generator-14.md` | Legacy |
| Odoo 15.0 | `odoo-module-generator-15.md` | Legacy |
| Odoo 16.0 | `odoo-module-generator-16.md` | Supported |
| Odoo 17.0 | `odoo-module-generator-17.md` | Supported |
| Odoo 18.0 | `odoo-module-generator-18.md` | Current |
| Odoo 19.0 | `odoo-module-generator-19.md` | Current |
| All versions | `odoo-module-generator-all.md` | Shared concepts |

## Migration guides

When upgrading modules between versions:

| Migration Path | File |
|----------------|------|
| 14.0 -> 15.0 | `odoo-module-generator-14-15.md` |
| 15.0 -> 16.0 | `odoo-module-generator-15-16.md` |
| 16.0 -> 17.0 | `odoo-module-generator-16-17.md` |
| 17.0 -> 18.0 | `odoo-module-generator-17-18.md` |
| 18.0 -> 19.0 | `odoo-module-generator-18-19.md` |

## How to use

### Step 1: Identify target version

If the version is not specified, ask before proceeding:

```text
What Odoo version should I target? (14.0, 15.0, 16.0, 17.0, 18.0, 19.0)
```

### Step 2: Load the correct file

Examples:

```text
# Odoo 18.0 project
Read: skills/odoo-module-generation/references/odoo-module-generator-18.md

# Upgrade from 17.0 to 18.0
Read: skills/odoo-module-generation/references/odoo-module-generator-17-18.md
```

### Step 3: Gather input parameters

Required parameters:

| Parameter | Type | Required | Example |
|-----------|------|----------|---------|
| `module_name` | string | Yes | `custom_inventory` |
| `module_description` | string | Yes | `Custom inventory tracking` |
| `odoo_version` | string | Yes | `18.0` |
| `target_apps` | list | No | `['stock', 'sale']` |
| `ui_stack` | string | No | `owl`, `classic`, `hybrid` |
| `multi_company` | boolean | No | `true` |
| `multi_currency` | boolean | No | `false` |
| `security_level` | string | No | `basic`, `advanced`, `audit` |
| `performance_critical` | boolean | No | `false` |
| `custom_models` | list | No | List of model definitions |
| `custom_fields` | list | No | Fields to add to existing models |

### Step 4: Apply version-specific patterns

Only use patterns from the loaded version-specific file. Never mix patterns from different versions.

## Version detection hints

If the version is not explicitly stated, look for these clues in existing code:

| Indicator | Version |
|-----------|---------|
| `@api.multi` decorator | 14.0 |
| `track_visibility` parameter | 14.0 |
| `tracking` parameter | 15.0+ |
| Tuple syntax for x2many | 14.0-15.0 |
| `Command` class usage | 16.0+ |
| `attrs` in views | 14.0-16.0 |
| Direct `invisible` / `readonly` | 17.0+ |
| `_check_company_auto` | 18.0+ |
| Type hints on fields | 18.0+ |
| `SQL()` builder | 18.0+ |
| Full type annotations | 19.0+ |

## Quick reference by version

### v14
- Single-record `create(vals)`
- `track_visibility='onchange'`
- `attrs` in views

### v15
- `@api.multi` removed
- `tracking=True` replaces `track_visibility`
- OWL 1.x introduced

### v16
- `Command` class for x2many
- `attrs` deprecated
- OWL 2.x
- `@api.model_create_multi` recommended

### v17
- `attrs` removed from views
- Direct `invisible` and `readonly`
- `@api.model_create_multi` mandatory

### v18
- `_check_company_auto = True`
- `check_company=True` on fields
- Type hints recommended
- `SQL()` builder recommended
- `company_ids` in record rules; `allowed_company_ids` only in Python/context when the active company scope must be forwarded

### v19
- Prefer type hints in maintained code
- Prefer `SQL()` for new or refactored raw SQL
- Verify frontend assumptions against the current `19.0` source

## Structured output format

Agents should prefer structured output for generated module skeletons:

```json
{
  "module_skeleton": {
    "name": "module_name",
    "version": "18.0.1.0.0",
    "odoo_version": "18.0",
    "files": {
      "__manifest__.py": "...",
      "__init__.py": "...",
      "models/__init__.py": "...",
      "models/model_name.py": "...",
      "views/model_name_views.xml": "..."
    }
  }
}
```

## Related sources

- `odoo-version-routing.md`
- `odoo-manifest-data-order.md`
- `rules/security.md`
- `rules/coding-style.md`

