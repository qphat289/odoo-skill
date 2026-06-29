# Odoo Common Bug Patterns

Use this file before build work and during review when the team wants a compact set of high-repeat mistakes to avoid.

This file is for bugs that are:

- frequent enough to justify a reusable prevention rule
- broad enough to matter across multiple modules
- actionable before or during code generation

Do not turn this file into a dump of one-off debugging notes or deployment procedures. Promote only repeatable patterns.

## Version bands

Use these version labels consistently in this file:

- `14-15`: applies mainly to Odoo 14 and 15
- `16`: applies mainly to Odoo 16
- `17+`: applies to Odoo 17 and later unless narrowed further
- `18+`: applies to Odoo 18 and later unless narrowed further
- `all`: applies across the supported repository range
- `OWL`: frontend pattern that should still be checked against the active version skill

## How to use

1. Read this file during implementation planning to turn repeated mistakes into explicit plan checks.
2. Read this file again before code generation so the agent avoids the bad pattern instead of only fixing it later.
3. If review or testing finds a new recurring bug:
   - log it in `docs/CORRECTIONS_LOG.md`
   - verify it against the smallest relevant canonical source
   - promote it here only when it is truly repeatable

## Pattern index

| ID | Area | Versions | Summary |
|---|---|---|---|
| CB-ORM-001 | ORM | all | Do not bypass or recurse instead of calling `super()` in CRUD overrides |
| CB-ORM-002 | ORM | all | Verify `_inherit` model names against real Odoo source |
| CB-ORM-003 | ORM | all | Avoid re-query loops and unnecessary browse calls |
| CB-ORM-004 | ORM | all | Do not use non-stored computed fields in domains or searches |
| CB-ORM-005 | ORM | all | Every computed field needs accurate `@api.depends(...)` inputs |
| CB-ORM-006 | ORM | 16+ | Prefer `Command` helpers for x2many write operations |
| CB-VIEW-001 | Views | all | Validate XPath targets against the real parent view |
| CB-VIEW-002 | Data | all | Protect seed or configuration records with `noupdate="1"` when overwrite is not desired |
| CB-VIEW-003 | Views | 17+ | Do not use legacy `attrs` syntax in XML visibility logic |
| CB-SEC-001 | Security | all | Every persistent model needs ACL coverage |
| CB-SEC-002 | Security | all | `ir.model.access.csv` must use the correct `model_...` XML ID |
| CB-SEC-003 | Security | all | Record rules must be reviewed for over-restriction and multi-rule intersection |
| CB-PERF-001 | Performance | all | Use recordsets, batching, and `mapped()` instead of N+1 ORM loops |
| CB-PERF-002 | Performance | all | Do not call `sudo()` inside loops |
| CB-PERF-003 | Performance | all | Use `search_count()` when only a count is needed |
| CB-UPG-001 | Upgrade | all | Migration scripts must skip fresh installs with `if not version: return` |
| CB-FE-001 | Frontend | OWL | Do not mutate reactive state in place |

## Promotion candidate template

Use this structure before promoting a new bug into the index:

```markdown
### CB-AREA-XXX: Short bug name

- Area:
- Versions:
- Why it matters:
- Trigger or symptom:
- Bad pattern:
- Preferred pattern:
- Check before build:
- Check during review:
```

## Patterns

### CB-ORM-001: CRUD override bypasses `super()`

- Area: ORM
- Versions: all

- Why it matters: breaks base Odoo logic, causes recursion, and hides side effects such as mail, tracking, or computed behavior.
- Bad pattern:

```python
def create(self, vals_list):
    return self.env["my.model"].create(vals_list)
```

- Preferred pattern:

```python
@api.model_create_multi
def create(self, vals_list):
    return super().create(vals_list)
```

- Check before build:
  - any `create`, `write`, `unlink`, or action override must justify its logic around a real `super()` call
  - for 17+, keep CRUD decorators aligned with the active version skill

### CB-ORM-002: `_inherit` points to the wrong model

- Area: ORM
- Versions: all

- Why it matters: the code may load late or fail only at runtime, which makes the defect expensive to debug.
- Bad pattern:

```python
_inherit = "sale.orders"
```

- Preferred pattern:
  - verify the exact model technical name in official source, debug mode, or the active version reference before writing the class

### CB-ORM-003: re-query loops and unnecessary `browse()`

- Area: ORM
- Versions: all

- Why it matters: creates N+1 behavior and noisy code for simple recordset operations.
- Bad pattern:

```python
orders = self.env["sale.order"].search([("state", "=", "sale")])
for order in orders:
    total += self.env["sale.order"].browse(order.id).amount_total
```

- Preferred pattern:

```python
orders = self.env["sale.order"].search([("state", "=", "sale")])
total = sum(orders.mapped("amount_total"))
```

- Check before build:
  - avoid converting a recordset to IDs only to browse it again
  - batch record access whenever the logic is read-only aggregation

### CB-ORM-004: non-stored computed field used in domain or search

- Area: ORM
- Versions: all

- Why it matters: searches fail or behave incorrectly when the field cannot be queried.
- Bad pattern:

```python
amount_custom = fields.Float(compute="_compute_custom")
self.search([("amount_custom", ">", 1000)])
```

- Preferred pattern:
  - add `store=True` when the field must support domains or search
  - otherwise keep it out of search logic and use another indexed source field

