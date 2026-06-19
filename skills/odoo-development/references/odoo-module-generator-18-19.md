# Odoo Module Migration Guide: 18.0 -> 19.0

This guide covers module-level changes to review when upgrading from Odoo 18.0 to 19.0.
Treat v19 guidance as provisional until verified against the current upstream branch.

## Breaking-change summary

| Component | 18.0 | 19.0 | Action Required |
|-----------|------|------|-----------------|
| Type hints | Recommended | Mandatory | Must add |
| `SQL()` builder | Recommended | Mandatory | Must migrate |
| Raw SQL strings | Deprecated | Removed | Must migrate |
| OWL | 2.x | 3.x | Update frontend components |
| Python | 3.11+ | 3.12+ expected | Verify runtime |

## Type hints

Before:

```python
def calculate_total(self, include_tax=True, discount=None):
    discount = discount or 0
    total = sum(self.mapped('amount'))
    if include_tax:
        total *= 1.21
    return total - discount
```

After:

```python
from typing import Optional

def calculate_total(
    self,
    include_tax: bool = True,
    discount: Optional[float] = None,
) -> float:
    discount = discount or 0.0
    total = sum(self.mapped('amount'))
    if include_tax:
        total *= 1.21
    return total - discount
```

## SQL builder

Before:

```python
query = """
    SELECT id, name FROM %s WHERE company_id = %s
""" % (self._table, self.env.company.id)
self.env.cr.execute(query)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    """
    SELECT id, name FROM %s WHERE company_id = %s
    """,
    SQL.identifier(self._table),
    self.env.company.id,
)
self.env.cr.execute(query)
```

## OWL 3.x reminder

Review any custom components for:
- updated hook usage
- service access patterns
- lifecycle expectations
- newer template assumptions

## Migration checklist

- [ ] Add method type hints
- [ ] Add field type hints where the codebase expects them
- [ ] Replace all raw SQL with `SQL()`
- [ ] Review custom OWL components for 3.x compatibility
- [ ] Re-test reporting, dashboards, and custom queries
- [ ] Verify against upstream before final release
