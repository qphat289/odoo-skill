# Odoo Effort Estimation Guide

Use this reference for rough presales sizing before detailed planning.

## Estimation principles

1. Estimate in ranges, not single-point promises.
2. Separate configuration, customization, integration, migration, testing, and project overhead.
3. Add explicit uncertainty notes when requirements are still moving.
4. Do not hide assumptions; write them next to the estimate.

## Useful effort bands

| Work item | Typical band | Notes |
|---|---|---|
| Basic module configuration | 1-3 days | Standard setup, light business tuning |
| Simple field and view extension | 0.5-2 days | Small change, little workflow impact |
| New simple model | 2-5 days | CRUD, ACL, basic views |
| Complex workflow customization | 4-10 days | Multiple states, approvals, automation |
| Custom report | 1-5 days | Depends on layout and aggregation depth |
| External integration | 5-20+ days | Depends on API quality, sync direction, error handling |
| Data migration | 2-20+ days | Depends on volume, cleanliness, mapping, reconciliation |
| UAT, training, PM overhead | 15-30% | Add on top of build effort |

## Multipliers

Increase the range when one or more of these apply:

- unclear requirements
- new Odoo version or unstable upstream behavior
- domain the team rarely implements
- many companies, warehouses, currencies, or approvals
- strict documentation or procurement process

## Output template

```markdown
## Estimate Summary

| Area | Classification | Range | Assumptions |
|---|---|---|---|
```

