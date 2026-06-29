---
name: odoo-quality
description: Domain skill for Odoo QA/QC planning, test generation, test execution guidance, performance review, validation, and quality gates across Odoo 14-19.
---

# Odoo Quality

Use this skill when the task is about QA/QC planning, test generation, test execution guidance, performance review, verification before handoff, or quality gates after generation and refactoring.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| QA/QC planning | `references/test-plan-template.md` | Build a detailed `Test Plan.md` with coverage, statuses, traceability, and execution loop tracking |
| QA/QC example | `references/test-plan-example-sale-approval.md` | See a realistic end-to-end `Test Plan.md` example before drafting a new plan |
| Test patterns | `references/odoo-test-patterns.md` | Unit, integration, browser, and Odoo test design |
| Test tooling | `references/test-tooling-patterns.md` | `TransactionCase`, `Form`, `HttpCase`, patching, query counts |
| Test execution | `references/odoo-test-execution.md` | Running tests and interpreting results |
| Performance | `references/odoo-performance-guide.md` | N+1, batching, slow ORM, SQL review |
| Profiling | `references/odoo-profiling-guide.md` | Reproduce, measure, and inspect bottlenecks |
| PostgreSQL indexing | `references/postgresql-indexing-guide.md` | `EXPLAIN`, index selection, Odoo search and join tuning |
| Common bug prevention | `references/common-bug-patterns.md` | Prevent repeat mistakes before generation and catch them during review |

## Rules

1. Use this skill as the final pass before handoff on important tasks.
2. Use a dedicated `Test Plan.md` before writing or executing tests for non-trivial modules, integrations, or security-sensitive flows.
3. Treat `Test Plan.md` as the QA/QC source of truth for case coverage, defect/retest tracking, and execution evidence.
4. Preserve upstream requirement-analysis, fit-gap, design, and technical traceability when it materially improves QA/QC clarity.
5. Pair with `rules/security.md` and `rules/coding-style.md` for review outputs.
6. For bug clusters that repeat, promote them into a reusable rule or checklist.
7. When optimizing SQL-heavy flows, pair this skill with `odoo-models` so ORM and indexing advice stay aligned.
8. Use `references/common-bug-patterns.md` as the compact pre-build and review bug baseline.
9. If the final QA/QC deliverable must be exported to `.docx` or mapped from a spreadsheet source, keep QA/QC as the primary route and add document/spreadsheet capability only for the artifact-handling step.
