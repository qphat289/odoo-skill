# Odoo 19 API Version Notes

Use this file together with `controller-api-patterns.md` and `external-api-patterns.md` when the target version is `19.0`.

## Critical deltas

- Route docs use `type="jsonrpc"` instead of the older `type="json"` wording.
- `auth="bearer"` remains documented.
- Route options include newer knobs such as `captcha=` and `save_session=`.
- Treat copied 17/18 snippets with caution and normalize them to current 19 routing semantics.

## Safe baseline

```python
from odoo import http


class ApiController(http.Controller):
    @http.route("/api/v1/orders", type="jsonrpc", auth="bearer", methods=["POST"], csrf=False)
    def list_orders(self, domain=None, limit=80):
        return {
            "orders": http.request.env["sale.order"].search_read(
                domain or [],
                ["name", "state", "amount_total"],
                limit=limit,
            )
        }
```

## Review focus

- Update old `type="json"` snippets before applying them blindly to 19.
- Keep bearer/session expectations explicit.
- Recheck non-trivial controller options against the active 19 docs/source.
