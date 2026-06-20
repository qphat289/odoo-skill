# Workflow Orchestrator for AI Agents

Step-by-step orchestration for autonomous Odoo module operations.
Follow these workflows for complete end-to-end execution.

## Master workflow selector

Map request type to workflow:
- "Create module" -> `workflows/generate-module.md`
- "Review module" -> `workflows/review-module.md`
- "Upgrade module" -> `workflows/upgrade-module.md`
- "Add security" -> `workflows/generate-module.md`
- "Add tests" -> `workflows/generate-module.md`
- "Add OWL component" -> `workflows/generate-module.md`

When a user request is received, load the appropriate sub-workflow file:
- For module creation, scaffolding, adding features (views, models, security, OWL, tests), read and execute `workflows/generate-module.md`.
- For reviewing, auditing, and static analysis of Odoo code, read and execute `workflows/review-module.md`.
- For upgrading, migrating, or version-specific refactoring of Odoo modules, read and execute `workflows/upgrade-module.md`.

---

## Decision rule

Do not keep version syntax tables in this orchestrator. After version detection:

1. Load the matching version skill `skills/odoo-14.0/` through `skills/odoo-19.0/`.
2. Load the relevant workflow.
3. Load `skills/odoo-upgrade/references/odoo-version-routing.md`.
4. Load `skills/odoo-module-generation/references/odoo-manifest-data-order.md` when file ordering or XML references matter.
5. Load `rules/security.md` and `rules/coding-style.md`.
6. Load only the references needed for the task.

---

## Error Recovery

### Common Errors and Recovery Actions

| Error | Detection | Recovery |
|-------|-----------|----------|
| Version not specified | `odoo_version` missing | Ask user directly and stop until clarified |
| Invalid module name | Pattern mismatch | Suggest valid name |
| Missing security | No ir.model.access.csv | Generate basic access rights |
| Deprecated version pattern | Found rule violation from version skill or reference | Apply the fix from the matching version skill |

### Recovery Workflow

```python
def recover_from_error(error_type, context):
    recovery_actions = {
        "VERSION_MISSING": lambda: ask_user_version(),
        "INVALID_NAME": lambda: suggest_valid_name(context["name"]),
        "SECURITY_MISSING": lambda: generate_default_security(context),
        "DEPRECATED_PATTERN": lambda: apply_transformation(context),
    }

    if error_type in recovery_actions:
        return recovery_actions[error_type]()
    return {"status": "error", "message": "Unrecoverable error"}
```

---

## Orchestrator Checklist

### Before Starting Any Workflow

- [ ] Odoo version identified
- [ ] Input validated against schema
- [ ] Matching version skill loaded
- [ ] GitHub verification planned

### During Execution

- [ ] Each file generated in correct order
- [ ] Security files before views in manifest
- [ ] Version-specific references and shared rules applied
- [ ] No rule or version-skill violations remain

### Before Output

- [ ] All files syntax-validated
- [ ] Manifest data order verified
- [ ] Version notes collected
- [ ] Warnings documented

---

## Example Complete Execution

```text
USER: "Create a sales approval module for Odoo 18"

AGENT WORKFLOW:
1. Parse: module_name="sale_approval", odoo_version="18.0"
2. Load: `skills/odoo-18.0/SKILL.md`, then the referenced module/model/security files
3. Verify: WebFetch sale_order.py for v18 patterns
4. Generate:
   - __manifest__.py (with data order)
   - __init__.py
   - models/__init__.py
   - models/sale_approval.py (_check_company_auto, @api.model_create_multi)
   - security/sale_approval_security.xml (groups)
   - security/ir.model.access.csv (access rights)
   - views/sale_approval_views.xml (invisible expressions)
   - views/menuitems.xml
   - tests/__init__.py
   - tests/test_sale_approval.py
5. Validate: All checks pass
6. Output: Complete module with file tree and version notes
```

