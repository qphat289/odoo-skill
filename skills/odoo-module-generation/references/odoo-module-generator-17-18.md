# Odoo Module Migration Guide: 17.0 -> 18.0

This guide covers the practical module-level changes to review when upgrading from Odoo 17.0 to 18.0.

## Breaking-change summary

| Component | 17.0 | 18.0 | Action Required |
|-----------|------|------|-----------------|
| `_check_company_auto` | Optional | Recommended | Add to suitable models |
| `check_company` | Optional | Recommended | Add to relations |
| `SQL()` builder | Optional | Recommended | Migrate raw SQL |
| Type hints | Optional | Recommended | Add where useful |
| Raw SQL strings | Allowed | Deprecated | Plan migration |

## Company-check automation

Before:

```python
class MyModel(models.Model):
    _name = 'my.model'

    company_id = fields.Many2one('res.company')
    partner_id = fields.Many2one('res.partner')

    def write(self, vals):
        if 'partner_id' in vals:
            partner = self.env['res.partner'].browse(vals['partner_id'])
            if partner.company_id and partner.company_id != self.company_id:
                raise UserError(_("Partner company mismatch."))
        return super().write(vals)
```

After:

```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

## SQL builder pattern

Before:

```python
def _get_statistics(self):
    query = """
        SELECT partner_id, SUM(amount) as total
        FROM %s
        WHERE company_id = %s AND state = '%s'
        GROUP BY partner_id
    """ % (self._table, self.env.company.id, 'confirmed')
    self.env.cr.execute(query)
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
def process_partner(self, partner_id, options=None):
    partner = self.env['res.partner'].browse(partner_id)
    options = options or {}
    return partner.name
```

After:

```python
from typing import Any, Optional

def process_partner(
    self,
    partner_id: int,
    options: Optional[dict[str, Any]] = None,
) -> str:
    partner = self.env['res.partner'].browse(partner_id)
    options = options or {}
    return partner.name
```

## Multi-company updates

Keep `company_ids` in record rules. If business logic must forward the active company scope, use `allowed_company_ids` in Python/context instead:

```xml
<field name="domain_force">[
    '|',
    ('company_id', '=', False),
    ('company_id', 'in', company_ids)
]</field>
```

## Migration checklist

- [ ] Review all company-aware models
- [ ] Add `_check_company_auto = True` where appropriate
- [ ] Add `check_company=True` on matching relations
- [ ] Keep record rules on `company_ids`
- [ ] Use `allowed_company_ids` only in Python/context where active company scope must be propagated
- [ ] Review and migrate raw SQL
- [ ] Add type hints to key methods
- [ ] Re-test multi-company and reporting flows
