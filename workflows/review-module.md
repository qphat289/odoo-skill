# WORKFLOW: Review Module

## Purpose

Guide the agent through structured review of an existing Odoo module for correctness, security, maintainability, and performance.

## When to use

Use this workflow for audits, code review, regression-risk checks, or static module quality assessment.

## Inputs

- module path
- target Odoo version
- optional review focus such as security, performance, or upgrade readiness
- optional `Project Tracking.md` when review status must be tracked

## Required reads

- `skills/odoo-models/references/odoo-model-patterns-{version}.md`
- `skills/odoo-security/references/odoo-security-guide-{version}.md`
- `skills/odoo-quality/references/odoo-performance-guide.md`
- `skills/odoo-quality/references/common-bug-patterns.md`
- `skills/odoo-models/references/advanced-orm-performance-patterns.md`
- `skills/odoo-upgrade/references/odoo-troubleshooting-guide.md`
- `skills/odoo-operations/references/logging-debugging-patterns.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- `skills/odoo-owl/references/odoo-owl-components-{version}.md`
- `skills/odoo-integrations/references/controller-api-patterns.md`
- `skills/odoo-integrations/references/api-version-notes-{version}.md`
- `skills/odoo-automation/references/cron-automation-patterns.md`
- `skills/odoo-module-generation/references/xml-data-loading-patterns.md`
- `skills/odoo-models/references/mixin-composition-patterns.md`
- `skills/odoo-models/references/decorator-decision-patterns.md`
- `skills/odoo-operations/references/transaction-safety-patterns.md`
- `skills/odoo-quality/references/postgresql-indexing-guide.md`
- `skills/odoo-quality/references/test-tooling-patterns.md`
- `agents/odoo-code-reviewer.md`

## Steps

1. Scan the module structure and identify manifest, Python, XML, CSV, JS, and test files.
2. Confirm the module version from the manifest or explicit user input.
3. Invoke `agents/odoo-code-reviewer.md` when a systematic full review is expected.
4. Load the required model, security, performance, troubleshooting, and rule references.
5. Load optional references only when the module content warrants them.
6. Review by area:
   - manifest and data ordering
   - models and ORM patterns
   - security and multi-company behavior
   - views and reports
   - automation, controllers, and frontend if present
   - performance traps and test coverage
7. When a bug matches a recurring pattern, name the pattern explicitly in the review notes.
8. If a repeat-worthy bug is not already covered in the canonical references, add it to `docs/CORRECTIONS_LOG.md` for later promotion.
9. Group findings by severity and provide actionable fixes.
10. If `Project Tracking.md` is in use, update only the affected review/status rows with evidence from the review.

## Suggested correction-log row

```markdown
| CB-CAND-001 | pending | YYYY-MM-DD | security | 17+ | skills/odoo-quality/references/common-bug-patterns.md | record rule over-restricts users | rule intersection blocks valid records for normal users | review all overlapping rules and company filters before shipping | review finding in module audit | promote if the same pattern appears again |
```

## Outputs

- critical findings
- warnings
- suggestions
- version-specific review notes

## Validation gates

- review criteria match the confirmed version
- security and multi-company issues are checked explicitly
- performance findings point to concrete patterns, not vague suspicion
- output is structured enough to drive fixes or follow-up review
