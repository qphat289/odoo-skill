# Odoo Security Migration Guide: 17.0 -> 18.0

Use this guide when upgrading security-sensitive code from Odoo 17.0 to 18.0.

## Summary

This hop is mostly additive rather than destructive.

| Component | 17.0 | 18.0 | Migration Priority |
|-----------|------|------|--------------------|
| Multi-company rule context | `company_ids` | `allowed_company_ids` | High |
| Company validation | Manual checks | `_check_company_auto` and `check_company=True` | High |
| Type hints | Optional | Recommended | Medium |
| SQL builder | Optional | Recommended | Medium |
| View security syntax | Direct expressions | Direct expressions | Low |

## Recommended migrations

### 1. Record rules: `company_ids` -> `allowed_company_ids`

Before:

```xml
<field name="domain_force">[
    '|',
    ('company_id', '=', False),
    ('company_id', 'in', company_ids)
]</field>
```

After:

```xml
<field name="domain_force">[
    '|',
    ('company_id', '=', False),
    ('company_id', 'in', allowed_company_ids)
]</field>
```

### 2. Replace manual company constraints with framework support

Before:

```python
class MyModel(models.Model):
    _name = 'my.model'

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one(
        'res.partner',
        domain="[('company_id', 'in', [company_id, False])]",
    )

    @api.constrains('partner_id', 'company_id')
    def _check_company(self):
        for record in self:
            if record.partner_id.company_id and record.partner_id.company_id != record.company_id:
                raise ValidationError(_("Partner company mismatch"))
```

After:

```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

Migration steps:
1. Add `_check_company_auto = True` on company-aware models.
2. Add `check_company=True` on the relevant relations.
3. Remove manual company constraints when the framework fully covers them.
4. Re-test company switching and cross-company record selection.

### 3. Start adopting type hints

Before:

```python
name = fields.Char(required=True)
partner_id = fields.Many2one('res.partner')
amount = fields.Float()
```

After:

```python
name: str = fields.Char(required=True)
partner_id: int = fields.Many2one('res.partner')
amount: float = fields.Float()
```

### 4. Start adopting `SQL()` builder

Before:

```python
def _get_data(self):
    self.env.cr.execute(
        """
        SELECT id, name FROM my_table
        WHERE company_id = %s AND active = %s
        """,
        [self.env.company.id, True]
    )
    return self.env.cr.dictfetchall()
```

After:

```python
from odoo.tools import SQL

def _get_data(self):
    query = SQL(
        """
        SELECT id, name FROM %(table)s
        WHERE company_id = %(company_id)s AND active = %(active)s
        """,
        table=SQL.identifier('my_table'),
        company_id=self.env.company.id,
        active=True,
    )
    self.env.cr.execute(query)
    return self.env.cr.dictfetchall()
```

## No change required

These remain broadly the same:
- Security groups
- `ir.model.access.csv` format
- Direct-expression view security syntax
- Field-level `groups=...` usage

## Migration checklist

- [ ] Update record rules from `company_ids` to `allowed_company_ids`
- [ ] Add `_check_company_auto = True` where appropriate
- [ ] Add `check_company=True` to relevant relations
- [ ] Remove obsolete manual company constraints
- [ ] Review raw SQL and plan migration to `SQL()`
- [ ] Re-test multi-company behavior
