---
name: odoo-quality
description: Domain skill for Odoo testing, performance review, validation, and quality gates across Odoo 14-19.
---

# Odoo Quality

Use this skill when the task is about testing, performance review, verification before handoff, or quality gates after generation and refactoring.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Test patterns | `references/odoo-test-patterns.md` | Unit, integration, browser, and Odoo test design |
| Test tooling | `references/test-tooling-patterns.md` | `TransactionCase`, `Form`, `HttpCase`, patching, query counts |
| Test execution | `references/odoo-test-execution.md` | Running tests and interpreting results |
| Performance | `references/odoo-performance-guide.md` | N+1, batching, slow ORM, SQL review |
| Profiling | `references/odoo-profiling-guide.md` | Reproduce, measure, and inspect bottlenecks |
| PostgreSQL indexing | `references/postgresql-indexing-guide.md` | `EXPLAIN`, index selection, Odoo search and join tuning |
| Common bug prevention | `references/common-bug-patterns.md` | Prevent repeat mistakes before generation and catch them during review |

## Rules

1. Use this skill as the final pass before handoff on important tasks.
2. Pair with `rules/security.md` and `rules/coding-style.md` for review outputs.
3. For bug clusters that repeat, promote them into a reusable rule or checklist.
4. When optimizing SQL-heavy flows, pair this skill with `odoo-models` so ORM and indexing advice stay aligned.
5. Use `references/common-bug-patterns.md` as the compact pre-build and review bug baseline.
