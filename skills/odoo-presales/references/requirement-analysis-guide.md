# Odoo Requirement Analysis Guide

Use this reference when the customer already provides a detailed Scope of Work, requirements document, module list, function list, spreadsheet, or meeting package.

Suggested artifact: `Requirement Analysis.md`

Default format rule:

- Use `.md` as the primary artifact for requirement analysis unless the user explicitly requests another format.
- Keep source-heavy, row-structured customer material traceable enough that it can be transferred into `Fit-Gap Analysis.xlsx` cleanly.
- Use `Clarification Register.xlsx` as the default place to capture clarification questions and answers.

## Goal

Turn customer-provided requirements into a clean analysis baseline without inventing new scope.

## Core rule

Do not suggest extra modules, features, flows, reports, or integrations unless the user explicitly asks for recommendations. Verify only the missing or inconsistent information that materially affects fit-gap, functional design, solution design, technical design, estimation, risk, or acceptance.

Clarification rule:

- ask only high-value, directly relevant questions
- do not ask side-track or low-impact questions
- capture clarification rows in `Clarification Register.xlsx`
- resolve blocking clarifications before treating the analysis baseline as ready for fit-gap

## Required input handling

1. Preserve the customer's requirement IDs, module names, function names, and wording when possible.
2. Split compound requirements only when one row contains multiple decisions or deliverables.
3. Normalize terminology without changing scope.
4. Mark missing information as `Need confirmation`, not as an assumed solution.
5. Keep phase-2/backlog ideas separate from confirmed scope.

## Clarification filter

### Blocking clarifications

Ask before finalizing fit-gap or downstream design when the answer would change:

- fit vs configuration vs customization vs integration
- in-scope vs out-of-scope vs later phase
- core business rule or approval rule
- solution direction
- estimate or major risk
- acceptance baseline

### Deferred minor questions

Do not stop the flow for questions that add little value right now, such as:

- wording polish
- low-impact display preferences
- small owner or formatting details
- details that can be refined later without changing the current classification

## Analysis output

```markdown
# Requirement Analysis

## Source Files

| File | Type | Notes |
|---|---|---|

## Requirement Inventory

| Req ID | Module / Area | Customer Requirement | Source | Priority | Status | Notes |
|---|---|---|---|---|---|---|

## Clarification Register Status

- Clarification artifact: `Clarification Register.xlsx`
- Blocking clarification status:
- Minor clarification status:
- Ready for fit-gap:

## Scope Boundaries

### In Scope

### Out Of Scope

### Phase Later / Backlog Candidates

## Next-Step Recommendation

- Recommended next workflow:
- Clarification readiness note:
```

## Blocking clarification examples

- approval threshold source or owner
- exact report layout, filters, and grouping
- field calculation formula
- integration direction, frequency, API owner, and failure handling
- migration volume, source format, and data cleansing owner
- user groups and approval responsibility
- legal, accounting, or compliance constraint

## Minor clarification examples

- final wording preference for an email subject
- non-critical field label preference
- preferred owner name for a later review cycle

## Validation gates

- no new scope is introduced
- every clarification row explains why the answer is needed
- low-value questions are filtered out
- customer-provided module/function structure remains traceable
- output is ready for fit-gap analysis
