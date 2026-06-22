# Odoo Discovery Questionnaire

Use this reference to collect enough business detail before fit-gap analysis or implementation planning.

## Core sections

### 1. Customer context

- Company name and industry
- Business model
- Number of users, branches, warehouses, legal entities
- Target Odoo version or expected rollout window
- Decision makers and daily process owners

### 2. Current systems

- Which systems are used today for sales, accounting, inventory, HR, projects, ecommerce, and reporting
- Which flows still depend on spreadsheets or manual re-entry
- Known pain points, bottlenecks, or compliance constraints

### 3. Scope by business area

For each relevant area, capture the current flow, desired flow, exceptions, approval rules, reports, and external systems.

Suggested areas:

- Sales and CRM
- Purchase
- Inventory and logistics
- Manufacturing
- Accounting and invoicing
- HR
- Projects and services
- Website and ecommerce

### 4. Delivery context

- Must-have go-live scope
- Nice-to-have scope
- Budget range if available
- Timeline constraints
- Environment preference: Odoo.sh, on-premise, or managed hosting

## Red flags

Mark these early because they usually change effort materially:

- Multi-step approvals with many exceptions
- Heavy cross-company rules
- Legacy data in many formats
- Realtime external integrations
- Fixed-format government or partner reports
- Custom pricing, commissions, or allocation logic
- Requirements that conflict with standard Odoo process assumptions

## Output template

```markdown
# Discovery Notes

## Customer Context

## Current Systems

## Business Areas

## Constraints and Risks

## Open Questions

## Suggested Next Step
```

