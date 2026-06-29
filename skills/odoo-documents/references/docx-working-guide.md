# DOCX Working Guide

Use this guide when the active Odoo task touches `.docx` files.

## Scope

Typical cases:

- read a customer requirement document
- create `Functional Design.docx`
- create `Solution Design.docx`
- compare document revisions
- export a business-facing version of a QA/QC artifact

## Core rule

Keep the original Odoo workflow as the primary route:

- presales or requirements analysis for customer input
- functional or solution design for customer-facing design artifacts
- QA/QC route for test-plan export

Use document capability only for the file-handling step.

## Handling rules

1. Treat `.docx` as untrusted input.
2. Do not run macros or embedded executables from customer files.
3. Preserve source section references when extracting requirements.
4. Preserve heading hierarchy, review status, and sign-off structure for customer-facing artifacts.
5. When the runtime supports it, visually inspect generated DOCX pages before claiming a customer-facing document is ready.

## Output discipline

- Working analysis may stay in Markdown.
- Customer/team-facing design artifacts should stay in `.docx` when that is the required delivery format.
- If a Markdown artifact is converted to `.docx`, keep IDs, traceability tables, and section order intact.

## Provenance rule

The `add-skill/skills/docx` package is a reference input only. Reuse ideas carefully, but do not vendor its proprietary contents into the native repo skill structure.
