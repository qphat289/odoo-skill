# Odoo Model Patterns - Core Concepts

This file covers cross-version ORM concepts only.
Use version-specific files for actual implementation details.

## Shared concepts

1. Choose the correct base class: `models.Model`, `models.TransientModel`, or `models.AbstractModel`.
2. Keep manifest ordering, security, and ORM behavior aligned.
3. Use computed fields, constraints, onchanges, and inheritance deliberately.
4. Treat version-specific APIs as external to this file.

## Cross-version reminders

| Version band | Main ORM note |
|-------------|---------------|
| 14-15 | legacy decorators and view patterns still appear |
| 16 | `Command` becomes the preferred x2many style |
| 17 | `@api.model_create_multi` and direct XML expressions matter |
| 18 | multi-company safeguards and `SQL()` become common |
| 19 | prefer `models.Constraint(...)`, add type hints where useful, and verify stronger claims upstream |

## Stable patterns

### Standard model

```python
class MyModel(models.Model):
    _name = "my.model"
    _description = "My Model"
```

### Transient model

```python
class MyWizard(models.TransientModel):
    _name = "my.wizard"
    _description = "My Wizard"
```

### Constraint example

```python
@api.constrains("amount")
def _check_amount(self):
    for record in self:
        if record.amount < 0:
            raise ValidationError(_("Amount must be positive."))
```

### Computed field example

```python
@api.depends("line_ids.amount")
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped("amount"))
```

## Guidance

- keep this file generic
- keep version claims in version-specific references
- verify uncertain 19.0 behavior against official docs or source
