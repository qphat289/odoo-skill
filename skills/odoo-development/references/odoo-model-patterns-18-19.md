# Odoo Model Migration Guide: 18.0 -> 19.0

Focus areas:
- Mandatory type hints
- Mandatory `SQL()` builder
- Higher confidence around newer model conventions

Treat v19 patterns as provisional until verified against upstream.

## Summary

| Feature | 18.0 | 19.0 | Action |
|---------|------|------|--------|
| Type hints | Recommended | Mandatory | Must add |
| `SQL()` builder | Recommended | Mandatory | Must migrate |
| Raw SQL strings | Deprecated | Removed | Must migrate |

## Type hints

Before:

```python
def calculate_totals(self, options=None):
    options = options or {}
    results = []
    for record in self:
        total = sum(record.line_ids.mapped('amount'))
        if options.get('include_tax'):
            total *= 1.21
        results.append({'id': record.id, 'total': total})
    return results
```

After:

```python
from __future__ import annotations
from typing import Any, Optional

def calculate_totals(
    self,
    options: Optional[dict[str, Any]] = None,
) -> list[dict[str, Any]]:
    options = options or {}
    results: list[dict[str, Any]] = []
    for record in self:
        total: float = sum(record.line_ids.mapped('amount'))
        if options.get('include_tax'):
            total *= 1.21
        results.append({'id': record.id, 'total': total})
    return results
```

## CRUD signatures

```python
from __future__ import annotations
from typing import Any, Optional

@api.model_create_multi
def create(self, vals_list: list[dict[str, Any]]) -> 'MyModel':
    return super().create(vals_list)

def write(self, vals: dict[str, Any]) -> bool:
    return super().write(vals)

def unlink(self) -> bool:
    return super().unlink()

def copy(self, default: Optional[dict[str, Any]] = None) -> 'MyModel':
    return super().copy(default)
```

## SQL builder

Before:

```python
query = """
    SELECT id, name, amount
    FROM %s
    WHERE company_id = %s
    ORDER BY create_date DESC
""" % (self._table, self.env.company.id)
self.env.cr.execute(query)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    """
    SELECT id, name, amount
    FROM %s
    WHERE company_id = %s
    ORDER BY %s
    """,
    SQL.identifier(self._table),
    self.env.company.id,
    SQL('create_date DESC'),
)
self.env.cr.execute(query)
```

## Migration checklist

- [ ] Add `from __future__ import annotations`
- [ ] Add method type hints
- [ ] Add field type hints where the project expects them
- [ ] Replace raw SQL with `SQL()`
- [ ] Re-test custom ORM-heavy code paths
