# Example Technical Design: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting a full `Technical Design.md`. It is paired with:

- `skills/odoo-quality/references/test-plan-example-sale-approval.md`
- `skills/odoo-module-generation/references/project-tracking-example-sale-approval.md`

The goal is to show how a technical design can stay implementation-oriented while remaining traceable to business scope and ready for QA/QC and delivery tracking.

## Scenario summary

- Target Odoo version: `18.0`
- Business area: Sales, CRM, Approval, Customer sync
- Custom modules:
  - `x_sale_approval`
  - `x_crm_sale_bridge`
  - `x_sale_sync_api`
- Standard dependencies:
  - `sale`
  - `sale_management`
  - `crm`
  - `mail`

## Example artifact

```markdown
# Technical Design

## 1. Source Artifacts

| Artifact | Path / Version | Status | Notes |
|---|---|---|---|
| Requirement Analysis | `docs/analysis/Requirement Analysis.md` | Approved | requirement inventory normalized and phase boundary confirmed |
| Clarification Register | `docs/analysis/Clarification Register.xlsx` | Approved | blocking and minor clarifications resolved before design handoff |
| Functional Design | `docs/design/Functional Design.docx` | Approved | process, role, approval, and sync flow confirmed |
| Solution Design | `docs/design/Solution Design.docx` | Approved | custom approval and outbound sync approach selected |
| Fit/Gap Analysis | `docs/analysis/Fit-Gap.xlsx` | Approved | custom logic and API sync classified as custom/integration |

## 2. Technical Summary

- Target Odoo version: `18.0`
- Target module technical name:
  - `x_sale_approval`
  - `x_crm_sale_bridge`
  - `x_sale_sync_api`
- Existing modules to depend on:
  - `sale`
  - `sale_management`
  - `crm`
  - `mail`
- Standard modules to inherit:
  - `sale.order`
  - `sale.order.line`
  - `crm.lead`
  - `ir.config_parameter`
  - `mail.activity`
  - `mail.template`
- Custom module(s):
  - `x_sale_approval`: approval logic and sales policy rules
  - `x_crm_sale_bridge`: CRM-to-sale mapping and qualification gate
  - `x_sale_sync_api`: outbound sync, payload log, retry, and idempotency
- Implementation sequencing notes:
  - build approval core first because CRM bridge and outbound sync depend on stable sale-order state behavior
  - lock security and approval-state semantics before retry and integration work
  - create automated tests as each module slice stabilizes instead of waiting until the end

## 3. Requirement Traceability

| Req ID | Fit/Gap ID | Functional Section | Solution Decision | Technical Section | Test Plan Hint | Tracking Hint | Build Treatment |
|---|---|---|---|---|---|---|---|
| RQ-001 | GAP01 | FD-2.1 quotation approval | custom approval extension on `sale.order` | Model and Data Design; Business Logic Design; View Design; Security Design | TP-002, TP-003, TP-005 | T-001, T-002, T-003, T-005 | extend `sale.order` with approval state and methods |
| RQ-002 | GAP01 | FD-2.4 credit limit validation | server-side validation before confirm | Business Logic Design; Security Design | TP-006 | T-006, T-009 | add guarded confirm validation |
| RQ-003 | GAP01 | FD-2.5 low margin policy | approval path instead of hard stop | Model and Data Design; Business Logic Design | TP-007 | T-009, T-010 | compute margin and policy check |
| RQ-004 | GAP02 | FD-3.1 opportunity handoff | custom bridge from qualified `crm.lead` to quotation defaults | Model and Data Design; Business Logic Design; View Design | TP-008, TP-009 | T-011, T-012, T-013 | extend action and default mapping |
| RQ-005 | GAP03 | SD-4.2 approved order sync | dedicated integration module with payload log | Model and Data Design; Business Logic Design; Integration Design; Automation Design | TP-010, TP-011, TP-013 | T-014, T-015, T-016, T-018 | outbound REST integration |
| RQ-006 | GAP03 | SD-4.4 sync access control | service-user-only sync operations | Security Design; Integration Design | TP-012 | T-017 | protected actions and fields |

## 4. Module And Dependency Design

### 4.1 Build order / dependency order

1. `x_sale_approval`
2. `x_crm_sale_bridge`
3. `x_sale_sync_api`

Why:

- approval state is a prerequisite for downstream handoff and sync eligibility
- CRM bridge depends on stable order defaults and qualification guards
- sync module depends on confirmed approval behavior and protected service operations

### `x_sale_approval`

- Depends on:
  - `sale`
  - `sale_management`
  - `mail`
- Main responsibilities:
  - approval threshold
  - manager approval
  - credit limit validation
  - margin policy
  - approval notifications
- Load order:
  - security groups and ACL
  - config defaults if any
  - mail template
  - views

### `x_crm_sale_bridge`

- Depends on:
  - `crm`
  - `sale`
  - `x_sale_approval`
- Main responsibilities:
  - qualified opportunity -> quotation defaults
  - qualification guard
  - field mapping

### `x_sale_sync_api`

- Depends on:
  - `sale`
  - `x_sale_approval`
- Main responsibilities:
  - sync payload build
  - outbound API call
  - sync log and external reference
  - retry and idempotency

## 5. Model And Data Design

### 5.1 Model: `sale.order` via `_inherit`

- Purpose:
  - carry approval state and sync-related business fields
- `_name` / `_inherit`:
  - `_inherit = "sale.order"`
- Key fields:
  - `x_requires_approval` boolean
  - `x_approved_by` many2one `res.users`
  - `x_approval_date` datetime
  - `x_sync_state` selection
  - `x_external_sync_ref` char
- Computed fields:
  - `x_requires_approval`
  - optional `x_margin_percent`
- Constraints:
  - approval-specific state transitions must be coherent
  - sync state and external ref must align
- Onchange / CRUD behavior:
  - threshold and margin must refresh when quotation lines change
  - confirm path must branch to approval logic only when needed
- Company behavior:
  - `_check_company_auto = True`
  - relational fields with company-sensitive models use `check_company=True`
- Data loading:
  - no base data records beyond mail template and config defaults

### 5.2 Model: `sale.order.line` via `_inherit`

- Purpose:
  - support low-margin policy inputs
- Key fields:
  - optional `x_cost_price`
  - optional `x_line_margin`
- Computed fields:
  - margin-related helpers when not directly using standard fields
- Onchange / CRUD behavior:
  - line edits must feed order-level approval recompute

### 5.3 Model: `crm.lead` via `_inherit`

- Purpose:
  - carry qualification and mapping fields needed for quotation defaults
- Key fields:
  - `x_qualification_status`
  - `x_budget`
  - `x_timeline`
  - `x_competitor`
- Onchange / CRUD behavior:
  - quotation creation must be blocked for disallowed qualification states

### 5.4 Model: `x.sale.sync.log`

- Purpose:
  - persist outbound sync attempts and responses
- `_name`:
  - `x.sale.sync.log`
- Key fields:
  - `sale_order_id`
  - `request_payload`
  - `response_code`
  - `response_body`
  - `idempotency_key`
  - `retry_count`
  - `state`
- Constraints:
  - one active idempotency key per logical outbound sync cycle
- Company behavior:
  - linked to `sale.order.company_id`

## 6. Business Logic Design

### 6.1 Approval threshold entry

- Override `sale.order.action_confirm()`.
- If quotation total or policy conditions require approval:
  - do not call full standard confirmation yet
  - set state to `pending_approval`
  - log or notify approval request
- If approval not required:
  - preserve standard confirmation flow unchanged

### 6.2 Approval resume

- Method `action_approve()` allowed only for manager group.
- Required behavior:
  - set approver metadata
  - resume standard confirmation exactly once
  - avoid duplicate downstream side effects

### 6.3 Credit policy check

- Before standard confirmation:
  - evaluate partner credit policy
  - raise business-facing error when blocked
- Must be server-side, not only view logic.

### 6.4 Margin policy check

- Evaluate low-margin lines during confirm path or earlier validation hook.
- If margin rule says approval:
  - reuse approval flow
- If margin rule says block:
  - raise controlled error

### 6.5 CRM bridge logic

- Extend quotation creation action from `crm.lead`.
- Only allow allowed qualification states.
- Map approved lead fields into quotation defaults:
  - partner / contact
  - notes
  - timeline
  - tags or custom fields where applicable

### 6.6 Sync payload build

- Build payload only from approved/confirmed orders.
- Exclude internal-only or sensitive fields from outbound payload.
- Persist payload snapshot in sync log for troubleshooting.

### 6.7 Retry and idempotency

- Persist idempotency key before external call.
- Retry path must reuse or deliberately manage the same logical key.
- Duplicate remote record creation must be prevented.

## 7. View, Menu, Action, Wizard, And Report Design

- `sale.order` form:
  - show approval metadata
  - show sync state
  - approval button visible only for managers and only in `pending_approval`
- `crm.lead` form:
  - show qualification-related fields
  - provide action to create quotation when allowed
- Sync log views:
  - tree + form for support/admin roles
  - smart button from sale order if useful
- No new wizard required unless manual sync confirmation becomes necessary later.

## 8. Security Design

- Groups:
  - `x_sale_approval.group_sale_approver`
  - optional `x_sale_sync_api.group_sync_manager`
- ACL:
  - sync log readable by support/admin roles only
  - no broad write access to technical sync records for normal users
- Record rules:
  - company-based access for custom records
  - no cross-company leak from sync log
- Server-side permission checks:
  - `action_approve()` checks group membership
  - sync actions check allowed group or service user role
  - no UI-only reliance for protected operations
- Multi-company notes:
  - use `_check_company_auto = True`
  - use `check_company=True` on company-scoped relations
  - keep rule domains on `company_ids`

## 9. Integration Design

- External systems:
  - external order-sync API
- Direction:
  - outbound
- Payload/data mapping:
  - order header
  - customer reference
  - approved metadata
  - line items
  - exclude internal notes and protected fields
- Authentication:
  - config-driven API key or token from `ir.config_parameter`
- Error handling:
  - log code/body per attempt
  - set sync state to failed/pending retry as appropriate
- Retry/reconciliation:
  - idempotency key required
  - retry count tracked
  - reconciliation by external reference or idempotency key

## 10. Automation And Notification Design

- Approval request email:
  - triggered when order enters `pending_approval`
- Optional scheduled retry:
  - cron job may retry failed sync records in retryable states
- Activity scheduling:
  - optional mail activity for approver if business requires it

## 11. Data Migration And Configuration Design

- Configuration parameters:
  - approval threshold
  - API endpoint
  - API key/token
  - retry limit
- No historical data migration in first phase unless existing quotations need approval-state backfill.
- If backfill is later needed:
  - do via migration script, not ad hoc UI update

## 12. Performance, Logging, And Operations

- Avoid re-query loops during confirm and sync batch operations.
- Do not call `sudo()` inside loops.
- Sync logging must be sufficient for support without exposing secrets.
- Keep payload logging structured enough to debug but redact sensitive fields if needed.
- For batch retries, prefer recordset operations and bounded retry selection.

## 13. Test Planning Notes

- Unit / transaction tests:
  - approval threshold
  - approval resume
  - credit limit
  - margin policy
  - CRM qualification guard
  - payload build
- Security tests:
  - salesperson cannot approve
  - sales user cannot access protected sync action
  - multi-company access isolation
- Workflow tests:
  - quotation under threshold
  - quotation over threshold
  - opportunity -> quotation
- Integration tests:
  - successful outbound sync
  - retry and idempotency
- UAT support notes:
  - manager approval and outbound sync end-to-end
- Full case-by-case coverage and status: see `Test Plan.md`

## 14. Technical Risks And Preconditions

| ID | Topic | Risk / Precondition | Impact | Owner |
|---|---|---|---|---|
| TR-001 | approval resume | duplicate downstream confirmation may occur if custom method wraps standard flow incorrectly | high | Dev A |
| TR-002 | recompute | approval flag may go stale after line edit if depends/onchange path is incomplete | high | Dev A |
| TR-003 | idempotency | retry logic may create duplicate external records if key persistence is late | critical | Dev B |
| TR-004 | UAT dependency | business validation waits on stable SIT and critical defect closure | medium | PM |

## 15. Build Readiness Checklist

- [x] Functional Design source is identified
- [x] Solution Design source is identified
- [x] target Odoo version is confirmed
- [x] dependencies are known
- [x] every persistent model has ACL plan
- [x] security-sensitive flows have server-side checks
- [x] tests are identified for non-trivial logic
```

## Why this example is useful

1. It gives the agent a concrete model for turning business scope into module boundaries, model design, and implementation logic.
2. It stays technical without collapsing into backlog or execution status.
3. It names the same risks that later appear in the QA/QC and Project Tracking examples, so the handoff chain stays consistent.
4. It shows how to carry requirement IDs and fit-gap IDs into downstream QA/QC and tracking references.
5. It shows how to design both business logic and integration logic in the same artifact without losing traceability.
6. It creates a strong bridge from customer-facing design into automated tests and delivery tracking.
