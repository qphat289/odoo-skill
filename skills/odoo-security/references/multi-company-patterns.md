# Multi-Company Security Patterns

Use this file when a model is company-aware, when record rules depend on company visibility, or when a review must check cross-company leakage.

## Version guardrails

| Version band | Main pattern |
|---|---|
| `14-15` | Manual company validation in Python and explicit view/domain filtering |
| `16-17` | Same overall model; use `with_company()` consistently and keep record-rule domains explicit |
| `18+` | Prefer `_check_company_auto = True` and `check_company=True` on company-scoped relations |

Important distinction:
- In official security rule documentation, `company_ids` is the standard record-rule variable.
- In business logic/context handling for newer code, `allowed_company_ids` is often the right context key to respect active company scope.

## Baseline company-aware model

### `14-17`

```python
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MyModel(models.Model):
    _name = "my.model"

    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        domain="[('company_id', 'in', [company_id, False])]",
    )

    @api.constrains("company_id", "partner_id")
    def _check_partner_company(self):
        for record in self:
            if record.partner_id.company_id and record.partner_id.company_id != record.company_id:
                raise ValidationError("Partner company must match record company.")
```

### `18+`

```python
from odoo import fields, models


class MyModel(models.Model):
    _name = "my.model"
    _check_company_auto = True

    company_id = fields.Many2one(
        "res.company",
        required=True,
        default=lambda self: self.env.company,
        index=True,
    )
    partner_id = fields.Many2one("res.partner", check_company=True)
    warehouse_id = fields.Many2one("stock.warehouse", check_company=True)
```

## Record-rule baseline

### Shared/company-safe rule

```xml
<record id="my_model_company_rule" model="ir.rule">
    <field name="name">My Model: multi-company</field>
    <field name="model_id" ref="model_my_model"/>
    <field name="domain_force">[
        '|',
        ('company_id', '=', False),
        ('company_id', 'in', company_ids)
    ]</field>
</record>
```

Rules:
- Use a global rule for company partitioning.
- Prefer `company_ids` inside record-rule domains.
- Avoid mixing several unrelated global rules that can accidentally intersect to zero access.

## Business logic and context

### Respect active company scope

```python
allowed_company_ids = self.env.context.get("allowed_company_ids", self.env.companies.ids)

records = self.with_context(allowed_company_ids=allowed_company_ids).search([
    ("company_id", "in", allowed_company_ids),
])
```

### Switch company explicitly

```python
for company in self.env.companies:
    pending = self.with_company(company).search([
        ("company_id", "=", company.id),
        ("state", "=", "pending"),
    ])
    pending._process_company_batch()
```

Rules:
- Prefer `with_company()` over ad-hoc context mutation when the goal is to run logic in another company.
- Use explicit company filters in cron/batch jobs, even when the env company is switched.

## Shared records

Use company-less records intentionally:

```xml
<field name="domain_force">[
    '|',
    ('company_id', '=', False),
    ('company_id', 'in', company_ids)
]</field>
```

If the model is not meant to be shared, remove the `False` branch and keep the model strictly company-scoped.

## Review checklist

- Model has `company_id` when it should be company-aware.
- Company rule exists and is global.
- Company-scoped relations use `check_company=True` on `18+`.
- Legacy versions have an explicit Python/company validation path.
- Search views, many2one domains, and cron jobs do not leak across companies.
- `sudo()` calls do not accidentally bypass intended company boundaries.

## Common mistakes

- Using `user.company_ids` in a rule when the active company scope matters more than all switchable companies.
- Forgetting `_check_company_auto` on 18+ company-aware models.
- Assuming UI domain filters are enough without server-side validation.
- Running a cross-company cron with one env company and no explicit company loop.
