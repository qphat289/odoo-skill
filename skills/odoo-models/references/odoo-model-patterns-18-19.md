# Odoo Model Migration Guide: 18.0 -> 19.0

Focus areas:
- stronger type-hint adoption
- preferred `SQL()` usage in new SQL-heavy code
- verified move toward `models.Constraint(...)`

Use this file to guide model upgrades without overstating unverified breakages.

## Summary

| Feature | 18.0 | 19.0 | Action |
|---------|------|------|--------|
| Type hints | Recommended | Stronger adoption | Add on new or touched methods |
| `SQL()` builder | Recommended | Preferred for new/refactored SQL | Migrate opportunistically |
| SQL constraints | `_sql_constraints` common | `models.Constraint(...)` preferred | Migrate |

## Type hints

Before:

```python
def calculate_totals(self, options=None):
    options = options or {}
    results = []
    for record in self:
        total = sum(record.line_ids.mapped("amount"))
        if options.get("include_tax"):
            total *= 1.21
        results.append({"id": record.id, "total": total})
    return results
```

After:

```python
from typing import Any

def calculate_totals(
    self,
    options: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    options = options or {}
    results: list[dict[str, Any]] = []
    for record in self:
        total = sum(record.line_ids.mapped("amount"))
        if options.get("include_tax"):
            total *= 1.21
        results.append({"id": record.id, "total": total})
    return results
```

## CRUD signatures

```python
from typing import Any

@api.model_create_multi
def create(self, vals_list: list[dict[str, Any]]):
    return super().create(vals_list)

def write(self, vals: dict[str, Any]) -> bool:
    return super().write(vals)
```

## SQL builder

Before:

```python
self.env.cr.execute(
    "SELECT id, name, amount FROM my_model WHERE company_id = %s",
    [self.env.company.id],
)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    "SELECT id, name, amount FROM %s WHERE company_id = %s",
    SQL.identifier(self._table),
    self.env.company.id,
)
self.env.cr.execute(query)
```

## Constraint migration

```python
_amount_positive = models.Constraint(
    "CHECK(amount >= 0)",
    "Amount must be positive.",
)
```

## Migration checklist

- [ ] Add method type hints where the code is new, touched, or review-critical
- [ ] Prefer `SQL()` in new or high-risk raw SQL code
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Re-test ORM-heavy flows on the target build
