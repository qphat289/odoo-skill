# WORKFLOW: Test Module

## Purpose

Guide the agent through executing, debugging, and summarizing Odoo tests.

## When to use

Use this workflow for running tests, checking failures, or interpreting test logs and outcomes.

## Inputs

- module name
- target database
- optional test tag, class, or scope

## Required reads

- `skills/odoo-quality/SKILL.md`
- `skills/odoo-quality/references/odoo-test-execution.md`

## Optional reads

- `skills/odoo-quality/references/test-tooling-patterns.md`
- `agents/odoo-tester.md`

## Steps

1. Confirm module name, database, and optional tag or class filter.
2. Load the test-execution reference.
3. Load test-tooling guidance when failures need debugging or fixture interpretation.
4. Invoke `agents/odoo-tester.md` for actual execution and log parsing.
5. Summarize the run:
   - passes
   - failures
   - key traceback
   - likely cause
   - next fix to try

## Outputs

- structured test run summary
- prioritized failure analysis

## Validation gates

- module and database are correctly identified
- log interpretation is based on the actual failing trace, not guesswork
- next steps are specific enough to drive a fix

