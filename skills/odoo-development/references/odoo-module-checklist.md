# Odoo Module Checklist

> **Used by:** planner and generation/review flows during task breakdown and execution.
>
> Reference this file when building or reviewing an Odoo module to ensure nothing important is missed.

---

## Module Scaffold

Minimum required files:

```text
{module_name}/
|-- __manifest__.py          # REQUIRED
|-- __init__.py              # REQUIRED
|-- models/
|   `-- __init__.py          # REQUIRED if models exist
|-- views/                   # REQUIRED if any UI exists
`-- security/
    `-- ir.model.access.csv  # REQUIRED for every new persistent model
```

### `__manifest__.py` template

```python
{
    'name': 'Module Display Name',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Short one-line description',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/{model}_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
```

Rules:
- Version format: `{odoo_version}.{X}.{Y}.{Z}`, for example `17.0.1.0.0`
- Put `security/ir.model.access.csv` first in `data`
- Do not import Python files from the manifest
- Use `__init__.py` imports only

---

## Task Categories

### Category A - Foundation

| Task | File | Notes |
|------|------|-------|
| Scaffold structure | `__manifest__.py`, `__init__.py` | Set version and depends |
| Security groups | `security/res_groups.xml` | Define before files that reference them |
| Access rights | `security/ir.model.access.csv` | One line per model per group |

### Category B - Models

| Task | File | Notes |
|------|------|-------|
| New model | `models/{name}.py` | Use `models.Model` |
| Inherited model | `models/{name}.py` | Use `_inherit = 'existing.model'` |
| Transient model | `wizards/{name}.py` | Use `models.TransientModel` |

Model checklist:
- [ ] `_name` defined for new models
- [ ] `_description` defined
- [ ] `_order` set if default sorting matters
- [ ] `_rec_name` set if not using `name`
- [ ] Relational fields define `ondelete` where appropriate
- [ ] Computed fields use `store=True` only when needed
- [ ] `@api.constrains` covers business rules
- [ ] `@api.onchange` is UI-only, not business logic
- [ ] `name_get()` overridden only when needed for older versions

### Category C - Views

| Task | File | Notes |
|------|------|-------|
| Form view | `views/{model}_views.xml` | Full record editing |
| List view | `views/{model}_views.xml` | `<list>` in v17+, `<tree>` in v16- |
| Kanban view | `views/{model}_views.xml` | Stage-based workflows |
| Search view | `views/{model}_views.xml` | Filters and group-by |
| Action | `views/menu_items.xml` | `ir.actions.act_window` |
| Menu items | `views/menu_items.xml` | Parent -> child -> action |

View checklist:
- [ ] XML IDs follow a consistent module-based naming pattern
- [ ] Form view has `<header>` when workflow states exist
- [ ] List view shows only key columns
- [ ] Search view has useful filters and group-by entries
- [ ] Visibility syntax matches the target version:
  - v14-v16: `attrs="{'invisible': [('state', '=', 'done')]}"` or equivalent
  - v17+: `invisible="state == 'done'"`

### Category D - Security

| Task | File | Notes |
|------|------|-------|
| Access rights | `security/ir.model.access.csv` | Required per model |
| Record rules | `security/ir.rule.xml` | Row-level filtering |
| Custom groups | `security/res_groups.xml` | Only if the app needs roles |

`ir.model.access.csv` format:

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_{model}_{group},{model} {group},model_{model_underscore},{group_xml_id},1,1,1,1
```

Rules:
- Every new persistent model needs at least one access line
- `base.group_user` is the default internal-user baseline when appropriate
- Use custom or higher-privilege groups deliberately

### Category E - Menus and Actions

Checklist:
- [ ] Actions point to the correct model and views
- [ ] Menus are loaded after the actions they reference
- [ ] Group restrictions are applied deliberately

### Category F - Tests

Checklist:
- [ ] Non-trivial business logic has at least one behavioral test
- [ ] Security-sensitive features have permission tests
- [ ] Version-sensitive syntax or upgrade-sensitive logic has targeted tests

---

## Build Order

Use this order unless a specific dependency forces a variation:

1. Scaffold
2. Security groups
3. Models
4. Access rights
5. Data
6. Views
7. Actions
8. Menus
9. Reports
10. Controllers
11. OWL assets
12. Tests

If you need the exact canonical ordering rules for manifest and XML references, also read `odoo-manifest-data-order.md`.

---

## Final Checks

- [ ] Manifest version is correct
- [ ] Dependencies are complete
- [ ] Access rights exist for each model
- [ ] Manifest `data` order is dependency-safe
- [ ] View syntax matches target version
- [ ] Multi-company behavior is safe
- [ ] Tests exist for important business or security flows
