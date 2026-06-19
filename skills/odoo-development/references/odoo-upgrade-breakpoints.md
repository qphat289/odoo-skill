# Odoo Upgrade Breakpoints

Use this file as the compact central upgrade matrix for migration planning.

## Upgrade hop matrix

### 14.0 -> 15.0

- Remove `@api.multi`
- Replace `track_visibility` with `tracking`
- Review asset bundle changes
- Review OWL introduction for frontend work

### 15.0 -> 16.0

- Prefer `Command` for x2many operations
- Start phasing out older view patterns and legacy JS assumptions
- Review OWL 2.x references when frontend code exists

### 16.0 -> 17.0

- Replace `attrs` with direct XML expressions
- Update `create()` patterns to `@api.model_create_multi`
- Re-check view/list/search syntax and JS import patterns

### 17.0 -> 18.0

- Add `_check_company_auto` and `check_company=True` where applicable
- Move rule context toward `allowed_company_ids`
- Prefer SQL builder and add type hints where practical

### 18.0 -> 19.0

- Review mandatory typing expectations
- Replace remaining raw SQL with `SQL()` builder
- Migrate SQL constraints toward `models.Constraint()`
- Re-check `res.users` group assignment patterns
- Review OWL 3.x adjustments

## Use rules

- Treat this file as the starting matrix, not the final authority.
- For each hop, read:
  - `odoo-version-knowledge-{source}-{target}.md`
  - `odoo-module-generator-{source}-{target}.md`
  - `odoo-model-patterns-{source}-{target}.md`
  - `odoo-security-guide-{source}-{target}.md`
