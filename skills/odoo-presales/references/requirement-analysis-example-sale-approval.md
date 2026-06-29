# Example Requirement Analysis: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting `Requirement Analysis.md`.

It is paired conceptually with:

- `skills/odoo-presales/references/fit-gap-analysis-example-sale-approval.md`
- `skills/odoo-module-generation/references/technical-design-example-sale-approval.md`
- `skills/odoo-quality/references/test-plan-example-sale-approval.md`
- `skills/odoo-module-generation/references/project-tracking-example-sale-approval.md`

## Scenario summary

- Target Odoo version: `18.0`
- Business area: Sales, CRM, Approval, Customer sync
- Example filename: `Requirement Analysis.md`

## Example artifact

```markdown
# Requirement Analysis

## 1. Source Files

| File | Type | Scope / Notes |
|---|---|---|
| `Customer_SOW_v2.docx` | DOCX | commercial scope and functional objectives |
| `Sales_CRM_Workshop_Notes.xlsx` | XLSX | detailed flow notes, priorities, and clarification dependencies |
| `MOM_2026-06-20.pdf` | PDF | phase boundary and stakeholder decisions |

## 2. Analysis Summary

- Customer / project: `ABC Distribution - Sales Approval Rollout`
- Target Odoo version: `18.0`
- Analysis status: `Approved for fit-gap`
- Main business areas:
  - Sales quotation approval
  - CRM opportunity handoff
  - External order sync
- Known phase boundary:
  - Phase 1 includes sales approval, CRM handoff, and outbound sync only
- Main assumptions:
  - quotation approval applies before final confirmation
  - outbound sync applies only to approved/confirmed quotations
  - stock customization is not in current phase

## 3. Requirement Inventory

| Req ID | Module / Area | Process / Function | Customer Requirement | Source Ref | Priority | Scope Status | Notes |
|---|---|---|---|---|---|---|---|
| RQ-001 | Sales | Quotation Approval | quotation above threshold requires manager approval before confirmation | `Customer_SOW_v2.docx §3.2` | High | In Scope | core phase-1 requirement |
| RQ-002 | Sales | Standard Confirmation | quotation below threshold must keep standard flow | `Workshop row 14` | High | In Scope | regression-sensitive |
| RQ-003 | Sales / Finance | Credit Policy | customer over credit limit must not confirm quotation | `Customer_SOW_v2.docx §3.4` | High | In Scope | exact policy source still to verify |
| RQ-004 | Sales | Margin Policy | low-margin quotation needs special handling | `Workshop row 22` | Medium | In Scope | exact business rule not fully confirmed |
| RQ-005 | CRM / Sales | Opportunity To Quotation | salesperson can create quotation from qualified opportunity with default values | `Customer_SOW_v2.docx §4.1` | High | In Scope | requires field mapping |
| RQ-006 | CRM | Qualification Gate | non-qualified lead must not create quotation | `Workshop row 31` | Medium | In Scope | likely small guard rule |
| RQ-007 | Sales / Integration | Order Sync API | approved quotation must sync to external order platform | `Customer_SOW_v2.docx §5.2` | High | In Scope | integration owner identified |
| RQ-008 | Integration | Retry / Idempotency | sync retry must not create duplicate external order | `Workshop row 39` | High | In Scope | major technical risk |
| RQ-009 | Sales / Notification | Approval Notice | approver must receive approval request notification | `Customer_SOW_v2.docx §3.6` | Medium | In Scope | recipient rule still needs confirmation |
| RQ-010 | Stock | Delivery Customization | stock picking customization for approved order | `MOM_2026-06-20 item 8` | Low | Later Phase | explicitly out of phase 1 |

## 4. Requirement Grouping

| Group ID | Group Name | Included Req IDs | Why Grouped |
|---|---|---|---|
| G-001 | Approval Flow | RQ-001, RQ-002, RQ-003, RQ-004, RQ-009 | same quotation approval process |
| G-002 | CRM Handoff | RQ-005, RQ-006 | same opportunity-to-quotation flow |
| G-003 | External Sync | RQ-007, RQ-008 | same outbound integration flow |
| G-004 | Future Scope | RQ-010 | not for current delivery phase |

## 5. Clarification Register Status

- Clarification artifact: `Clarification Register.xlsx`
- Blocking clarification status:
  - `CL-001` credit rule source: Answered
  - `CL-002` low-margin treatment: Answered
  - `CL-003` outbound API sync mode: Answered
- Minor clarification status:
  - `CL-004` fallback approval recipient: Answered
- Ready for fit-gap: `Yes`

## 6. Scope Boundaries

### In Scope

- quotation approval flow
- credit and margin policy handling
- CRM opportunity to quotation handoff
- outbound order sync
- approval notification

### Out Of Scope

- stock picking customization
- invoice customization
- warehouse process changes

### Later Phase / Backlog Candidates

- stock picking customization for approved quotations
- deeper finance approval matrix
- sync callback dashboard

## 7. Next-Step Recommendation

- Recommended next workflow: `workflows/fit-gap.md`
- Ready for fit-gap: `Yes`
- Key blockers before fit-gap:
  - none
```

## Why this example is useful

1. It shows how to normalize mixed customer inputs before classification starts.
2. It keeps the result lean and working-oriented instead of turning it into early Functional Design.
3. It gives stable `RQ-xxx` IDs that can flow into `FG-xxx`, `TD`, `TP`, and `T-xxx`.
4. It uses the same scenario as the downstream examples, so the whole chain feels coherent.
