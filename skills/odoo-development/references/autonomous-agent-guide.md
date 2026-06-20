# Autonomous Agent Guide for Odoo Development

Use this guide when an agent needs to operate with minimal supervision across spec, generation, review, and upgrade work.

## Core principles

1. Detect the target Odoo version first.
2. Load only the smallest relevant skill set for the task.
3. Do not mix version-specific patterns.
4. Treat manifest ordering, security, and multi-company rules as first-class concerns.
5. Verify uncertain syntax or major-version claims against official docs or source.

## Input schema

```json
{
  "module_name": "string",
  "module_description": "string",
  "odoo_version": "14.0|15.0|16.0|17.0|18.0|19.0",
  "target_apps": ["sale", "stock"],
  "ui_stack": "classic|owl|hybrid",
  "multi_company": true,
  "security_level": "basic|advanced|audit",
  "performance_critical": false,
  "include_tests": true
}
```

## Workflow: generate

1. Parse inputs and confirm or detect the target version.
2. Load:
   - `odoo-module-generator-{version}.md`
   - `odoo-model-patterns-{version}.md`
   - `odoo-security-guide-{version}.md`
   - `odoo-owl-components-{version}.md` when frontend work exists
3. Build the module skeleton with correct manifest order.
4. Add models, security, views, data, and tests.
5. Validate version-sensitive rules before finishing.

## Workflow: review

1. Detect the version from `__manifest__.py` and code patterns.
2. Load the matching model/security references.
3. Scan for version-incorrect patterns.
4. Review security, manifest order, and test gaps.
5. Report findings by severity.

## Workflow: upgrade

1. Identify source and target versions.
2. Load the matching hop references.
3. Convert deprecated APIs one hop at a time.
4. Verify each high-risk claim against upstream sources.
5. Re-test manifest loading, security flows, and frontend behavior.

## High-risk version checks

### v17+
- no `attrs` or `states` in XML views
- `@api.model_create_multi` expected in normal create flows

### v18+
- `_check_company_auto` and `check_company=True` where company-aware logic applies
- `SQL()` preferred for new raw SQL

### v19
- prefer `models.Constraint(...)` over `_sql_constraints`
- prefer type hints in maintained code
- prefer `SQL()` in new or risky raw SQL
- verify frontend/runtime claims against the current upstream branch before enforcing them as rules

## Output expectations

- keep output structured and version-aware
- explain any assumption that was not directly confirmed
- surface "verified" vs "preferred" vs "check upstream" when a rule is not absolute
