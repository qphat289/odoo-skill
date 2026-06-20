# Odoo Decorator Decision Patterns

Use this file when the main question is which `@api` decorator belongs on a method, or when reviewing model code for decorator mistakes.

## Version guardrails

- Odoo 14: single-record `@api.model def create(self, vals)` is still common and valid.
- Odoo 15-16: `@api.model_create_multi` should be preferred for new code and upgrade-safe code.
- Odoo 17+: `@api.model_create_multi` is the normal required create pattern in this repo.
- For version-final syntax, always pair this file with the active version skill and `odoo-model-patterns-{version}.md`.

## Fast decision table

| Situation | Use | Notes |
|---|---|---|
| Override `create()` | `@api.model_create_multi` | Required baseline for modern Odoo create overrides |
| Method does not depend on current records | `@api.model` | Use for factories, defaults, lookup helpers |
| Stored/non-stored compute depends on fields | `@api.depends(...)` | List every field that drives the result |
| Non-stored compute depends on context | `@api.depends_context(...)` | Use for `company`, `uid`, `lang`, pricelist, feature flags |
| Validate business data on create/write | `@api.constrains(...)` | Simple field names only |
| React to form edits before save | `@api.onchange(...)` | UI-only, pseudo-record, no CRUD |
| Block deletion in normal usage | `@api.ondelete(at_uninstall=False)` | Prefer over validation inside `unlink()` |
| Daily cleanup task | `@api.autovacuum` | Lightweight cleanup called by autovacuum cron |
| Existing public method must not be RPC-callable | `@api.private` | Use when renaming to `_method` is not practical |

## Copy-paste patterns

### `create()` override

```python
from odoo import api, models


class MyModel(models.Model):
    _name = "my.model"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals.setdefault("state", "draft")
        records = super().create(vals_list)
        records._post_create_sync()
        return records
```

Rules:
- Treat `vals_list` as a list even when callers pass a single dict.
- Do not use `@api.model` on `create()`.
- Batch-safe logic comes before per-record side effects.

Version note:
- If the target is Odoo 14 and you are reviewing legacy code, a single-record `create(self, vals)` override may still be intentional.
- For Odoo 15+, prefer converging to `@api.model_create_multi`.

### Model-level helper

```python
from odoo import api, models


class MyModel(models.Model):
    _name = "my.model"

    @api.model
    def _default_team_id(self):
        return self.env.user.sale_team_id.id
```

### Field compute with context

```python
from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    display_price = fields.Float(compute="_compute_display_price")

    @api.depends("list_price")
    @api.depends_context("pricelist", "company")
    def _compute_display_price(self):
        pricelist_id = self.env.context.get("pricelist")
        pricelist = self.env["product.pricelist"].browse(pricelist_id) if pricelist_id else False
        for product in self:
            product.display_price = (
                pricelist._get_product_price(product, 1.0) if pricelist else product.list_price
            )
```

Rules:
- Use `@api.depends_context` for non-stored context-sensitive values.
- Every record in `self` must be assigned.
- Missing dependencies cause stale values and hard-to-trace bugs.

### Constraint that must always hold

```python
from odoo import api, models
from odoo.exceptions import ValidationError


class MyModel(models.Model):
    _name = "my.model"

    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        for record in self:
            if record.date_end and record.date_start and record.date_end < record.date_start:
                raise ValidationError("End date must be after start date.")

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._check_dates()
        return records
```

Rules:
- `@api.constrains` only reacts when listed fields are present in `create()` or `write()`.
- Use simple field names only, not dotted paths.
- If the invariant must always run, call the checker from `create()` or `write()`.

### Onchange

```python
from odoo import api, models


class MyModel(models.Model):
    _name = "my.model"

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id:
            self.email = self.partner_id.email
            self.phone = self.partner_id.phone
```

Rules:
- `onchange` is form behavior, not a backend guarantee.
- Do not call `create()`, `write()`, or `unlink()` from an onchange.
- Do not rely on dotted names inside `@api.onchange`.

### Delete rule

```python
from odoo import api, models
from odoo.exceptions import UserError


class MyModel(models.Model):
    _name = "my.model"

    @api.ondelete(at_uninstall=False)
    def _unlink_except_draft(self):
        if any(record.state not in ("draft", "cancel") for record in self):
            raise UserError("Only draft or cancelled records can be deleted.")
```

Rules:
- Prefer `@api.ondelete` to delete validation in `unlink()`.
- `at_uninstall=False` is the safe default for business models.

Version note:
- If an older codebase still validates deletion inside `unlink()`, do not rewrite blindly without checking the active version references and uninstall behavior.

### Autovacuum

```python
from datetime import timedelta

from odoo import api, fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.autovacuum
    def _gc_orphan_attachments(self):
        threshold = fields.Datetime.now() - timedelta(days=30)
        self.search([
            ("res_model", "=", False),
            ("create_date", "<", threshold),
        ]).unlink()
```

## Review checklist

- `create()` override uses `@api.model_create_multi`.
- `@api.depends` lists every field actually read.
- `@api.constrains` does not use dotted paths.
- `@api.onchange` is not used as a substitute for backend validation.
- Delete validation uses `@api.ondelete` when appropriate.
- Context-sensitive compute uses `@api.depends_context`.

## Common mistakes

- `@api.model` on `create()` in Odoo 17+ code.
- Compute method that forgets one record in `self`.
- Constraint that assumes it always runs.
- Onchange that performs ORM writes or external calls.
- Deletion rules hidden in `unlink()` and then breaking uninstall flows.
