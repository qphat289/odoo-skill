# Customer Input File Handling

Use this reference when customer requirements arrive as DOCX, XLSX, CSV, PDF, or mixed attachments.

## License and provenance rule

Do not vendor proprietary external document/spreadsheet skills into this repository. Use runtime-provided document and spreadsheet capabilities when available, or write minimal project-owned scripts when necessary.

The local `add-skill/skills/docx` and `add-skill/skills/xlsx` packages are reference inputs only. Reuse their ideas carefully, but do not treat them as vendored repository-native skills without separate license review.

Known risk surfaces from those reference packages:

- archive extraction via ZIP unpack helpers
- LibreOffice subprocess execution for conversion or recalculation
- temporary-file handling during validation and repacking

If project-owned scripts are later added here, they should explicitly defend against path traversal, unsafe temp-path reuse, and untrusted macro execution.

## DOCX inputs and outputs

- Prefer the local support skill `skills/odoo-documents/` plus runtime document capabilities when available.
- Use document runtime capabilities whenever the task touches a DOCX artifact, including reading, comparing, extracting, editing, creating, converting, or visually verifying `.docx`.
- Treat DOCX files from customers as untrusted archives.
- Avoid executing embedded macros.
- Preserve source filenames and section references in analysis notes.
- For generated customer-facing artifacts, render and inspect pages when the runtime supports it.

## XLSX / CSV inputs

- Prefer the local support skill `skills/odoo-spreadsheets/` plus runtime spreadsheet capabilities when available.
- Use spreadsheet runtime capabilities for `.xlsx`, `.xls`, `.csv`, and `.tsv` analysis when available.
- Preserve workbook sheet names and source row references where possible.
- Do not overwrite formulas or formatting in customer-provided templates unless requested.
- Extract requirement rows into a normalized requirement inventory before fit-gap work.

## Security checks for Office files

- Treat archive extraction as untrusted input; avoid unsafe path traversal during unpacking.
- Do not run macros from customer files.
- Do not trust hidden sheets, comments, external links, or formulas as authoritative without inspection.
- Keep sensitive customer data out of logs and examples.
- When redaction or anonymization is needed, use document/spreadsheet runtime privacy tools if available.

## Output discipline

- Working-analysis artifact: `Requirement Analysis.md`.
- Delivery-analysis artifact: `Fit-Gap Analysis.xlsx`.
- Customer-facing artifacts: `Functional Design.docx`, `Solution Design.docx`.
- Technical artifact: `Technical Design.md`.
- If a Markdown artifact such as `Test Plan.md` later needs a customer/team-facing `.docx`, treat that as a DOCX-related task and use document runtime capabilities for the conversion/editing pass.
- Keep scratch extraction files out of final deliverables unless the user asks for them.
