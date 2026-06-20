# Controller and API Patterns

Use this file for HTTP controllers, JSON routes, website endpoints, file transfers, and webhook/API design.

## Version guardrails

| Version band | Guardrail |
|---|---|
| `14-15` | Keep to `type="http"` / `type="json"` and classic auth modes. |
| `16` | Transitional baseline; keep older route semantics unless the project already normalized forward. |
| `17` | Do not assume `auth="bearer"` exists. |
| `18` | `auth="bearer"` is documented; still choose it deliberately rather than by default. |
| `19` | Route docs move JSON handlers to `type="jsonrpc"`; review copied snippets before reuse. |

If a controller pattern conflicts with the active version skill, the version skill wins.

## Route baseline

```python
from odoo import http
from odoo.http import request


class MyController(http.Controller):
    @http.route("/my_module/ping", type="http", auth="public", methods=["GET"])
    def ping(self):
        return "OK"
```

## Route options that matter

```python
@http.route(
    "/my/path",
    type="http",          # "http" or "json"
    auth="user",          # "user", "public", "none"
    methods=["GET"],
    csrf=True,
    cors=None,
    website=False,
)
```

### Auth model

| Auth | Meaning | Use case |
|---|---|---|
| `user` | Logged-in user required | backend pages, authenticated JSON routes |
| `public` | Public user if anonymous, real user if logged in | website pages, public forms |
| `none` | No normal DB/user auth flow | health checks, low-level webhooks, manual token bootstrap |

Version notes:
- In Odoo 17, do not assume `auth="bearer"` exists.
- `auth="none"` is special-purpose. Use it only when normal user/public auth is not appropriate.

## Controller inheritance

When overriding an existing controller method, re-decorate it.

```python
from odoo import http
from odoo.addons.web.controllers.home import Home


class MyHome(Home):
    @http.route()
    def index(self, *args, **kwargs):
        return super().index(*args, **kwargs)
```

## Pick the right route type

### `type="http"`

Use for:
- HTML pages
- form posts
- redirects
- file download/upload

```python
@http.route("/my_module/page", type="http", auth="user")
def page(self):
    records = request.env["my.model"].search([])
    return request.render("my_module.page_template", {"records": records})
```

### `type="json"`

Use for:
- frontend RPC
- machine-to-machine JSON calls
- OWL service calls

```python
@http.route("/my_module/data", type="json", auth="user")
def get_data(self, domain=None, limit=80):
    return {
        "records": request.env["my.model"].search_read(
            domain or [],
            ["name", "state"],
            limit=limit,
        ),
    }
```

Rules:
- Keep JSON handlers returning Python dict/list payloads.
- Prefer `type="json"` over manual `json.dumps(...)` when the consumer is Odoo/OWL RPC.

## OWL / frontend JSON route

```python
@http.route("/my_module/action", type="json", auth="user")
def run_action(self, record_id):
    record = request.env["my.model"].browse(record_id).exists()
    if not record:
        return {"error": "not_found"}
    record.action_confirm()
    return {"success": True, "state": record.state}
```

```javascript
/** @odoo-module **/
import { useService } from "@web/core/utils/hooks";

setup() {
    this.rpc = useService("rpc");
}

async confirm(recordId) {
    const result = await this.rpc("/my_module/action", { record_id: recordId });
    return result;
}
```

## Public form with CSRF

```xml
<form action="/my_module/submit" method="POST">
    <input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>
    <input type="text" name="email"/>
    <button type="submit">Send</button>
</form>
```

```python
@http.route("/my_module/submit", type="http", auth="public", methods=["POST"])
def submit(self, email=None, **kwargs):
    request.env["newsletter.signup"].sudo().create({"email": email})
    return request.redirect("/thanks")
```

Rule:
- Disable CSRF only for endpoints protected another way.

## Webhook pattern

```python
import hashlib
import hmac

from odoo import http
from odoo.http import request


class WebhookController(http.Controller):
    @http.route("/webhook/my_module", type="http", auth="none", methods=["POST"], csrf=False)
    def webhook(self, **kwargs):
        secret = request.env(su=True)["ir.config_parameter"].get_param("my_module.webhook_secret")
        signature = request.httprequest.headers.get("X-Signature", "")
        payload = request.httprequest.get_data()
        expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            return request.make_response("bad signature", status=400)

        request.env(su=True)["my.model"].process_webhook_payload(payload)
        return request.make_response("OK", status=200)
```

Rules:
- Verify signatures on the raw request body.
- Keep webhook route thin; move processing into a model method.
- Use elevated env deliberately and narrowly.

## File upload

```python
import base64

from odoo import http
from odoo.http import request


class UploadController(http.Controller):
    @http.route("/my_module/upload", type="http", auth="user", methods=["POST"])
    def upload(self, **post):
        upload = request.httprequest.files.get("file")
        if not upload:
            return request.make_response("No file", status=400)

        attachment = request.env["ir.attachment"].create({
            "name": upload.filename,
            "datas": base64.b64encode(upload.read()),
            "mimetype": upload.mimetype,
            "res_model": "my.model",
            "res_id": int(post.get("res_id", 0)) or False,
        })
        return request.redirect(f"/web#id={attachment.res_id}&model=my.model")
```

## File download

Prefer `Stream` for binary delivery when possible.

```python
from odoo import http
from odoo.http import Stream, request


class DownloadController(http.Controller):
    @http.route("/my_module/download/<int:attachment_id>", type="http", auth="user")
    def download(self, attachment_id):
        attachment = request.env["ir.attachment"].browse(attachment_id).exists()
        if not attachment:
            return request.not_found()
        attachment.check("read")
        return Stream.from_attachment(attachment).get_response(as_attachment=True)
```

Version note:
- If the active version skill uses a different `not_found` handling style, follow that version-specific rule.
- If `Stream` is not the preferred pattern on the target codebase, fall back to an explicit `request.make_response(...)` binary response.

## Token/API-key pattern

```python
from werkzeug.exceptions import Forbidden


class ApiController(http.Controller):
    def _check_api_key(self):
        key = request.httprequest.headers.get("X-Api-Key")
        expected = request.env["ir.config_parameter"].sudo().get_param("my_module.api_key")
        if not key or key != expected:
            raise Forbidden()

    @http.route("/api/v1/orders", type="json", auth="user", csrf=False, cors="*")
    def list_orders(self, domain=None, limit=80):
        self._check_api_key()
        return {
            "orders": request.env["sale.order"].sudo().search_read(
                domain or [],
                ["name", "state", "amount_total"],
                limit=limit,
            )
        }
```

Rules:
- For cross-origin JSON APIs, set `cors` explicitly.
- Avoid blanket `sudo()` on public endpoints unless the domain and returned fields are tightly controlled.

## Review checklist

- Route type matches the real consumer.
- Overridden controllers are re-decorated.
- `csrf=False` is justified.
- Public routes do not leak fields through `sudo().search_read(...)`.
- File downloads check existence and access.
- Webhooks validate signature before ORM work.

## Common mistakes

- Using `type="http"` and hand-rolling JSON for normal OWL RPC.
- Treating `auth="none"` like a regular authenticated controller.
- Returning tuple-style `(payload, 401)` from JSON handlers.
- Putting business logic directly in the controller instead of models/services.
- Downloading binary fields without explicit access checks.
