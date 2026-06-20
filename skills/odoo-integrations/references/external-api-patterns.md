# External API Integration Patterns

Use this file for outbound HTTP clients, inbound webhooks, third-party sync jobs, token/API-key flows, retry strategy, and idempotent integration design.

## Version guardrails

| Version band | Integration notes |
|---|---|
| `14-15` | No built-in bearer route auth baseline. Use `auth="user"`, `auth="public"`, or `auth="none"` plus manual token/signature validation. |
| `16` | Same broad integration model as 14-15, but modernize code toward batch-safe ORM and cleaner RPC helpers. |
| `17` | Pair with `api-version-notes-17.md`: no documented `auth="bearer"` route flow, JSON routes still use `type="json"`. |
| `18` | Pair with `api-version-notes-18.md`: `auth="bearer"` is documented and can be used deliberately for token APIs. |
| `19` | Pair with `api-version-notes-19.md`: route docs move JSON endpoints to `type="jsonrpc"`. |

If this file conflicts with the active version skill or version API notes, the version-specific file wins.

## Configuration storage

Prefer a small configuration model or `ir.config_parameter` wrapper instead of hardcoding credentials.

```python
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ExternalApiConfig(models.Model):
    _name = "external.api.config"
    _description = "External API Configuration"

    name = fields.Char(required=True)
    base_url = fields.Char(required=True)
    api_key = fields.Char(groups="base.group_system")
    api_secret = fields.Char(groups="base.group_system")
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company,
        required=True,
    )
    active = fields.Boolean(default=True)

    @api.constrains("base_url")
    def _check_base_url(self):
        for record in self:
            if not record.base_url.startswith(("http://", "https://")):
                raise ValidationError("Base URL must start with http:// or https://")
```

Rules:
- Restrict secret fields with `groups=`.
- Keep one active config per company unless the integration explicitly supports multiple endpoints.
- Use `ir.config_parameter` for simple singleton settings, not for large sync state.

## Reusable HTTP client

Keep network code out of controllers and business objects. Put it in a service-like abstract model.

```python
import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from odoo import models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ApiClientMixin(models.AbstractModel):
    _name = "api.client.mixin"
    _description = "Reusable API Client"

    def _get_api_config(self):
        config = self.env["external.api.config"].search([
            ("company_id", "=", self.env.company.id),
            ("active", "=", True),
        ], limit=1)
        if not config:
            raise UserError("No active external API configuration found.")
        return config

    def _get_session(self):
        session = requests.Session()
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _get_headers(self):
        config = self._get_api_config()
        return {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json",
        }

    def _request(self, method, path, *, json=None, params=None, timeout=30):
        config = self._get_api_config()
        url = f"{config.base_url.rstrip('/')}/{path.lstrip('/')}"
        session = self._get_session()
        try:
            response = session.request(
                method=method,
                url=url,
                headers=self._get_headers(),
                json=json,
                params=params,
                timeout=timeout,
            )
            response.raise_for_status()
            return response
        except requests.Timeout as exc:
            _logger.warning("API timeout %s %s", method, url)
            raise UserError("External API request timed out.") from exc
        except requests.RequestException as exc:
            _logger.exception("API request failed %s %s", method, url)
            raise UserError("External API request failed.") from exc
```

Rules:
- Always set timeouts.
- Retry only idempotent-safe operations or endpoints documented as retry-safe.
- Raise user-safe errors from service methods; do not leak raw stack traces to UI or public controllers.

## Inbound sync pattern

Use mapping models and idempotent keys so repeated deliveries do not duplicate records.

```python
from odoo import api, fields, models


class ExternalOrderMap(models.Model):
    _name = "external.order.map"
    _description = "External Order Mapping"

    external_id = fields.Char(required=True, index=True)
    company_id = fields.Many2one("res.company", required=True, index=True)
    sale_order_id = fields.Many2one("sale.order", index=True)

    _sql_constraints = [
        (
            "external_order_unique",
            "unique(external_id, company_id)",
            "External order already mapped for this company.",
        ),
    ]

    @api.model
    def sync_one_payload(self, payload):
        mapping = self.search([
            ("external_id", "=", str(payload["id"])),
            ("company_id", "=", self.env.company.id),
        ], limit=1)
        if mapping:
            mapping.sale_order_id.write({
                "client_order_ref": payload.get("reference"),
            })
            return mapping.sale_order_id

        order = self.env["sale.order"].create({
            "partner_id": payload["partner_id"],
            "client_order_ref": payload.get("reference"),
        })
        self.create({
            "external_id": str(payload["id"]),
            "company_id": self.env.company.id,
            "sale_order_id": order.id,
        })
        return order
```

Rules:
- Back idempotency with SQL uniqueness, not only Python pre-checks.
- Keep mapping state explicit.
- For concurrency and savepoint behavior, pair with `transaction-safety-patterns.md`.

## Outbound push pattern

Do not hide third-party writes inside broad `write()` overrides unless the repo explicitly wants synchronous coupling.

Prefer:
- explicit action methods
- cron-based queue processing
- post-commit or retryable background jobs when available in the target stack

Safer shape:

```python
class ResPartner(models.Model):
    _inherit = "res.partner"

    external_customer_id = fields.Char()
    sync_to_external = fields.Boolean(default=True)

    def action_queue_external_sync(self):
        for partner in self.filtered("sync_to_external"):
            self.env["external.sync.job"].create({
                "model_name": partner._name,
                "res_id": partner.id,
                "job_type": "push_partner",
            })
```

Rules:
- Avoid calling remote APIs inside hot UI writes when latency or failure would degrade normal user workflows.
- Queue and retry long-running or flaky integrations.

## Webhook pattern

Use raw-body signature verification and thin controllers.

```python
import hashlib
import hmac

from odoo import http
from odoo.http import request


class WebhookController(http.Controller):
    @http.route("/webhook/external", type="http", auth="none", methods=["POST"], csrf=False)
    def external_webhook(self, **kwargs):
        secret = request.env(su=True)["ir.config_parameter"].get_param("my_module.webhook_secret")
        signature = request.httprequest.headers.get("X-Signature", "")
        payload = request.httprequest.get_data()
        expected = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            return request.make_response("bad signature", status=400)

        request.env(su=True)["external.webhook.handler"].handle_payload(payload)
        return request.make_response("OK", status=200)
```

Rules:
- Verify the raw body, not a reserialized dict.
- Keep webhook logic idempotent.
- Acknowledge quickly; push expensive work into models/jobs.

## Token and route strategy

Pick route auth based on the version and the trust model:

- Internal frontend RPC: `auth="user"` with normal ACL/rule enforcement
- Public website callback: `auth="public"` or `auth="none"` plus signature/API-key checks
- Odoo 17 token API: manual bearer handling, then `request.update_env(...)`
- Odoo 18+: `auth="bearer"` can be used when that exact flow matches the endpoint contract
- Odoo 19: follow the documented route type and auth semantics from the matching API notes

## File and payload hygiene

- Whitelist writable fields before forwarding payloads into `create()` or `write()`.
- Validate enum values and required identifiers.
- Limit attachment size and accepted mimetypes before creating `ir.attachment`.
- Log enough for traceability, but never log secrets, full tokens, or raw PII payloads unnecessarily.

## Review checklist

- Credentials are not hardcoded.
- Timeouts and retry policy are explicit.
- Sync is idempotent.
- Remote failures do not corrupt local state silently.
- Public routes validate signature, token, or API key before ORM work.
- `sudo()` is narrow and justified.
- Multi-company sync keys include company scoping where needed.
