# Odoo Version Knowledge - 18.0

Release profile:
- Release line: 18.0
- Python: 3.11+ required, 3.12 recommended
- OWL: 2.x

## Overview

Odoo 18.0 focuses on:
- Multi-company improvements with automatic validation
- SQL safety improvements with `SQL()` builder
- Type hint preparation for stricter later versions
- Performance refinements

## New features in v18

### `_check_company_auto`

Automatic company consistency validation:

```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

### `SQL()` builder

Safe SQL query construction:

```python
from odoo.tools import SQL

query = SQL(
    "SELECT * FROM %s WHERE company_id = %s",
    SQL.identifier(self._table),
    self.env.company.id,
)
```

### Type hints

Recommended for business methods:

```python
def calculate_total(self, include_tax: bool = True) -> float:
    return sum(self.mapped('amount'))
```

### `allowed_company_ids` in record rules

```xml
<field name="domain_force">[
    ('company_id', 'in', allowed_company_ids)
]</field>
```

## Breaking changes in v18

| Feature | Change | Action Required |
|---------|--------|-----------------|
| `request.not_found()` | Must be raised, not returned | Replace `return request.not_found()` with `raise request.not_found()` |

### `request.not_found()` behavior

```python
# Wrong in v18
if not record.exists():
    return request.not_found()

# Correct in v18
if not record.exists():
    raise request.not_found()
```

## Deprecations in v18

| Feature | Status | Replacement | Deadline |
|---------|--------|-------------|----------|
| Raw SQL strings | Deprecated | `SQL()` builder | v19 |
| Methods without type hints | Deprecated | Add type hints | v19 |
| `company_ids` in rules | Deprecated | `allowed_company_ids` | - |

## Required patterns in v18

### Model definition

```python
class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _check_company_auto = True

    company_id = fields.Many2one(
        'res.company',
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )
```

### Create method

```python
@api.model_create_multi
def create(self, vals_list: list[dict]) -> 'MyModel':
    return super().create(vals_list)
```

### View visibility

```xml
<button name="action_confirm"
        invisible="state != 'draft'"
        readonly="locked"/>
```

## GitHub verification URLs

Verify against official source:

| Component | URL |
|-----------|-----|
| Base models | `github.com/odoo/odoo/tree/18.0/odoo/addons/base/models` |
| Web module | `github.com/odoo/odoo/tree/18.0/addons/web` |
| OWL components | `github.com/odoo/odoo/tree/18.0/addons/web/static/src` |
| Mail thread | `github.com/odoo/odoo/tree/18.0/addons/mail/models` |
| Sale module | `github.com/odoo/odoo/tree/18.0/addons/sale/models` |

## Field patterns

### Standard fields

```python
name = fields.Char(string='Name', required=True, tracking=True)
active = fields.Boolean(default=True)
sequence = fields.Integer(default=10)
state = fields.Selection([...], default='draft', tracking=True, copy=False)
```

### Relational fields

```python
partner_id = fields.Many2one('res.partner', check_company=True)
product_id = fields.Many2one('product.product', check_company=True)
warehouse_id = fields.Many2one('stock.warehouse', check_company=True)
```

### Monetary fields

```python
currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)
amount = fields.Monetary(currency_field='currency_id')
```

## Security patterns

### Access rights

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,model_my_model,group_user,1,1,1,0
access_my_model_manager,my.model.manager,model_my_model,group_manager,1,1,1,1
```
