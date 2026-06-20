# Odoo Module Generator - Version 19.0

Use this file only for Odoo 19.0 module generation.
Treat it as an audited generator guide: keep verified patterns strong, and keep uncertain claims labeled as preference or "verify upstream".

## Version 19.0 guidance

- Python: official docs still state 3.10+ minimum runtime
- Type hints: preferred on new or touched methods
- SQL: prefer `SQL()` in new or heavily refactored raw SQL
- Constraints: prefer `models.Constraint(...)` over `_sql_constraints`
- Frontend: verify current `@web` and `@odoo/owl` patterns against the `19.0` source tree
- Views: use direct `invisible` / `readonly` / `required` expressions

## `__manifest__.py` template

```python
# -*- coding: utf-8 -*-
{
    "name": "{Module Title}",
    "version": "19.0.1.0.0",
    "category": "{Category}",
    "summary": "{Short description}",
    "description": """
{Detailed description}
    """,
    "author": "{Author}",
    "website": "{Website}",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "security/{module_name}_security.xml",
        "security/ir.model.access.csv",
        "views/{model_name}_views.xml",
        "views/menuitems.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "{module_name}/static/src/**/*.js",
            "{module_name}/static/src/**/*.xml",
            "{module_name}/static/src/**/*.scss",
        ],
    },
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
```

## Model template

```python
# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import Any

from odoo import Command, _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import SQL


class {ModelName}(models.Model):
    _name = "{module_name}.{model_name}"
    _description = "{Model Description}"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "create_date desc"
    _check_company_auto = True

    name = fields.Char(required=True, tracking=True)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        tracking=True,
        check_company=True,
    )
    user_id = fields.Many2one(
        "res.users",
        default=lambda self: self.env.user,
        tracking=True,
        check_company=True,
    )
    line_ids = fields.One2many(
        "{module_name}.{model_name}.line",
        "parent_id",
        copy=True,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        default="draft",
        required=True,
        tracking=True,
        copy=False,
    )
    amount = fields.Monetary(currency_field="currency_id")
    currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id,
        required=True,
    )

    @api.depends("line_ids.amount")
    def _compute_total_amount(self) -> None:
        for record in self:
            record.total_amount = sum(record.line_ids.mapped("amount"))

    total_amount = fields.Float(
        compute="_compute_total_amount",
        store=True,
    )

    @api.constrains("amount")
    def _check_amount(self) -> None:
        for record in self:
            if record.amount < 0:
                raise ValidationError(_("Amount must be positive."))

    _name_uniq = models.Constraint(
        "UNIQUE(company_id, name)",
        "Name must be unique per company!",
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]):
        for vals in vals_list:
            if not vals.get("name"):
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code(
                        "{module_name}.{model_name}"
                    )
                    or _("New")
                )
        return super().create(vals_list)

    def write(self, vals: dict[str, Any]) -> bool:
        if vals.get("state") == "done":
            for record in self:
                if not record.line_ids:
                    raise UserError(_("Cannot complete without lines."))
        return super().write(vals)

    def action_add_line(self) -> None:
        self.write({
            "line_ids": [
                Command.create({"name": "New Line", "amount": 0}),
            ],
        })

    def _get_report_data(self) -> list[dict[str, Any]]:
        query = SQL(
            """
            SELECT
                m.id,
                m.name,
                m.state,
                COALESCE(SUM(l.amount), 0) AS total
            FROM %s m
            LEFT JOIN %s l ON l.parent_id = m.id
            WHERE m.company_id IN %s
            GROUP BY m.id, m.name, m.state
            ORDER BY m.create_date DESC
            """,
            SQL.identifier(self._table),
            SQL.identifier("{module_name}_{model_name}_line"),
            tuple(self.env.companies.ids),
        )
        self.env.cr.execute(query)
        return self.env.cr.dictfetchall()
```

## Frontend note

For Odoo 19 frontend work:
- keep `/** @odoo-module **/`
- verify the current import, hook, and props patterns in `addons/web`
- avoid repo-wide claims about a forced OWL major-version rewrite unless upstream confirms it

## Checklist

- [ ] Add `from __future__ import annotations` when it helps keep typed code clean
- [ ] Add type hints where the code is new, touched, or high-value
- [ ] Prefer `SQL()` in new or high-risk raw SQL helpers
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Use `_check_company_auto = True` where multi-company logic applies
- [ ] Use `check_company=True` on relevant relational fields
- [ ] Use `@api.model_create_multi` for create
- [ ] Use `Command` for x2many work
- [ ] Use direct XML expressions in views
- [ ] Verify frontend assumptions against current `19.0` source
- [ ] Verify runtime assumptions against official docs and the deployment target

## Agent instructions

1. Prefer conservative 19.0 patterns over speculative "new mandatory" claims.
2. Use `models.Constraint(...)` for new SQL constraints.
3. Prefer `SQL()` for new or refactored low-level SQL.
4. Add type hints where they improve maintainability and review quality.
5. Re-check any uncertain frontend or runtime assumption against official sources.
