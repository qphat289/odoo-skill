# Odoo 17 API Version Notes

Use this file together with `controller-api-patterns.md` and `external-api-patterns.md` when the target version is `17.0`.

## Critical deltas

- Route JSON type: use `type="json"`.
- Route auth values: `user`, `public`, `none`.
- Do not assume built-in `auth="bearer"` support in this version baseline.
- For token APIs, validate the header manually, then switch request env explicitly when needed.
- `Stream` is a good default for attachment/binary downloads in this version family.

## Safe baseline

```python
from odoo import http
from odoo.http import request
from werkzeug.exceptions import Unauthorized


class ApiController(http.Controller):
    @http.route("/api/v1/me", type="json", auth="none", csrf=False)
    def api_me(self, **params):
        token = request.httprequest.headers.get("Authorization", "")
        if not token.startswith("Bearer "):
            raise Unauthorized()
        user = request.env(su=True)["api.token"]._authenticate(token[7:])
        if not user:
            raise Unauthorized()
        request.update_env(user=user.id)
        return {"login": user.login}
```

## Review focus

- No `auth="bearer"` assumptions copied from newer versions.
- Frontend RPC routes stay on `type="json"`.
- Manual token bootstrap happens before privileged ORM work.
