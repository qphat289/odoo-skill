# WORKFLOW: Presales Discovery

## Purpose

Guide the agent through early-stage requirement gathering before fit-gap, Functional Design, Solution Design, or Technical Design is ready.

## When to use

Use this workflow when the scope is still business-facing and the team needs structured discovery notes rather than design artifacts.

If the customer already provided a detailed Scope of Work, requirement document, module list, or function list, prefer `workflows/requirements-analysis.md` instead.

## Inputs

- customer context
- industry or business domain
- known systems, pain points, and constraints

## Required reads

- `skills/odoo-presales/SKILL.md`
- `skills/odoo-presales/references/discovery-questionnaire.md`

## Optional reads

- `skills/odoo-presales/references/requirement-analysis-guide.md` when discovery is already detailed enough to normalize requirements

## Steps

1. Read the presales skill and discovery questionnaire.
2. Collect:
   - company context
   - current systems
   - business flows
   - reporting and operational needs
   - integration or compliance constraints
3. Mark red flags early when they may affect cost or solution shape.
4. Produce either:
   - a discovery question set
   - or `Discovery Notes` when the answers already exist
5. Move to requirement analysis or fit-gap work when discovery is sufficiently complete.
6. Start Functional Design or Solution Design only when the required input is specific enough.

## Outputs

- discovery question set
- or `Discovery Notes`
- optional requirement inventory

## Validation gates

- business context is captured before technical solutioning
- red flags are visible, not buried in notes
- discovery output is clear enough to feed fit-gap analysis
