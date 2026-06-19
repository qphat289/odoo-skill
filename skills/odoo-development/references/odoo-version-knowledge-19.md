# Odoo Version Knowledge - 19.0

Development profile:
- Status: in development
- Python: 3.11 and 3.12
- Frontend: OWL 3.x
- Verify against: `https://github.com/odoo/odoo/tree/master`

## Overview

Odoo 19.0 trends toward:
- Mandatory type-hint discipline
- Required `SQL()` builder usage
- Newer OWL 3.x frontend patterns
- Stricter model and security conventions

## Breaking changes from v18

### SQL constraints use `models.Constraint()`

```python
# Deprecated pattern
class MyModel(models.Model):
    _name = 'my.model'

    _sql_constraints = [
        ('check_percentage', 'CHECK(percentage >= 0 AND percentage <= 100)',
         'The percentage must be between 0 and 100.'),
    ]

# v19 pattern
class MyModel(models.Model):
    _name = 'my.model'

    _check_percentage = models.Constraint(
        'CHECK(percentage >= 0 AND percentage <= 100)',
        'The percentage of an analytic distribution should be between 0 and 100.',
    )
```

### `res.users.create()` should not assign `groups_id`

```python
# Broken pattern
user = self.env['res.users'].create({
    'login': 'user@example.com',
    'groups_id': [(6, 0, [group.id])],
})

# Correct pattern
user = self.env['res.users'].create({'login': 'user@example.com'})
group.write({'users': [(4, user.id)]})
```

### Type hints are mandatory

```python
# Deprecated pattern
def action_confirm(self):
    pass

# v19 pattern
def action_confirm(self) -> bool:
    return True

def create_record(self, name: str, partner_id: int | None = None) -> 'MyModel':
    return self.create({'name': name, 'partner_id': partner_id})
```

### `SQL()` builder is required

```python
from odoo.tools import SQL

# Deprecated pattern
self.env.cr.execute("SELECT id FROM my_model WHERE state = %s", ['draft'])

# v19 pattern
self.env.cr.execute(SQL(
    "SELECT id FROM my_model WHERE state = %s",
    'draft'
))
```

## OWL 3.x example

```javascript
/** @odoo-module **/

import { Component, useState, onWillStart, onWillUnmount } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";

    static props = {
        recordId: { type: Number, optional: true },
        onSelect: { type: Function, optional: true },
    };

    static defaultProps = {
        recordId: null,
    };

    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.state = useState({
            data: [],
            loading: true,
            error: null,
        });

        this._abortController = null;

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
            const data = await this.orm.searchRead(
                "my.model",
                [],
                ["name", "state"],
                { order: "create_date DESC" }
            );
            this.state.data = data;
            this.state.error = null;
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

- Treat this file as provisional because v19 is still moving.
- Verify every non-trivial pattern against official Odoo master before applying it broadly.
- Prefer targeted adoption of v19-only patterns rather than blind global replacement.
