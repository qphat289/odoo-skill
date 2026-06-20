# Odoo Version Knowledge - Complete Reference

This is a compact comparison file for cross-version reasoning.
Use the version-specific references for actual implementation.

## Cross-version matrix

| Topic | 14 | 15 | 16 | 17 | 18 | 19 |
|------|----|----|----|----|----|----|
| `@api.multi` | legacy | removed | removed | removed | removed | removed |
| `tracking=True` | partial transition | yes | yes | yes | yes | yes |
| `attrs` in views | yes | yes | transitional | removed | removed | removed |
| direct XML expressions | no | no | yes | yes | yes | yes |
| `Command` for x2many | no | no | yes | yes | yes | yes |
| `@api.model_create_multi` | no | optional | recommended | required | required | required |
| `_check_company_auto` | no | no | no | no | preferred | preferred |
| `check_company=True` | no | no | no | no | preferred | preferred |
| `SQL()` builder | no | no | no | no | preferred | preferred for new/refactored SQL |
| type hints | rare | rare | rare | rare | recommended | stronger adoption, not blanket mandatory |
| SQL constraints | `_sql_constraints` | `_sql_constraints` | `_sql_constraints` | `_sql_constraints` | `_sql_constraints` | `models.Constraint(...)` preferred |
| frontend stance | legacy/OWL 1 intro | OWL 1 | OWL 2 style | OWL 2 style | OWL 2 style | verify current upstream web patterns |

## Python runtime guidance

| Odoo version | Runtime guidance |
|--------------|------------------|
| 14.0 | 3.6+ |
| 15.0 | 3.8+ |
| 16.0 | 3.8+ |
| 17.0 | 3.10+ |
| 18.0 | 3.11+ common target |
| 19.0 | official docs still state 3.10+ minimum |

## Migration summary

### v14 -> v15
- remove `@api.multi`
- replace `track_visibility`

### v15 -> v16
- adopt `Command`
- move web assets into the manifest `assets` key

### v16 -> v17
- remove `attrs` / `states`
- use direct XML expressions
- use `@api.model_create_multi`

### v17 -> v18
- add multi-company safeguards
- prefer `SQL()` in new raw SQL
- add type hints where helpful

### v18 -> v19
- migrate `_sql_constraints` toward `models.Constraint(...)`
- keep adding type hints in maintained code
- prefer `SQL()` in new or risky raw SQL
- verify frontend and runtime assumptions against upstream
