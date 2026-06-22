# WORKFLOW: Security Module

## Purpose

Guide the agent through generation or audit of Odoo security configuration with explicit ACL, record-rule, and company-scope checks.

## When to use

Use this workflow when the task is primarily about permissions, groups, rules, or security posture rather than full module generation or review.

## Inputs

- target Odoo version
- task mode: generate or audit
- module path or model scope
- multi-company requirement if relevant

## Required reads

- `skills/odoo-security/SKILL.md`
- `skills/odoo-security/references/odoo-security-guide-{version}.md`
- `rules/security.md`

## Optional reads

- `skills/odoo-models/SKILL.md`
- `skills/odoo-operations/references/transaction-safety-patterns.md`

## Steps

1. Confirm the target version and task mode.
2. Load the version-specific security guide and shared security rules.
3. Load optional model or transaction-safety references when access logic touches model design or raw SQL.
4. For generate mode:
   - define groups
   - define ACLs
   - define record rules only where needed
   - define field-level restrictions if required
5. For audit mode:
   - scan ACLs, rules, and security-sensitive code paths
   - check for company leakage, unsafe `sudo()`, and permission gaps
6. Report or generate the minimum needed security artifacts.

## Outputs

- security design
- or structured audit findings with fixes

## Validation gates

- every persistent model has explicit ACL
- record rules are necessary and least-privilege
- multi-company behavior is checked where relevant
- no privileged bypass is left unexplained

