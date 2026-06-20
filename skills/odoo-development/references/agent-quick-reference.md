# Agent Quick Reference Card

## Version pattern matrix

| Pattern | v14 | v15 | v16 | v17 | v18 | v19 |
|---------|-----|-----|-----|-----|-----|-----|
| `@api.multi` | legacy | removed | removed | removed | removed | removed |
| `tracking=True` | no | yes | yes | yes | yes | yes |
| `attrs=` in views | yes | yes | transitional | removed | removed | removed |
| direct XML expressions | no | no | yes | yes | yes | yes |
| tuple x2many commands | yes | yes | legacy tolerated | legacy tolerated | legacy tolerated | avoid |
| `Command` class | no | no | yes | yes | yes | yes |
| `@api.model_create_multi` | no | optional | recommended | required | required | required |
| `_check_company_auto` | no | no | no | no | preferred | preferred |
| `check_company=True` | no | no | no | no | preferred | preferred |
| `SQL()` builder | no | no | no | no | preferred | preferred for new/refactored SQL |
| type hints | rare | rare | rare | rare | recommended | stronger adoption, not blanket mandatory |

## File loading by task

### Generate
- `odoo-module-generator-{version}.md`
- `odoo-model-patterns-{version}.md`
- `odoo-security-guide-{version}.md`
- `odoo-owl-components-{version}.md` when frontend work exists

### Review
- `odoo-model-patterns-{version}.md`
- `odoo-security-guide-{version}.md`
- `odoo-performance-guide.md`

### Upgrade
- version-hop generator/model/security references
- matching version knowledge reference

## 19.0 rule of thumb

- verified: `models.Constraint(...)` direction
- preferred: type hints, `SQL()` for new SQL, conservative post-create group assignment
- verify upstream: frontend package/version assumptions, runtime tightening
