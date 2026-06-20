# Odoo Test Tooling Patterns

Use this file when the task is about choosing the right Odoo test class, using `Form`, patching dependencies, or catching performance regressions with query assertions.

## Version guardrails

- `TransactionCase`, `HttpCase`, and `Form` are stable concepts across the supported versions in this repo.
- Query/performance helpers can differ in emphasis between older and newer versions, so performance assertions should be checked against the active version skill on legacy targets.
- Use this file as the shared baseline, then confirm version-specific details in the active version skill when writing strict regression tests.

## Pick the right base class

| Use case | Base class | Notes |
|---|---|---|
| Most model and service tests | `TransactionCase` | Default choice |
| Heavy shared mutable state across methods | `SingleTransactionCase` | Use sparingly |
| HTTP endpoints, tours, browser behavior | `HttpCase` | Usually with `post_install` |

### Default baseline

```python
from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestMyFlow(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create({"name": "Demo"})
```

## Form-driven tests

Use `Form` when onchange logic, defaults, modifiers, or x2many inline editing matter.

```python
from odoo.tests.common import Form


def test_create_with_form(self):
    with Form(self.env["my.model"]) as form:
        form.name = "Demo"
        form.partner_id = self.partner
        with form.line_ids.new() as line:
            line.name = "Line A"
            line.quantity = 2
    record = form.record
    self.assertEqual(record.name, "Demo")
```

Use raw `create()` only when UI behavior is not part of the test.

## Query-count and warmup

Use `@warmup` with `assertQueryCount` when guarding against N+1 or cache-sensitive regressions.

```python
from odoo.tests.common import warmup


@warmup
def test_partner_lookup_cost(self):
    with self.assertQueryCount(3):
        self.env["my.model"].search([]).mapped("partner_id.name")
```

Rules:
- Cold-cache counts are noisy.
- Use this only for stable, meaningful hot paths.

Version note:
- On older targets, if query assertion helpers differ from the current baseline, follow the active version references instead of forcing the newer pattern.

## Patching and mocking

Prefer Odoo test helpers over manual patch lifecycle handling.

```python
from unittest.mock import patch


def test_external_call(self):
    mock_post = self.startPatcher(patch("requests.post"))
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"ok": True}

    result = self.env["my.model"].call_external()

    self.assertTrue(result)
    mock_post.assert_called_once()
```

Class-wide patch:

```python
@classmethod
def setUpClass(cls):
    super().setUpClass()

    def _always_ok(self):
        return True

    cls.classPatch(type(cls.env["my.model"]), "_check_remote", _always_ok)
```

## HTTP and tour tests

```python
from odoo.tests.common import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestMyUi(HttpCase):
    def test_controller(self):
        response = self.url_open("/my_module/ping")
        self.assertEqual(response.status_code, 200)

    def test_tour(self):
        self.start_tour("/web", "my_module_tour", login="admin")
```

Rules:
- Keep `HttpCase` for real UI or HTTP behavior.
- Do not use browser tests for pure ORM logic.

## Users and record capture

### `new_test_user`

```python
from odoo.tests.common import new_test_user


@classmethod
def setUpClass(cls):
    super().setUpClass()
    cls.user_manager = new_test_user(
        cls.env,
        login="manager_demo",
        groups="base.group_user,my_module.group_manager",
    )
```

### `RecordCapturer`

```python
from odoo.tests.common import RecordCapturer


def test_created_messages(self):
    with RecordCapturer(self.env["mail.message"], [("model", "=", "my.model")]) as cap:
        self.env["my.model"].create({"name": "Demo"})
    self.assertTrue(cap.records)
```

## Practical review checklist

- Base class matches the real scope of the test.
- `HttpCase` is tagged `post_install`.
- `Form` is used when onchange/default/UI logic matters.
- External services are mocked.
- Security rules are tested with `with_user(...)`.
- Performance-sensitive flows use query assertions when justified.

## Common mistakes

- Using `HttpCase` for plain model tests.
- Testing onchange with raw `create()` and assuming equivalent coverage.
- Manual `patch().start()` without reliable cleanup.
- Query-count checks without warmup on cache-sensitive code.
