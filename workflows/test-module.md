# WORKFLOW: Test Module

## Purpose

Guide the agent through executing, debugging, retesting, and summarizing Odoo tests.

## When to use

Use this workflow for running tests, checking failures, retesting fixes, or interpreting test logs and outcomes.

## Inputs

- module name
- target database
- optional test tag, class, or scope
- optional `Test Plan.md`
- optional `Project Tracking.md` when test status must be tracked

## Required reads

- `skills/odoo-quality/SKILL.md`
- `skills/odoo-quality/references/odoo-test-execution.md`

## Optional reads

- `skills/odoo-quality/references/test-tooling-patterns.md`
- `agents/odoo-tester.md`

## Steps

1. Confirm module name, database, optional tag or class filter, and relevant Test Plan case IDs when available.
2. Load the test-execution reference.
3. Load test-tooling guidance when failures need debugging or fixture interpretation.
4. Invoke `agents/odoo-tester.md` for actual execution and log parsing.
5. Summarize the run:
   - passes
   - failures
   - key traceback
   - likely cause
   - next fix to try
6. If failures or missing behavior are found, feed them back into the implementation/debug step and mark the affected cases/tasks for fix and retest.
7. If `Test Plan.md` or `Project Tracking.md` is in use, update only the affected rows with evidence from the run.

## Outputs

- structured test run summary
- prioritized failure analysis
- updated Test Plan / Project Tracking status notes when those artifacts are in scope

## Validation gates

- module and database are correctly identified
- log interpretation is based on the actual failing trace, not guesswork
- next steps are specific enough to drive a fix

