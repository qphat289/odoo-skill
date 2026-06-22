# WORKFLOW: Generate Tests

## Purpose

Guide the agent through creating new Odoo tests that match the target version and the actual feature behavior.

## When to use

Use this workflow when writing new unit, integration, or security tests rather than executing them.

## Inputs

- target Odoo version
- module or feature path
- test type: unit, integration, or security

## Required reads

- `skills/odoo-quality/SKILL.md`
- `skills/odoo-quality/references/odoo-test-patterns.md`
- `skills/odoo-quality/references/test-tooling-patterns.md`

## Optional reads

- matching domain skill for the feature under test

## Steps

1. Confirm version, scope, and target test type.
2. Scan the module or feature to identify models, workflows, and security-sensitive behavior.
3. Load the required test references.
4. Load the matching domain skill if the business logic is specialized.
5. Generate the smallest useful test set:
   - setup fixtures
   - happy path
   - edge cases
   - access checks where relevant
6. Make sure the generated tests match the real model names, groups, and workflows.

## Outputs

- test file skeletons or complete test cases
- coverage notes
- missing-case reminders

## Validation gates

- tests reflect the confirmed target version
- tests use real model and group names from the implementation
- business and security logic both receive coverage when relevant

