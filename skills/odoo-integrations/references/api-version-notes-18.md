# Odoo 18 API Version Notes

Use this file together with `controller-api-patterns.md` and `external-api-patterns.md` when the target version is `18.0`.

## Critical deltas

- Route JSON type remains `type="json"`.
- `auth="bearer"` is documented in controller routing.
- `readonly=` and `handle_params_access_error=` exist as advanced route options.
- Session-backed and bearer-backed access can coexist, so be explicit about the expected auth model.

## Safe baseline

```python
from odoo import http


class ApiController(http.Controller):
    @http.route("/api/v1/orders", type="json", auth="bearer", methods=["POST"], csrf=False)
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

- Use `auth="bearer"` only when token auth is really the contract.
- Keep `type="json"` for normal frontend and machine JSON routes in 18.
- For advanced route behavior, verify whether read-only cursor or parameter-access hooks are needed.
