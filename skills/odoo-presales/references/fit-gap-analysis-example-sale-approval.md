# Example Fit-Gap Analysis: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting `Fit-Gap Analysis.xlsx`.

It is paired conceptually with:

- `skills/odoo-presales/references/clarification-register-example-sale-approval.md`
- `skills/odoo-module-generation/references/technical-design-example-sale-approval.md`
- `skills/odoo-quality/references/test-plan-example-sale-approval.md`
- `skills/odoo-module-generation/references/project-tracking-example-sale-approval.md`

## Scenario summary

- Target Odoo version: `18.0`
- Business area: Sales, CRM, Approval, Customer sync
- Example filename: `Fit-Gap Analysis.xlsx`

## Example workbook structure

### Sheet: `Overview`

| Field | Value |
|---|---|
| Customer / Project | `ABC Distribution - Sales Approval Rollout` |
| Target Odoo Version | `18.0` |
| Analysis Status | `Approved` |
| Clarification Register Status | `Ready` |
| Prepared By | `FC / solution owner` |
| Scope Boundary | `Phase 1 covers quotation approval, CRM handoff, and outbound order sync` |
| Total Requirement Rows | `10` |

### Sheet: `Fit-Gap Matrix`

| ID | Requirement ID | Requirement Summary | Business Area | Module / Process | Classification | Proposed Approach | Scope Status | Phase | Priority | Source Ref | Clarification Ref | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FG-001 | RQ-001 | quotation above threshold needs manager approval before confirmation | Sales | Sale Order Approval | Customization | extend `sale.order` with approval state and manager action | In scope | Phase 1 | High | `SOW section 3.2` |  | maps to approval workflow |
| FG-002 | RQ-002 | quotation below threshold should keep standard confirm flow | Sales | Sale Order Approval | Fit | reuse standard `sale.order` confirm path when approval not required | In scope | Phase 1 | High | `Workshop note W-04` |  | regression-sensitive |
| FG-003 | RQ-003 | customer over credit limit cannot confirm quotation | Sales / Finance | Credit Policy | Customization | add server-side credit validation before confirm | In scope | Phase 1 | High | `SOW section 3.4` | `CL-001` | finance policy confirmed in clarification register |
| FG-004 | RQ-004 | low-margin quotations need special handling | Sales | Margin Policy | Process change | use approval policy instead of full hard block | In scope | Phase 1 | Medium | `Workshop W-08` | `CL-002` | business decision confirmed: approval path |
| FG-005 | RQ-005 | salesperson can create quotation from qualified opportunity | CRM / Sales | Opportunity To Quotation | Customization | extend CRM lead action and quotation defaults mapping | In scope | Phase 1 | High | `SOW section 4.1` |  | depends on qualification status |
| FG-006 | RQ-006 | non-qualified leads must not create quotations | CRM | Lead Qualification | Configuration | use qualification statuses and UI/action guard | In scope | Phase 1 | Medium | `Workshop W-11` |  | may be config plus small code guard |
| FG-007 | RQ-007 | approved quotation must sync to external order platform | Sales / Integration | Order Sync API | Integration | outbound REST connector with payload mapping and sync log | In scope | Phase 1 | High | `SOW section 5.2` | `CL-003` | phase 1 scope uses synchronous request/response |
| FG-008 | RQ-008 | outbound sync retry must not create duplicate external order | Integration | Retry / Idempotency | Integration | persist idempotency key and retry state in custom sync log | In scope | Phase 1 | High | `Workshop W-15` |  | critical technical risk |
| FG-009 | RQ-009 | users need approval request email notification | Sales / Notification | Approval Notification | Configuration | mail template plus activity or email trigger | In scope | Phase 1 | Medium | `SOW section 3.6` | `CL-004` | fallback recipient rule confirmed |
| FG-010 | RQ-010 | stock picking customization for approved order is not part of phase 1 | Stock | Delivery | Out of scope | keep visible in later phase list only | Later phase | Phase 2 | Low | `Meeting MOM-03` |  | must not leak into current scope |

## Why this example is useful

1. It shows why `Fit-Gap` is better as `.xlsx`: every requirement stays one row and stays traceable.
2. It separates fit, customization, integration, process change, and out-of-scope decisions clearly.
3. It gives stable `FG-xxx` IDs that later artifacts can cite.
4. It shows how fit-gap rows cite clarified answers instead of carrying open-question debt downstream.
5. It uses the same scenario as the Technical Design, Test Plan, and Project Tracking examples, so the chain feels coherent.
