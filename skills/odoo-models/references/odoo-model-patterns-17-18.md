# Odoo Model Migration Guide: 17.0 -> 18.0

Focus areas:
- Company checks
- `SQL()` builder adoption
- Type hints

## Summary

| Feature | 17.0 | 18.0 | Recommendation |
|---------|------|------|----------------|
| `_check_company_auto` | Not used by default | Available | Adopt on company-aware models |
| `check_company` | Rare | Preferred | Add on relevant relations |
| `SQL()` builder | Optional | Recommended | Migrate raw SQL |
| Type hints | Optional | Recommended | Add progressively |

## Automatic company validation

Before:

```python
class MyModel(models.Model):
    _name = 'my.model'

    company_id = fields.Many2one('res.company')
    partner_id = fields.Many2one('res.partner')

    @api.constrains('partner_id', 'company_id')
    def _check_partner_company(self):
        for record in self:
            if record.partner_id.company_id and record.partner_id.company_id != record.company_id:
                raise ValidationError(_("Partner company must match record company."))
```

After:

```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

## SQL builder

Before:

```python
def _get_statistics(self):
    query = """
        SELECT partner_id, SUM(amount) as total
        FROM %s
        WHERE company_id = %%s AND state = %%s
        GROUP BY partner_id
    """ % self._table
    self.env.cr.execute(query, (self.env.company.id, 'confirmed'))
    return self.env.cr.dictfetchall()
```

After:

```python
from odoo.tools import SQL

def _get_statistics(self):
    query = SQL(
        """
        SELECT partner_id, SUM(amount) as total
        FROM %s
        WHERE company_id = %s AND state = %s
        GROUP BY partner_id
        """,
        SQL.identifier(self._table),
        self.env.company.id,
        'confirmed',
    )
    self.env.cr.execute(query)
    return self.env.cr.dictfetchall()
```

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

## Rule-domain update

Before:

```xml
<field name="domain_force">[
    ('company_id', 'in', company_ids)
]</field>
```

After:

```xml
<field name="domain_force">[
    ('company_id', 'in', company_ids)
]</field>
```

## Migration checklist

- [ ] Add `_check_company_auto = True` to company-aware models
- [ ] Add `check_company=True` to relevant Many2one fields
- [ ] Remove duplicated manual company validation
- [ ] Keep record-rule `company_ids`; use `allowed_company_ids` only in Python/context when active company scope must be propagated
- [ ] Start converting raw SQL to `SQL()`
- [ ] Add type hints to high-value methods first