### CB-ORM-005: missing or incomplete `@api.depends(...)`

- Area: ORM
- Versions: all

- Why it matters: computed values go stale and the bug looks random to end users.
- Bad pattern:

```python
@api.depends()
def _compute_full_name(self):
    ...
```

- Preferred pattern:
  - declare every real input field in `@api.depends(...)`
  - review indirect dependencies when related fields or child lines drive the value

### CB-ORM-006: legacy x2many tuples used where `Command` is expected

- Area: ORM
- Versions: 16+

- Why it matters: older tuple syntax still appears in examples, but newer code becomes harder to review and easier to misuse.
- Preferred pattern for 16+:

```python
from odoo.fields import Command

self.tag_ids = [Command.set(tag_ids)]
self.tag_ids = [Command.link(tag_id)]
self.tag_ids = [Command.unlink(tag_id)]
```

- Check before build:
  - if the active target is 14 or 15, keep compatibility with the version skill
  - if the active target is 16+, prefer `Command`

### CB-VIEW-001: XPath target is guessed instead of verified

- Area: Views
- Versions: all

- Why it matters: inherited views fail silently at design time and loudly at load time.
- Preferred pattern:
  - inspect the real parent view XML first
  - use a precise XPath tied to stable structure
  - document why the selector is stable when the target is non-obvious

### CB-VIEW-002: missing `noupdate="1"` on records that should survive upgrade

- Area: Data
- Versions: all

- Why it matters: upgrades overwrite seed or configuration data unintentionally.
- Use this pattern when:
  - the data is initial configuration
  - the business expects later manual edits to survive upgrades

- Preferred pattern:

```xml
<odoo>
    <data noupdate="1">
        ...
    </data>
</odoo>
```

### CB-VIEW-003: legacy `attrs` syntax used on Odoo 17+

- Area: Views
- Versions: 17+

- Why it matters: view logic breaks because the XML syntax changed.
- Bad pattern:

```xml
<field name="date_end" attrs="{'invisible': [('type', '!=', 'fixed')]}"/>
```

- Preferred pattern on 17+:

```xml
<field name="date_end" invisible="type != 'fixed'"/>
```

- Check before build:
  - use technical selection keys, not translated labels

### CB-SEC-001: persistent model without ACL coverage

- Area: Security
- Versions: all

- Why it matters: users hit `Access Denied` after code is deployed.
- Preferred pattern:
  - every persistent business model must map to `security/ir.model.access.csv`
  - review related transient or helper models separately instead of blindly adding access rows everywhere

### CB-SEC-002: wrong `model_id` format in `ir.model.access.csv`

- Area: Security
- Versions: all

- Why it matters: the ACL row looks valid but points to the wrong XML ID.
- Bad pattern:

```csv
access_my_model,my model,my_model,base.group_user,1,1,1,0
```

- Preferred pattern:

```csv
access_my_model,my.model access,model_my_model,base.group_user,1,1,1,0
```

### CB-SEC-003: record rules block valid users

- Area: Security
- Versions: all

- Why it matters: rule intersections are easy to underestimate, especially with group overlap and multi-company domains.
- Check before build:
  - identify which groups the rule applies to
  - check whether several rules combine with AND-style filtering for the same user
  - review company scope explicitly when record visibility depends on company fields

### CB-PERF-001: ORM loops hide N+1 behavior

- Area: Performance
- Versions: all

- Why it matters: performance problems usually enter the module at generation time, not only during later optimization.
- Preferred pattern:
  - use recordsets, batched reads, and `mapped()`
  - avoid `browse(record.id)` inside a loop over records you already have
  - move aggregate or count logic to native ORM helpers when possible

### CB-PERF-002: `sudo()` called inside loops

- Area: Performance
- Versions: all

- Why it matters: repeatedly creating elevated environments is wasteful and obscures the real permission boundary.
- Bad pattern:

```python
for record in records:
    record.sudo().write({"field": "value"})
```

- Preferred pattern:

```python
records.sudo().write({"field": "value"})
```

### CB-PERF-003: full search loaded when only the count is needed

- Area: Performance
- Versions: all

- Why it matters: it loads unnecessary rows and is easy to miss during review.
- Bad pattern:

```python
records = self.search([("state", "=", "draft")])
count = len(records)
```

- Preferred pattern:

```python
count = self.search_count([("state", "=", "draft")])
```

### CB-UPG-001: migration script runs on fresh install

- Area: Upgrade
- Versions: all

- Why it matters: upgrade logic can corrupt fresh installations or make initial installs fail.
- Preferred pattern:

```python
def migrate(cr, version):
    if not version:
        return
```

### CB-FE-001: OWL state mutated in place

- Area: Frontend
- Versions: OWL

- Why it matters: UI updates become inconsistent and hard to reproduce.
- Bad pattern:

```javascript
this.state.items.push(newItem);
```

- Preferred pattern:

```javascript
this.state.items = [...this.state.items, newItem];
```

## Deliberately not included

These topics are useful, but they should stay in domain or operations references instead of this compact prevention file:

- generic backup reminders
- broad deployment runbooks
- one-off debug shell commands
- restart or cache-clear instructions that are not code-pattern bugs
- business-dependent `ondelete` choices without a stable default bug rule
