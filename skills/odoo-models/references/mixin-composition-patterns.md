# Mixin Composition Patterns

Use this reference when the task needs chatter, activities, portal access, aliases, ratings, images, or marketing tracking.

## When to load this file

- model inherits `mail.thread`, `mail.activity.mixin`, or `portal.mixin`
- feature includes followers, chatter, activities, or email alias intake
- records need share links, ratings, avatars, or UTM attribution

## Core mixins

| Mixin | Use for | Notes |
|---|---|---|
| `mail.thread` | chatter, tracking, followers, messages | add `tracking=True` to important fields |
| `mail.activity.mixin` | scheduled activities | usually paired with `mail.thread` |
| `mail.alias.mixin.optional` | optional inbound email aliases | lighter than full alias inheritance |
| `mail.alias.mixin` | required alias-backed records | use only when every record needs an alias |
| `portal.mixin` | portal share URLs and access tokens | pair with portal routes/views |
| `rating.mixin` | partner ratings | already brings mail-thread behavior |
| `utm.mixin` | campaign/source/medium attribution | useful for website lead capture |
| `image.mixin` | image fields with resized variants | backend and website image records |
| `avatar.mixin` | generated avatars | simple visual identity without uploaded files |

## Safe composition patterns

### Standard business document

```python
class ApprovalRequest(models.Model):
    _name = "approval.request"
    _description = "Approval Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
        ],
        default="draft",
        tracking=True,
    )
    approver_id = fields.Many2one("res.users", tracking=True)
```

Use this for most workflow-driven custom models.

### Portal-visible record

```python
class ServiceRequest(models.Model):
    _name = "service.request"
    _inherit = ["portal.mixin", "mail.thread", "mail.activity.mixin"]

    partner_id = fields.Many2one("res.partner", required=True)

    def _compute_access_url(self):
        super()._compute_access_url()
        for record in self:
            record.access_url = f"/my/service_requests/{record.id}"
```

Use when external users need signed access links.

### Alias-driven intake

```python
class HelpdeskTeam(models.Model):
    _name = "helpdesk.team"
    _inherit = ["mail.thread", "mail.activity.mixin", "mail.alias.mixin.optional"]

    def _alias_get_creation_values(self):
        values = super()._alias_get_creation_values()
        values["alias_model_id"] = self.env["ir.model"]._get("helpdesk.ticket").id
        if self.id:
            values["alias_defaults"] = {"team_id": self.id}
        return values
```

Prefer `mail.alias.mixin.optional` unless every record must own an alias.

### Rated workflow

```python
class ProjectTask(models.Model):
    _name = "project.task"
    _inherit = ["rating.mixin", "mail.activity.mixin"]

    name = fields.Char(required=True)
    partner_id = fields.Many2one("res.partner")
```

Do not redundantly add `mail.thread` unless the codebase already does so consistently.

## Chatter view note by version

- Odoo 14-17: use the classic chatter block
- Odoo 18+: the `<chatter/>` shortcut is acceptable

### Safe cross-version chatter block

```xml
<div class="oe_chatter">
    <field name="message_follower_ids"/>
    <field name="activity_ids"/>
    <field name="message_ids"/>
</div>
```

Use this when you want one pattern that stays safe across multiple versions.

## Tracking rules

- Add `tracking=True` only to fields that matter to users.
- Track workflow states, assignees, amounts, and key approvals.
- Avoid tracking noisy technical fields.

### Good tracking example

```python
name = fields.Char(required=True, tracking=True)
state = fields.Selection([...], default="draft", tracking=True)
user_id = fields.Many2one("res.users", tracking=True)
```

### Noisy tracking anti-pattern

```python
write_date = fields.Datetime(tracking=True)  # avoid
sequence = fields.Integer(tracking=True)     # usually avoid
```

## Activity rules

- Schedule activities for human follow-up, not for every state change.
- Mark old workflow activities done when a later state supersedes them.

```python
self.activity_schedule(
    "mail.mail_activity_data_todo",
    summary="Review request",
    user_id=self.user_id.id,
)
```

## Alias rules

- Keep alias defaults small and deterministic.
- Do not create aliases for records that will never receive email input.
- Pair alias-based creation with clear security and ownership defaults.

## Portal rules

- `portal.mixin` only solves tokenized access primitives; it does not replace controller security.
- Pair it with `odoo-security` for record access rules and portal-facing checks.

## Image/avatar rules

- Use `image.mixin` for records that need uploaded artwork or product-like media.
- Use `avatar.mixin` for people/teams/simple visual entities where generated avatars are acceptable.

## Checklist

- [ ] chosen mixins match the business use case instead of being copied blindly
- [ ] chatter/activity UI matches target version
- [ ] tracked fields are intentional and low-noise
- [ ] alias and portal features are paired with security review
- [ ] image/avatar mixins are used only when the UI actually needs them
