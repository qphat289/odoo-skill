# Odoo Version Knowledge - 19.0

Release profile:
- Status: current release line
- Python: official docs still state 3.10+ minimum runtime
- Frontend: verify current `@odoo/owl` package and web patterns against the `19.0` source tree
- Verify against: `https://github.com/odoo/odoo/tree/19.0`

## Audited stance

The following points are strong enough to treat as verified for Odoo 19:
- Prefer `models.Constraint(...)` over `_sql_constraints`
- Keep `@api.model_create_multi` and modern multi-company patterns
- Verify non-trivial frontend behavior against current `addons/web` source

The following points should be treated as preference, not absolute rule:
- Type hints on new or touched methods
- `SQL()` builder for new or heavily refactored raw SQL
- Post-create `groups_id` assignment for `res.users` when provisioning flows are sensitive

## Verified change: `models.Constraint(...)` replaces `_sql_constraints`

```python
# Legacy pattern
class MyModel(models.Model):
    _name = "my.model"

    _sql_constraints = [
        ("check_percentage", "CHECK(percentage >= 0 AND percentage <= 100)",
         "The percentage must be between 0 and 100."),
    ]

# Odoo 19 preferred pattern
class MyModel(models.Model):
    _name = "my.model"

    _check_percentage = models.Constraint(
        "CHECK(percentage >= 0 AND percentage <= 100)",
        "The percentage of an analytic distribution should be between 0 and 100.",
    )
```

## Safer user provisioning pattern

Do not claim a blanket `groups_id` ban in `res.users.create()` unless the target build proves it.
For automation code, a safer pattern is still:

```python
user = self.env["res.users"].create({
    "login": "user@example.com",
    "name": "Example User",
})

group = self.env.ref("base.group_portal")
group.write({"users": [(4, user.id)]})
```

Use this when you want predictable post-create group assignment and clearer security review.

## Type hints: preferred, not globally mandatory

```python
# Still valid style in many official modules
def action_confirm(self):
    return True

# Preferred style for new or touched code
def action_confirm(self) -> bool:
    return True

def create_record(self, name: str, partner_id: int | None = None):
    return self.create({"name": name, "partner_id": partner_id})
```

## `SQL()` builder: strong preference, not blanket requirement

```python
from odoo.tools import SQL

# Preferred for new or refactored raw SQL
self.env.cr.execute(SQL(
    "SELECT id FROM my_model WHERE state = %s",
    "draft",
))

# Existing parametrized execute(...) patterns still exist in current core
self.env.cr.execute(
    "SELECT id FROM my_model WHERE state = %s",
    ["draft"],
)
```

## Frontend guidance for 19.0

Do not hardcode a specific OWL major-version label as a repository rule without re-checking upstream.
For Odoo 19 frontend work:
- use ES modules with `/** @odoo-module **/`
- follow current `@web` service and registry patterns from `addons/web`
- verify component hooks and props style against the target branch before large rewrites

Example pattern:

```javascript
/** @odoo-module **/

import { Component, onWillStart, onWillUnmount, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";

    static props = {
        recordId: { type: Number, optional: true },
        onSelect: { type: Function, optional: true },
    };

    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.state = useState({
            data: [],
            loading: true,
            error: null,
        });

        onWillStart(async () => {
            await this.loadData();
        });

        onWillUnmount(() => {
            this._abortController?.abort();
        });
    }

    async loadData() {
        this._abortController = new AbortController();
        try {
            this.state.data = await this.orm.searchRead(
                "my.model",
                [],
                ["name", "state"],
                { order: "create_date DESC" }
            );
        } catch (error) {
            if (error.name !== "AbortError") {
                this.state.error = String(error);
            }
        } finally {
            this.state.loading = false;
        }
    }
}
```

## Guidance

- Verify every non-trivial 19.0 claim against official docs or the current `19.0` source tree.
- Prefer "verified", "preferred", and "check upstream" labels instead of absolute claims unless the source is explicit.
- When migrating from 18.0, keep examples conservative unless the target deployment already runs a known 19.0 build.
