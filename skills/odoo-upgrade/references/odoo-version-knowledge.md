# Odoo Version Knowledge - Master Reference

Use this file as the routing reference for version-aware Odoo work.

## Core rule

Always identify the target Odoo version before generating or reviewing code.
Patterns that are valid in one version may be deprecated or broken in another.

## Version support snapshot

| Version | Status | Python guidance |
|---------|--------|-----------------|
| 14.0 | Legacy | 3.6+ |
| 15.0 | Legacy | 3.8+ |
| 16.0 | Supported | 3.8+ |
| 17.0 | Supported | 3.10+ |
| 18.0 | Current | 3.11+ common target |
| 19.0 | Current | official docs still state 3.10+ minimum |

## Version-specific files

| Version | File |
|---------|------|
| Odoo 14.0 | `odoo-version-knowledge-14.md` |
| Odoo 15.0 | `odoo-version-knowledge-15.md` |
| Odoo 16.0 | `odoo-version-knowledge-16.md` |
| Odoo 17.0 | `odoo-version-knowledge-17.md` |
| Odoo 18.0 | `odoo-version-knowledge-18.md` |
| Odoo 19.0 | `odoo-version-knowledge-19.md` |

## Key transitions

### v14 -> v15
- remove `@api.multi`
- replace `track_visibility` with `tracking`

### v15 -> v16
- adopt `Command` for x2many work
- move assets into the manifest `assets` key

### v16 -> v17
- remove `attrs` and `states` from XML views
- use `@api.model_create_multi`

### v17 -> v18
- adopt `_check_company_auto` and `check_company=True`
- prefer `SQL()` for new raw SQL
- start adding type hints where useful

### v18 -> v19
- migrate `_sql_constraints` toward `models.Constraint(...)`
- keep adding type hints in maintained code
- verify frontend assumptions against the current `19.0` source tree
- prefer `SQL()` for new or heavily refactored raw SQL

## Version detection hints

| Indicator | Version hint |
|-----------|--------------|
| `@api.multi` | 14.0 |
| `track_visibility` | 14.0 |
| `tracking=True` | 15.0+ |
| `Command` | 16.0+ |
| `attrs=` in views | 14.0-16.0 |
| direct `invisible` / `readonly` | 17.0+ |
| `_check_company_auto` | 18.0+ |
| `SQL()` builder | 18.0+ |
| widespread type hints | 18.0+ |

## Agent workflow

1. Determine the target version.
2. Load the matching version-specific file.
3. Load only the relevant domain references.
4. Verify uncertain syntax against official docs or the matching upstream branch.

Never use the 19.0 line as a place for unverified hard rules.
