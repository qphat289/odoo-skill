# Odoo Version Knowledge: 18 to 19 Migration

This file is an audited migration note for claims that are easy to overstate.
Use it to separate verified upstream changes from "prefer and verify" guidance.

## Audited summary

| Category | 18.0 | 19.0 | Confidence |
|----------|------|------|------------|
| SQL constraints | `_sql_constraints` still common | `models.Constraint(...)` is the preferred 19.0 pattern | Verified |
| Raw SQL | `SQL()` recommended | `SQL()` preferred for new or refactored SQL, but classic `cr.execute(...)` still exists in core | Verified |
| Type hints | Recommended | Stronger adoption in modern code, but not globally mandatory in core | Verified |
| `res.users` groups | Common to set in create flows | Use post-create assignment when you want safer provisioning, but do not claim a universal ban without target-build proof | Verified |
| Frontend | Follow v18 source | Re-check current `addons/web` patterns before calling anything an OWL major-version rewrite | Verified |
| Python runtime | 3.11+ common target | Official docs still state 3.10+ minimum runtime | Verified |

## Verified migration point: move SQL constraints to `models.Constraint(...)`

```python
# Before
_sql_constraints = [
    ("code_unique", "UNIQUE(code)", "Code must be unique."),
    ("amount_positive", "CHECK(amount >= 0)", "Amount must be positive."),
]

# After
_code_unique = models.Constraint(
    "UNIQUE(code)",
    "Code must be unique.",
)
_amount_positive = models.Constraint(
    "CHECK(amount >= 0)",
    "Amount must be positive.",
)
```

## Raw SQL migration stance

Treat this as the clean rule for new code:

```python
from odoo.tools import SQL

self.env.cr.execute(SQL(
    """
    SELECT state, COUNT(*)
    FROM my_model
    WHERE company_id = %s
    GROUP BY state
    """,
    self.env.company.id,
))
```

But do not state that every classic parametrized `execute()` call is invalid in 19.0. Current core still contains that style.

## Type hints migration stance

Good upgrade target:
- annotate new public methods
- annotate touched CRUD overrides
- add field annotations only where the codebase already benefits from them

Avoid saying:
- "all methods must be annotated"
- "untyped methods break in 19.0"

Example:

```python
@api.model_create_multi
def create(self, vals_list: list[dict[str, object]]):
    return super().create(vals_list)

def action_done(self) -> bool:
    self.write({"state": "done"})
    return True
```

## `res.users` provisioning guidance

Safer automation pattern:

```python
user = self.env["res.users"].create({
    "name": "Portal User",
    "login": "portal@example.com",
})

portal_group = self.env.ref("base.group_portal")
portal_group.write({"users": [(4, user.id)]})
```

Use this pattern in upgrade notes because it is conservative and review-friendly.
Do not describe it as a universal 19.0 requirement unless the target deployment proves it.

## Frontend migration guidance

Do not frame 18.0 to 19.0 as an automatic "OWL 2.x to 3.x rewrite".
Instead:
- re-check `addons/web/tooling/_package.json`
- inspect matching component patterns in `addons/web/static/src`
- update custom code only where the current source shows a real API difference

Safe migration checklist:
- keep `/** @odoo-module **/`
- keep `@web` services and registry usage aligned with source
- re-test custom hooks, lifecycle logic, and props validation

## Runtime guidance

For 19.0 environment planning:
- treat Python 3.10+ as the documented minimum
- verify the actual deployment or packaging constraints before tightening to 3.11/3.12

## Migration checklist

- [ ] Replace legacy `_sql_constraints` with `models.Constraint(...)`
- [ ] Prefer `SQL()` in new or high-risk raw SQL code
- [ ] Add type hints to new or touched methods, especially CRUD overrides
- [ ] Review user provisioning flows and use post-create group assignment where safer
- [ ] Verify frontend assumptions against the current `19.0` source tree
- [ ] Verify runtime assumptions against official docs and the deployment target
