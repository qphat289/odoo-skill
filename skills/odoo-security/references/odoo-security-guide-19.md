# Odoo Security Guide - Version 19.0

Use this file for Odoo 19 security-sensitive code.
It favors audited guidance over speculative "everything is mandatory" language.

## Version 19.0 guidance

- Python: official docs still state 3.10+ minimum runtime
- Multi-company: keep `_check_company_auto` and `check_company=True` where relevant
- Record rules: keep documented `company_ids` usage in rule domains
- Python/context propagation: use `allowed_company_ids` when active company scope must travel through service logic
- SQL: prefer `SQL()` for new or risky raw SQL
- Typing: add type hints where they improve readability, review quality, or tooling

## Security groups

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="module_category_custom" model="ir.module.category">
        <field name="name">Custom Module</field>
        <field name="sequence">100</field>
    </record>

    <record id="group_custom_user" model="res.groups">
        <field name="name">User</field>
        <field name="category_id" ref="module_category_custom"/>
    </record>

    <record id="group_custom_manager" model="res.groups">
        <field name="name">Manager</field>
        <field name="category_id" ref="module_category_custom"/>
        <field name="implied_ids" eval="[(4, ref('group_custom_user'))]"/>
    </record>
</odoo>
```

## Record-rule pattern

```xml
<record id="rule_custom_model_company" model="ir.rule">
    <field name="name">Custom Model: Multi-Company</field>
    <field name="model_id" ref="model_custom_model"/>
    <field name="global" eval="True"/>
    <field name="domain_force">[
        '|',
        ('company_id', '=', False),
        ('company_id', 'in', company_ids)
    ]</field>
</record>
```

## Model security pattern

```python
from __future__ import annotations

from typing import Any

from odoo import _, api, fields, models
from odoo.exceptions import AccessError
from odoo.tools import SQL


class SecureModel(models.Model):
    _name = "custom.secure"
    _description = "Secure Model"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _check_company_auto = True

    name = fields.Char(required=True, tracking=True, index="btree")
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        required=True,
        index=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        check_company=True,
        index=True,
    )
    user_id = fields.Many2one(
        "res.users",
        default=lambda self: self.env.user,
        tracking=True,
        check_company=True,
    )
    amount = fields.Float(digits="Product Price")

    _name_company_unique = models.Constraint(
        "UNIQUE(name, company_id)",
        "Name must be unique per company.",
    )

    @api.model_create_multi
    def create(self, vals_list: list[dict[str, Any]]):
        return super().create(vals_list)

    def action_sensitive_operation(self) -> None:
        if not self.env.user.has_group("custom_module.group_manager"):
            raise AccessError(_("Only managers can perform this action."))
        self.check_access_rights("write")
        self.check_access_rule("write")
        self._execute_sensitive_operation()

    def _execute_sensitive_operation(self) -> None:
        pass

    def _get_secure_data(self) -> list[dict[str, Any]]:
        query = SQL(
            """
            SELECT id, name, amount
            FROM %s
            WHERE company_id = %s
              AND active = %s
              AND create_uid = %s
            ORDER BY create_date DESC
            """,
            SQL.identifier(self._table),
            self.env.company.id,
            True,
            self.env.user.id,
        )
        self.env.cr.execute(query)
        return self.env.cr.dictfetchall()
```

## Checklist

- [ ] All models have `ir.model.access.csv` entries
- [ ] Use `_check_company_auto = True` for multi-company models
- [ ] Use `check_company=True` on company-aware relations
- [ ] Keep rule domains on documented `company_ids`
- [ ] Forward `allowed_company_ids` only where Python/context propagation requires it
- [ ] Add type hints where the code is new, touched, or review-critical
- [ ] Prefer `SQL()` for new or risky raw SQL
- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)` when touching that code
- [ ] Keep direct XML expressions in views

## Agent instructions

1. Prefer conservative security patterns that are easy to review.
2. Use `models.Constraint(...)` for new SQL constraints.
3. Prefer `SQL()` in new security-sensitive raw SQL.
4. Verify runtime and frontend assumptions against official sources before making broad 19.0 claims.
