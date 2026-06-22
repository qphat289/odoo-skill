# WORKFLOW: Upgrade Module

## Purpose

Guide the agent through upgrading an Odoo module from one version to another with hop-aware analysis and transformation planning.

## When to use

Use this workflow for migration, version-hop refactoring, or upgrade impact analysis.

## Inputs

- module path
- source Odoo version
- target Odoo version

## Required reads

- `skills/odoo-upgrade/references/odoo-version-knowledge-{source}-{target}.md`
- `skills/odoo-module-generation/references/odoo-module-generator-{source}-{target}.md`
- `skills/odoo-models/references/odoo-model-patterns-{source}-{target}.md`
- `skills/odoo-security/references/odoo-security-guide-{source}-{target}.md`
- `rules/security.md`
- `rules/coding-style.md`

## Optional reads

- `skills/odoo-owl/references/odoo-owl-components-{source}-{target}.md`
- `skills/odoo-integrations/references/controller-api-patterns.md`
- `skills/odoo-automation/references/cron-automation-patterns.md`
- `skills/odoo-operations/references/config-settings-patterns.md`
- `agents/odoo-upgrade-analyzer.md`

## Steps

1. Confirm source and target versions.
2. Calculate the migration hops if the upgrade spans more than one major version.
3. Invoke `agents/odoo-upgrade-analyzer.md` when the migration is broad or risky.
4. Load the required cross-version references for each hop.
5. Load optional references only when the module uses frontend, controllers, automation, or operational features.
6. Identify required transformations for each hop.
7. Decide which changes are:
   - automatic
   - manual but straightforward
   - risky and requiring upstream verification
8. Generate migration notes and scripts when appropriate.
9. Validate the final module state against the target version.

## Outputs

- required upgrade fixes
- recommended cleanups
- migration-script notes
- manual verification list

## Validation gates

- every source-target hop is accounted for
- target-version syntax and semantics are checked explicitly
- risky assumptions are marked for verification, not presented as facts
- migration output separates mandatory fixes from optional cleanup

