# Odoo Frontend Migration Guide: 18.0 -> 19.0

Treat this file as an audited review checklist, not as proof of a specific OWL major-version jump.

## Migration stance

For custom frontend code moving from 18.0 to 19.0:
- keep `/** @odoo-module **/`
- re-check current `@web` service and registry imports
- verify hook, lifecycle, and props patterns against the current 19.0 source tree
- do not assume a full component rewrite unless upstream examples show a real API gap

## Safe comparison

| Area | 18.0 habit | 19.0 migration stance |
|------|------------|-----------------------|
| Module format | ES modules | Keep ES modules |
| Services | `useService(...)` | Keep and verify exact import paths |
| Registry | `registry.category(...).add(...)` | Keep and verify category/API usage |
| State and hooks | Existing Owl hooks | Re-check current upstream examples |
| Props docs | Light JSDoc or none | Prefer clearer JSDoc when the component is non-trivial |

## Example migration

Before:

```javascript
/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            data: [],
            loading: true,
        });

        onWillStart(async () => {
            this.state.data = await this.orm.searchRead(
                "my.model",
                [],
                ["name", "state"]
            );
            this.state.loading = false;
        });
    }
}
```

After:

```javascript
/** @odoo-module **/

import { Component, onWillStart, onWillUnmount, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";

    static props = {
        recordId: { type: Number, optional: true },
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
                this.notification.add(this.state.error, { type: "danger" });
            }
        } finally {
            this.state.loading = false;
        }
    }
}

registry.category("actions").add("my_module.my_action", MyComponent);
```

## Migration checklist

- [ ] Re-check the current frontend package and imports in `addons/web`
- [ ] Verify props style against upstream examples
- [ ] Verify async cleanup for RPC-heavy components
- [ ] Re-test action registration and service access
- [ ] Avoid repo-wide claims about a mandatory OWL major-version rewrite without upstream proof
