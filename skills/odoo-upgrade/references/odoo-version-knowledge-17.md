# Odoo Version Knowledge - 17.0

Release profile:
- Release: October 2023
- Python: 3.10 and 3.11
- PostgreSQL: 13, 14, 15
- Frontend: OWL 2.x
- Verify against: `https://github.com/odoo/odoo/tree/17.0`

## Overview

Odoo 17.0 is the version where several older conventions become hard breaks rather than warnings.

Key points:
- `attrs` is removed from views
- `@api.model_create_multi` becomes the normal create pattern
- newer XML expression syntax is required
- frontend asset bundles should be checked again before copying v14-v16 bundle names such as `web.assets_common`

## Breaking changes from v16

### `attrs` removed

```xml
<!-- Breaks in v17 -->
<field name="partner_id"
       attrs="{'invisible': [('state', '=', 'draft')]}"/>

<!-- Required in v17 -->
<field name="partner_id"
       invisible="state == 'draft'"/>
```

### `@api.model_create_multi` mandatory

```python
# Breaks in v17
@api.model
def create(self, vals):
    return super().create(vals)

# Required in v17
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

## Technical stack

- Python 3.10+ with 3.11 preferred
- PostgreSQL 13+
- OWL 2.x
- ES modules on the frontend

## Version-specific model pattern

```python
from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence, id desc'

    name = fields.Char(required=True, tracking=True, index='trigram')
    code = fields.Char(index=True, copy=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True, index=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        'res.company',
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )
    user_id = fields.Many2one(
        'res.users',
        default=lambda self: self.env.user,
        tracking=True,
    )
    line_ids = fields.One2many('my.model.line', 'model_id', copy=True)
```

## CRUD pattern

```python
@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        if not vals.get('code'):
            vals['code'] = self.env['ir.sequence'].next_by_code('my.model')

    records = super().create(vals_list)

    for record in records:
        record.message_post(body=_("Record created."))

    return records

def write(self, vals):
    if vals.get('state') == 'confirmed':
        for record in self:
            if not record.line_ids:
                raise UserError(_("Add at least one line."))
    return super().write(vals)

def unlink(self):
    for record in self:
        if record.state not in ('draft', 'cancelled'):
            raise UserError(_("Only draft or cancelled records can be deleted."))
    return super().unlink()
```

## XML visibility syntax in v17

```xml
<button name="action_confirm"
        type="object"
        string="Confirm"
        invisible="state != 'draft'"/>

<field name="amount"
       readonly="state != 'draft'"
       required="state == 'confirmed'"/>

<group invisible="not show_details">
    <field name="detail"/>
</group>
```

## Frontend and asset note

- Treat v17 as a frontend packaging boundary as well as a view-syntax boundary.
- Do not assume older bundle targets like `web.assets_common` remain the right destination for custom assets.
- For backend OWL work, the safe default is usually `web.assets_backend` with JS, XML, and SCSS declared together.

## Practical guidance

- Treat v17 as the hard boundary for modern XML visibility syntax.
- Avoid carrying `attrs` or single-record `create()` assumptions into v17 code.
- Verify any uncertain UI or ORM pattern against official v17 source before finalizing implementation.
