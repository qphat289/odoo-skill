---
name: odoo-spreadsheets
description: Support skill for Odoo work that touches `.xlsx`, `.xls`, `.csv`, or `.tsv` artifacts such as customer requirement workbooks, fit-gap analysis, or structured tracking inputs.
---

# Odoo Spreadsheets

Use this skill when an Odoo task touches workbook or tabular-file artifacts.

This skill supports the primary workflow; it does not replace presales, QA/QC, or tracking routing.

## Quick reference

| Topic | File | When to use |
|---|---|---|
| Spreadsheet handling rules | `references/xlsx-working-guide.md` | Read, normalize, analyze, or build workbook-based Odoo artifacts |

## Rules

1. Keep the real presales, QA/QC, or tracking workflow as the primary route.
2. Use this skill only for the workbook or row-structured part of the task.
3. Preserve sheet names, row references, and stable IDs where they materially affect traceability.
4. Do not overwrite customer formulas or formatting unless the task explicitly requires it.
5. Do not vendor proprietary third-party skill files into this repository.
