# Odoo OWL Components - Version 19.0

This file captures conservative frontend guidance for Odoo 19.0.
Do not assume a specific OWL major-version label unless it is re-verified against the current upstream source.

## Verified stance

- Use ES modules with `/** @odoo-module **/`
- Follow `@web` services, registries, and hooks from the current `19.0` source tree
- Re-check `addons/web/tooling/_package.json` and matching examples in `addons/web/static/src` when a component pattern is uncertain

## Current component baseline

```javascript
/** @odoo-module **/

import {
    Component,
    onWillStart,
    onWillUnmount,
    useRef,
    useState,
} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class MyComponent extends Component {
    static template = "my_module.MyComponent";

    static props = {
        recordId: { type: Number, optional: true },
        mode: { type: String, optional: true },
        onSelect: { type: Function, optional: true },
    };

    static defaultProps = {
        mode: "view",
    };

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.notification = useService("notification");

        this.state = useState({
            data: [],
            loading: true,
            error: null,
            selectedId: null,
        });

        this.containerRef = useRef("container");

        onWillStart(async () => {
            await this.loadData();
        });

        onWillUnmount(() => {
            this._abortController?.abort();
        });
    }

    async loadData() {
        this.state.loading = true;
        this.state.error = null;
        this._abortController = new AbortController();

        try {
            this.state.data = await this.orm.searchRead(
                "my.model",
                [],
                ["name", "state", "amount"],
                { order: "create_date DESC", limit: 100 }
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

## Review checklist for 19.0 frontend work

- [ ] Keep `@odoo-module`
- [ ] Keep imports aligned with the current `@web` structure
- [ ] Verify hooks and lifecycle usage against upstream examples
- [ ] Re-test custom props validation and async cleanup behavior
- [ ] Avoid labeling the change as a mandatory OWL major-version jump unless re-verified
