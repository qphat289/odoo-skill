---
name: odoo-business-domains
description: Domain skill for reusable Odoo business-flow patterns such as sales, stock, accounting, HR, project, pricing, tax, and procurement across Odoo 14-19.
---

# Odoo Business Domains

Use this skill when the task depends on established business-module semantics rather than only low-level ORM or XML syntax.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Sales and CRM | `references/sale-crm-patterns.md` | Quotations, opportunities, sales workflows |
| Purchase and procurement | `references/purchase-procurement-patterns.md` | Purchasing, replenishment, vendor flows |
| Stock and inventory | `references/stock-inventory-patterns.md` | Pickings, quants, reservations, inventory ops |
| Accounting and taxes | `references/accounting-patterns.md`, `references/tax-fiscal-patterns.md` | Accounting entries, taxes, fiscal logic |
| HR and employees | `references/hr-employee-patterns.md` | Employee-linked flows and HR records |
| Project and tasks | `references/project-task-patterns.md` | Project stages, tasks, service delivery |
| Product, pricing, and variants | `references/product-variant-patterns.md`, `references/pricelist-pricing-patterns.md` | Catalog logic, variants, pricing rules |
| Lots, serials, and UoM | `references/lot-serial-patterns.md`, `references/uom-patterns.md` | Traceability, units, stock conversions |

## Rules

1. Use this skill only after the active version skill is known.
2. Do not use these domain references as a substitute for `odoo-models`, `odoo-security`, or `odoo-views`; pair them when implementation details matter.
3. Prefer the narrowest business reference that matches the user flow instead of loading the whole pack.
