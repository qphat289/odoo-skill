# Example Clarification Register: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting `Clarification Register.xlsx`.

## Example workbook structure

### Sheet: `Clarifications`

| Q ID | Requirement ID | Area / Process | Question | Why It Matters | Blocking Level | Owner | Answer | Answer Source | Status | Impact Summary |
|---|---|---|---|---|---|---|---|---|---|---|
| CL-001 | RQ-003 | Credit Policy | which exact credit rule blocks confirmation: overdue amount, credit limit, or both? | fit-gap / solution / acceptance | Blocking | customer finance lead | block when overdue amount exists or credit limit is exceeded | finance workshop 2026-06-21 | Answered | credit check must combine both conditions |
| CL-002 | RQ-004 | Margin Policy | low-margin case should block or require approval? | fit-gap / scope / test acceptance | Blocking | product owner | require approval, do not hard block | product owner chat 2026-06-22 | Answered | classification stays process change + approval path |
| CL-003 | RQ-007 | Order Sync API | is outbound API synchronous only, or do we need async callback handling? | fit-gap / technical design / estimate | Blocking | integration owner | synchronous request/response only in phase 1 | integration call 2026-06-22 | Answered | no callback design needed in current scope |
| CL-004 | RQ-009 | Approval Notice | who receives approval request if no manager is assigned on the salesperson team? | workflow detail / fallback logic | Minor | sales manager | regional sales director fallback | chat 2026-06-23 | Answered | fallback notification rule added |

### Sheet: `Summary`

| Field | Value |
|---|---|
| Customer / Project | `ABC Distribution - Sales Approval Rollout` |
| Target Odoo Version | `18.0` |
| Register Status | `Ready` |
| Blocking Count | `0 open` |
| Minor Count | `0 open` |
| Ready For Fit-Gap | `Yes` |
