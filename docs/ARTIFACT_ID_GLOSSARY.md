# Artifact ID Glossary

Use this glossary when reading or generating presales, design, technical, QA/QC, and tracking artifacts in this repository.

The goal is to keep IDs stable, readable, and traceable across the full delivery loop.

## Canonical ID families

| Prefix | Meaning | Main artifact | Example |
|---|---|---|---|
| `RQ-xxx` | normalized requirement row ID | `Requirement Analysis.md` | `RQ-003` |
| `CL-xxx` | clarification row ID | `Clarification Register.xlsx` | `CL-001` |
| `FG-xxx` | fit-gap row ID | `Fit-Gap Analysis.xlsx` | `FG-007` |
| `FR-xxx` | functional requirement ID | `Functional Design.docx` | `FR-002` |
| `SD-CF-xx` | confirmed-input / applied-assumption row in Solution Design | `Solution Design.docx` | `SD-CF-01` |
| `TD-x.x` | technical design section reference | `Technical Design.md` | `TD-6.2` |
| `TP-xxx` | test case ID | `Test Plan.md` | `TP-011` |
| `T-xxx` | delivery task ID | `Project Tracking.md` | `T-016` |
| `B-xxx` | blocker ID | `Project Tracking.md` | `B-002` |
| `D-xxx` | decision ID | `Project Tracking.md` or business-facing tracking notes | `D-001` |
| `R-xxx` | risk ID | `Test Plan.md` or technical/QA notes | `R-001` |

## Supporting ID families

| Prefix | Meaning | Example | Note |
|---|---|---|---|
| `G-xxx` | grouped requirement cluster | `G-002` | used when multiple `RQ` rows belong to one business group |
| `FD-x.x` | Functional Design section reference | `FD-3.1` | points to a section, not a row |
| `SD-x.x` | Solution Design section reference | `SD-4.2` | points to a section, not a row |

## Legacy or summary shorthand

Some older examples may use summary labels such as `GAP01`, `GAP02`, or `GAP03`.

Use them only as a business-facing summary shorthand when one label represents a grouped fit-gap theme.
For new row-level traceability, prefer `FG-xxx`.

Some older material may also use customer-style requirement labels such as `REQ-SALES-01`.
For repository-owned normalized artifacts, prefer `RQ-xxx`.
If the customer already has their own ID scheme, keep it in a separate source-reference column instead of replacing `RQ-xxx`.

## Usage rules

1. Keep one stable ID family per artifact instead of inventing a new code each time.
2. Prefer repository-owned canonical IDs for downstream traceability.
3. Keep customer-provided IDs visible as source references when they already exist.
4. Reuse existing IDs when updating an artifact; do not renumber unless the artifact is being rebuilt from scratch.
5. Use grouped IDs such as `G-xxx` or summary labels such as `GAP01` only when the artifact is summarizing multiple detailed rows.

## Recommended reading order

`RQ` -> `CL` -> `FG` -> `FR` / `SD` -> `TD` -> `TP` -> `T`
