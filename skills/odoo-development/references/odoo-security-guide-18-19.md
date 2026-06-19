# Odoo Security Migration Guide: 18.0 -> 19.0

Use this guide when upgrading security-sensitive code from Odoo 18.0 to 19.0.
Treat v19 guidance as provisional and verify against upstream before broad rollout.

## Summary

| Component | 18.0 | 19.0 | Migration Priority |
|-----------|------|------|--------------------|
| Type hints | Recommended | Mandatory | Critical |
| `SQL()` builder | Recommended | Mandatory | Critical |
| Python runtime | 3.11+ | 3.12+ expected | High |
| OWL | 2.x | 3.x | Medium |

## Type hints become mandatory

Before:

```python
class MyModel(models.Model):
    _name = 'my.model'

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner')
    line_ids = fields.One2many('my.line', 'parent_id')
```

After:

```python
from __future__ import annotations

class MyModel(models.Model):
    _name = 'my.model'

    name: str = fields.Char(required=True)
    partner_id: int = fields.Many2one('res.partner')
    line_ids: list[int] = fields.One2many('my.line', 'parent_id')
```

## `SQL()` builder becomes mandatory

Before:

```python
self.env.cr.execute(
    "SELECT id FROM my_table WHERE company_id = %s",
    [self.env.company.id]
)
```

After:

```python
from odoo.tools import SQL

query = SQL(
    "SELECT id FROM %(table)s WHERE company_id = %(company_id)s",
    table=SQL.identifier('my_table'),
    company_id=self.env.company.id,
)
self.env.cr.execute(query)
```

## Example migration helper

```python
import re

def add_type_hints(python_content):
    field_patterns = {
        r"(\\w+)\\s*=\\s*fields\\.Char\\(": r"\\1: str = fields.Char(",
        r"(\\w+)\\s*=\\s*fields\\.Text\\(": r"\\1: str = fields.Text(",
        r"(\\w+)\\s*=\\s*fields\\.Boolean\\(": r"\\1: bool = fields.Boolean(",
        r"(\\w+)\\s*=\\s*fields\\.Integer\\(": r"\\1: int = fields.Integer(",
        r"(\\w+)\\s*=\\s*fields\\.Float\\(": r"\\1: float = fields.Float(",
        r"(\\w+)\\s*=\\s*fields\\.Many2one\\(": r"\\1: int = fields.Many2one(",
        r"(\\w+)\\s*=\\s*fields\\.One2many\\(": r"\\1: list[int] = fields.One2many(",
        r"(\\w+)\\s*=\\s*fields\\.Many2many\\(": r"\\1: list[int] = fields.Many2many(",
    }

    content = python_content
    for pattern, replacement in field_patterns.items():
        content = re.sub(pattern, replacement, content)

    if "from __future__ import annotations" not in content:
        content = "from __future__ import annotations\\n" + content

    return content
```

## Migration checklist

- [ ] Add `from __future__ import annotations` where needed
- [ ] Add field and method type hints
- [ ] Replace all raw SQL with `SQL()`
- [ ] Re-verify custom security code on Python 3.12
- [ ] Re-test admin, internal-user, and multi-company flows
