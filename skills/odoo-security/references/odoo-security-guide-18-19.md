# Odoo Security Migration Guide: 18.0 -> 19.0

Use this guide when upgrading security-sensitive code from Odoo 18.0 to 19.0.
It is intentionally conservative: keep what is verified, soften what upstream does not state as mandatory.

## Summary

| Component | 18.0 | 19.0 | Security stance |
|-----------|------|------|-----------------|
| Type hints | Recommended | Stronger adoption | Add on new or touched code |
| `SQL()` builder | Recommended | Preferred for new/refactored SQL | Migrate high-risk SQL first |
| SQL constraints | `_sql_constraints` common | `models.Constraint(...)` preferred | Migrate |
| Python runtime | 3.11+ common target | Official docs state 3.10+ minimum | Verify deployment |
| Frontend | v18 web patterns | Verify current 19.0 source | Review custom components |

## Type hints

Before:

```python
class MyModel(models.Model):
    _name = "my.model"

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner")
    line_ids = fields.One2many("my.line", "parent_id")
```

After:

```python
class MyModel(models.Model):
    _name = "my.model"

    name: str = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner")
    line_ids = fields.One2many("my.line", "parent_id")
```

Use type hints where they improve readability, review quality, and IDE support. Do not claim that untyped security code is invalid by default in 19.0.

## `SQL()` builder

Before:

```python
self.env.cr.execute(
    "SELECT id FROM my_table WHERE company_id = %s",
    [self.env.company.id],
)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    "SELECT id FROM %s WHERE company_id = %s",
    SQL.identifier("my_table"),
    self.env.company.id,
)
self.env.cr.execute(query)
```

Use this as the preferred security-sensitive raw SQL pattern. Current 19.0 core still contains classic parametrized `execute()` in places, so do not overstate the rule.

## Constraint migration

Before:

```python
_sql_constraints = [
    ("name_company_unique", "UNIQUE(name, company_id)", "Name must be unique."),
]
```

After:

```python
_name_company_unique = models.Constraint(
    "UNIQUE(name, company_id)",
    "Name must be unique.",
)
```

## Migration checklist

- [ ] Add type hints where the security code is new, touched, or review-critical
- [ ] Prefer `SQL()` in new or risky raw SQL
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Re-verify multi-company and permission flows on the target build
- [ ] Verify runtime assumptions before release
