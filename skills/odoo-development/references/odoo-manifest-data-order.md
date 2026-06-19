# Odoo Manifest and Data Ordering

Use this file as the central source of truth for manifest `data` ordering and XML record ordering.

## Manifest `data` order

Use dependency order, not arbitrary grouping:

1. Security groups and categories
2. Access rights (`security/ir.model.access.csv`)
3. Base data records
4. Views
5. Actions
6. Menus
7. Reports
8. Wizards
9. Demo data

Example:

```python
'data': [
    'security/res_groups.xml',
    'security/ir.model.access.csv',
    'data/sequence.xml',
    'views/my_model_views.xml',
    'views/my_model_actions.xml',
    'views/menuitems.xml',
    'report/my_model_report.xml',
]
```

## XML ordering rules

- Define records before other records reference them.
- Define groups before access rules or menu restrictions use them.
- Define actions before menus that point to them.
- Define base views before inherited views that extend them inside the same module.

## Common failure patterns

- Menus loaded before actions
- Views loaded before required security groups
- Access CSV referencing groups that are defined later
- Inherited XML records loaded before the records they extend

## Use rules

- Use this file as the canonical ordering baseline across generation, review, and upgrade flows.
- Pull version-specific syntax from the matching version skill and `odoo-version-knowledge-{version}.md`.
