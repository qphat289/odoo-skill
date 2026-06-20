# Odoo Module Migration Guide: 18.0 -> 19.0

This guide covers module-level changes to review when upgrading from Odoo 18.0 to 19.0.
Use it as a conservative generator guide, not as a source for hard claims that upstream does not explicitly make.

## Breaking-change summary

| Component | 18.0 | 19.0 | Generator stance |
|-----------|------|------|------------------|
| Type hints | Recommended | Preferred more broadly | Add on new or touched code |
| `SQL()` builder | Recommended | Preferred for new/refactored SQL | Migrate opportunistically |
| SQL constraints | `_sql_constraints` common | `models.Constraint(...)` preferred | Migrate |
| OWL/frontend | v18 patterns | Verify current 19.0 web source | Review custom components |
| Python | 3.11+ common target | Official docs state 3.10+ minimum | Verify runtime |

## Type hints

Before:

```python
def calculate_total(self, include_tax=True, discount=None):
    discount = discount or 0
    total = sum(self.mapped("amount"))
    if include_tax:
        total *= 1.21
    return total - discount
```

After:

```python
def calculate_total(
    self,
    include_tax: bool = True,
    discount: float | None = None,
) -> float:
    discount = discount or 0.0
    total = sum(self.mapped("amount"))
    if include_tax:
        total *= 1.21
    return total - discount
```

## SQL builder

Before:

```python
self.env.cr.execute(
    "SELECT id, name FROM my_model WHERE company_id = %s",
    [self.env.company.id],
)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    "SELECT id, name FROM %s WHERE company_id = %s",
    SQL.identifier(self._table),
    self.env.company.id,
)
self.env.cr.execute(query)
```

Use the `SQL()` form as the preferred pattern for new or refactored low-level SQL. Do not claim that every old parametrized `execute()` becomes invalid in 19.0.

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

## Frontend reminder

Review custom frontend code for:
- current `@odoo-module` usage
- `@web` service and registry patterns
- hooks and lifecycle usage seen in the 19.0 source tree

Do not describe 19.0 as an automatic OWL major-version rewrite unless you have re-verified upstream.

## Migration checklist

- [ ] Add method type hints where the code is new, touched, or high-value for maintenance
- [ ] Prefer `SQL()` for new or risky raw SQL
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Review custom frontend components against the current `19.0` source
- [ ] Re-test reports, dashboards, and custom queries
- [ ] Verify runtime assumptions before release
