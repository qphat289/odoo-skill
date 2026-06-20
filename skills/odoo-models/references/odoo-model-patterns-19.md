# Odoo 19.0 Model Patterns

Use this file for Odoo 19 ORM work only.
It is intentionally conservative: strong on verified model changes, careful on claims that upstream does not make mandatory.

## Key characteristics

| Feature | Odoo 19.0 stance |
|---------|------------------|
| Type hints | Preferred on new or touched methods |
| Raw SQL | Prefer `SQL()` in new or refactored helpers |
| Constraints | Prefer `models.Constraint(...)` |
| X2many commands | `Command` class |
| Multi-company | `_check_company_auto` + `check_company=True` |
| Frontend references | Verify current upstream patterns |
| Python runtime | Official docs still state 3.10+ minimum |

## Typed method style

```python
def action_confirm(self) -> bool:
    for record in self:
        if record.state == "draft":
            record.state = "confirmed"
    return True

@api.model_create_multi
def create(self, vals_list: list[dict[str, object]]):
    return super().create(vals_list)
```

## SQL style

```python
from odoo.tools import SQL

query = SQL(
    """
    SELECT m.id, m.name, COUNT(l.id) AS line_count
    FROM %s m
    LEFT JOIN %s l ON l.model_id = m.id
    WHERE m.state = %s AND m.company_id = %s
    GROUP BY m.id, m.name
    HAVING COUNT(l.id) > %s
    """,
    SQL.identifier(self._table),
    SQL.identifier("my_model_line"),
    "confirmed",
    self.env.company.id,
    0,
)
self.env.cr.execute(query)
```

Use this as the preferred pattern for new or refactored raw SQL. Do not claim that every classic parametrized `execute()` becomes invalid in 19.0.

## Model definition example

```python
from __future__ import annotations

from typing import TYPE_CHECKING

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import SQL

if TYPE_CHECKING:
    from odoo.addons.base.models.res_company import Company
    from odoo.addons.base.models.res_partner import Partner


class MyModel(models.Model):
    _name = "my.model"
    _description = "My Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id desc"
    _check_company_auto = True

    name = fields.Char(required=True, tracking=True, index="trigram")
    code = fields.Char(index=True, copy=False)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        tracking=True,
        index=True,
    )
    sequence = fields.Integer(default=10)
    quantity = fields.Float(digits="Product Unit of Measure")
    active = fields.Boolean(default=True)
    company_id: Company = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )
    user_id = fields.Many2one(
        "res.users",
        default=lambda self: self.env.user,
        tracking=True,
        check_company=True,
    )
    partner_id: Partner = fields.Many2one(
        "res.partner",
        tracking=True,
        check_company=True,
    )
    line_ids = fields.One2many("my.model.line", "model_id", copy=True)
    total_amount = fields.Monetary(
        compute="_compute_total",
        store=True,
        currency_field="currency_id",
    )
    currency_id = fields.Many2one(
        "res.currency",
        related="company_id.currency_id",
    )

    _code_company_uniq = models.Constraint(
        "UNIQUE(code, company_id)",
        "Code must be unique per company!",
    )
    _positive_quantity = models.Constraint(
        "CHECK(quantity >= 0)",
        "Quantity must be positive!",
    )

    @api.constrains("quantity")
    def _check_quantity(self) -> None:
        for record in self:
            if record.quantity < 0:
                raise ValidationError(_("Quantity must be positive."))

    def action_view_lines(self) -> dict:
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Lines"),
            "res_model": "my.model.line",
            "view_mode": "tree,form",
            "domain": [("model_id", "=", self.id)],
            "context": {"default_model_id": self.id},
        }
```

## Checklist

- [ ] Prefer type hints in new or touched methods
- [ ] Prefer `SQL()` in new or risky raw SQL helpers
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Keep `@api.model_create_multi`
- [ ] Keep multi-company safety fields and options in place
- [ ] Verify uncertain frontend references against upstream source
