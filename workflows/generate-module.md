# WORKFLOW: Generate Module

## Purpose

Guide the agent through generating a new Odoo module or a substantial new feature set with version-correct structure and validation.

## When to use

Use this workflow for scaffolding a module, adding a major feature, or generating a clean implementation baseline from requirements.

Prefer `workflows/technical-design.md` first when Functional Design and Solution Design exist but `Technical Design.md` has not been produced yet.

## Inputs

- module name
- module description
- optional `Technical Design.md`
- optional `Test Plan.md`
- optional `Project Tracking.md`
- target Odoo version
- target apps or business area
- UI stack if relevant
- security level
- whether tests, automation, integrations, or OWL are needed

## Required reads

- `skills/odoo-module-generation/references/odoo-module-generator-{version}.md`
- `skills/odoo-module-generation/references/xml-data-loading-patterns.md`
- `skills/odoo-models/references/odoo-model-patterns-{version}.md`
- `skills/odoo-security/references/odoo-security-guide-{version}.md`
- `skills/odoo-quality/references/common-bug-patterns.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- `skills/odoo-owl/references/odoo-owl-components-{version}.md`
- `skills/odoo-integrations/references/controller-api-patterns.md`
- `skills/odoo-integrations/references/import-export-patterns.md`
- `skills/odoo-integrations/references/api-version-notes-{version}.md`
- `skills/odoo-automation/references/cron-automation-patterns.md`
- `skills/odoo-automation/references/mail-notification-patterns.md`
- `skills/odoo-models/references/mixin-composition-patterns.md`
- `skills/odoo-business-domains/references/sale-crm-patterns.md`
- `skills/odoo-operations/references/config-settings-patterns.md`
- `skills/odoo-operations/references/input-validation-schema.md`
- `skills/odoo-operations/references/transaction-safety-patterns.md`
- `skills/odoo-quality/references/odoo-performance-guide.md`
- `skills/odoo-models/references/advanced-orm-performance-patterns.md`
- `skills/odoo-quality/references/odoo-test-patterns.md`
- `skills/odoo-quality/references/test-tooling-patterns.md`
- `agents/odoo-context-gatherer.md`

## Steps

1. Validate the required inputs.
2. If the version is missing, stop and confirm it.
3. Invoke `agents/odoo-context-gatherer.md` before generating code when surrounding project context matters.
4. Load the required version-specific module, model, security, and common bug references.
5. Translate relevant common bug patterns into a short pre-build checklist for this module.
6. Load only the optional domain references that match the requested feature set.
7. If `Test Plan.md` exists, implement against the approved scope and keep the affected case IDs visible for later execution and status updates.
8. Generate the module structure in dependency-safe order:
   - manifest and package init
   - models
   - security
   - views and menus
   - assets or OWL components if needed
   - tests if included
9. Verify uncertain syntax against official Odoo sources when the version or pattern is sensitive.
10. Validate manifest ordering, syntax, security baseline, version compliance, and common bug avoidance.
11. If the request is part of the full delivery loop, hand off to `workflows/generate-tests.md`, `workflows/test-module.md`, or direct fix/retest work as appropriate.
12. If `Project Tracking.md` is in use, update only the affected task rows with evidence-based status changes.

## Outputs

- generated module file tree
- version-sensitive implementation notes
- validation summary

## Validation gates

- module name is valid and version is confirmed
- security files load before views and menus
- generated patterns match the target version
- every persistent model has ACL coverage
- relevant repeat-bug checks were applied before file generation
- non-trivial logic has at least a test recommendation, or tests are generated when requested
