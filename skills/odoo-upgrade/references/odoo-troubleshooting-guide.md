# Odoo Troubleshooting Guide

Common errors, likely causes, and fixes for Odoo module development.

## Quick error lookup

| Error Pattern | Likely Cause | Version | Solution |
|---------------|--------------|---------|----------|
| `'api' has no attribute 'multi'` | Using `@api.multi` | v15+ | Remove decorator |
| `attrs attribute is no longer supported` | Using `attrs=` | v17+ | Use direct XML expressions |
| `create() takes 2 positional arguments` | Single-record `create()` pattern | v17+ | Use `@api.model_create_multi` |
| `check_company failed` | Cross-company relation mismatch | v18+ | Add `_check_company_auto` and `check_company=True` |
| `string SQL warning during upgrade` | Legacy string SQL in code under upgrade | v19 audit | Prefer `SQL()` builder and verify against current source |
| `External ID not found` | Missing XML reference or wrong order | All | Check file order in manifest and XML |
| `Access Denied` | Missing access rules | All | Add `ir.model.access.csv` |
| `KeyError: 'field_name'` | Field not present in `vals` | All | Use `.get()` or guard access |
| `RecursionError` | Circular compute or onchange chain | All | Check dependencies and write flow |
| `MissingError` | Deleted record access | All | Use `record.exists()` |

## Version-specific errors

### v15+ - `odoo.api` has no attribute `multi`

Cause: `@api.multi` was removed.

Wrong:

```python
@api.multi
def action_confirm(self):
    for record in self:
        record.state = 'confirmed'
```

Correct:

```python
def action_confirm(self):
    for record in self:
        record.state = 'confirmed'
```

### v16+ / v17+ - `attrs` problems in XML

Cause: `attrs=` is deprecated in v16 and removed in v17.

Wrong:

```xml
<field name="partner_id" attrs="{'invisible': [('state', '=', 'draft')]}"/>
```

Correct:

```xml
<field name="partner_id" invisible="state == 'draft'"/>
```

Additional direct expressions:

```xml
<field name="amount" readonly="state != 'draft'"/>
<field name="partner_id" required="state == 'confirmed'"/>
<field name="internal_notes" column_invisible="True"/>
```

### v17+ - `create()` signature mismatch

Cause: single-record `create()` pattern where multi-create is expected.

Wrong:

```python
@api.model
def create(self, vals):
    return super().create(vals)
```

Correct:

```python
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

### v18+ - `check_company failed`

Cause: company-aware relations are missing the required company safety configuration.

Wrong:

```python
class MyModel(models.Model):
    _name = 'my.model'

    company_id = fields.Many2one('res.company')
    partner_id = fields.Many2one('res.partner')
```

Correct:

```python
class MyModel(models.Model):
    _name = 'my.model'
    _check_company_auto = True

    company_id = fields.Many2one('res.company', required=True)
    partner_id = fields.Many2one('res.partner', check_company=True)
```

### v19 - SQL migration warning

Cause: older string SQL pattern in code being upgraded.

Wrong:

```python
self.env.cr.execute(
    "SELECT id FROM my_model WHERE state = %s",
    ('draft',),
)
```

Preferred fix:

```python
from odoo.tools import SQL

self.env.cr.execute(SQL(
    "SELECT id FROM my_model WHERE state = %s",
    'draft',
))
```

## Troubleshooting process

1. Confirm the target Odoo version.
2. Check whether the failing pattern is version-sensitive.
3. Verify manifest and XML ordering.
4. Compare against the matching version knowledge file.
5. Verify uncertain cases against official Odoo source.

## Related sources

- `odoo-version-routing.md`
- `odoo-manifest-data-order.md`
- `odoo-version-knowledge-{version}.md`
- `rules/security.md`
- `rules/coding-style.md`
