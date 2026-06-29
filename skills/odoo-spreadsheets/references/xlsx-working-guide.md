# XLSX Working Guide

Use this guide when the active Odoo task touches `.xlsx`, `.xls`, `.csv`, or `.tsv` files.

## Scope

Typical cases:

- analyze customer requirement workbooks
- normalize workbook rows into `Requirement Analysis.md`
- create or update `Fit-Gap Analysis.xlsx`
- preserve structured tracking imports or exports

## Core rule

Keep the original Odoo workflow as the primary route:

- requirements analysis or fit-gap for customer requirement workbooks
- project tracking for status-oriented structured sheets
- QA/QC route when spreadsheet input feeds testing scope

Use spreadsheet capability only for the workbook-handling step.

## Handling rules

1. Treat workbook content as source material, not automatically as truth.
2. Preserve sheet names, row references, and stable IDs when they matter downstream.
3. Do not flatten row-based requirements into vague prose too early.
4. Do not overwrite formulas, comments, hidden sheets, or formatting in customer-provided files unless required.
5. When building a fit-gap workbook, keep one requirement per row and keep IDs stable once shared.

## Output discipline

- `Requirement Analysis.md` is the normalized analysis artifact.
- `Fit-Gap Analysis.xlsx` is the structured fit-gap artifact by default.
- Narrow fit-gap answers may stay lighter-weight if the user did not ask for the workbook.

## Provenance rule

The `add-skill/skills/xlsx` package is a reference input only. Reuse ideas carefully, but do not vendor its proprietary contents into the native repo skill structure.
