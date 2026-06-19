# WORKFLOW: Generate Module

This workflow guides the AI agent through parsing requirements, loading the target Odoo version patterns, generating consistent module files, and validating the generated output.

## Overview

```text
Input -> Validate -> Load Skills -> Generate Files -> Verify -> Output
```

---

## Step-by-Step Execution

### STEP 1: Parse and Validate Input

Extract module specifications from the user request. Prompt for missing details if necessary.

```python
# REQUIRED: Extract these from user request
input_data = {
    "module_name": "",           # REQUIRED - lowercase, underscores only
    "module_description": "",    # REQUIRED - min 10 chars
    "odoo_version": "",          # REQUIRED - 14.0/15.0/16.0/17.0/18.0/19.0
}

# OPTIONAL: Apply defaults if not specified
defaults = {
    "target_apps": [],
    "ui_stack": "classic",       # classic/owl/hybrid
    "multi_company": False,
    "multi_currency": False,
    "security_level": "basic",   # basic/advanced/audit
    "performance_critical": False,
    "include_tests": True,
    "include_demo": False,
    "models": [],
    "inherit_models": [],
}

# ACTION: If odoo_version not specified, ask user directly
if not input_data.get("odoo_version"):
    # Ask: "Which Odoo version are you targeting?"
    # Options: ["18.0 (Recommended)", "17.0", "16.0", "15.0", "14.0", "19.0 (Development)"]
    pass
```

### STEP 2: Load Version-Specific Skills

Before writing code, read the required matching Odoo version skill files.

```python
version = input_data["odoo_version"].replace(".0", "")  # "18.0" -> "18"

required_skills = [
    f"skills/odoo-development/references/odoo-module-generator-{version}.md",
    f"skills/odoo-development/references/odoo-model-patterns-{version}.md",
    f"skills/odoo-development/references/odoo-security-guide-{version}.md",
]

if input_data.get("ui_stack") in ["owl", "hybrid"]:
    required_skills.append(f"skills/odoo-development/references/odoo-owl-components-{version}.md")

if input_data.get("performance_critical"):
    required_skills.append("skills/odoo-development/references/odoo-performance-guide.md")

if input_data.get("include_tests"):
    required_skills.append("skills/odoo-development/references/odoo-test-patterns.md")

for skill in required_skills:
    pass

shared_rules = [
    "rules/security.md",
    "rules/coding-style.md",
]
```

### STEP 3: Verify Patterns Against GitHub

When uncertain about specific Odoo core syntax, query the official Odoo GitHub repository.

```python
if version >= "17":
    # Verify @api.model_create_multi usage
    pass

if version >= "18":
    # Verify _check_company_auto pattern
    pass

# Verify view syntax (attrs vs invisible)
```

### STEP 4: Generate Module Files

Generate files in a strict dependency-safe order. This is critical for the `data` loading sequence in the module manifest.

```python
files_to_generate = {
    "__manifest__.py": generate_manifest(input_data),
    "__init__.py": generate_root_init(input_data),
    "models/__init__.py": generate_models_init(input_data),
    "security/{module}_security.xml": generate_security_groups(input_data),
    "security/ir.model.access.csv": generate_access_rights(input_data),
    "views/menuitems.xml": generate_menus(input_data),
}
```

### STEP 5: Validate Generated Code

Perform automated lint checks on the generated code before outputting.

```python
validations = {
    "manifest_data_order": check_data_file_order(manifest),
    "security_before_views": check_security_first(manifest),
    "python_syntax": check_python_syntax(python_files),
    "xml_syntax": check_xml_syntax(xml_files),
    "version_patterns": check_version_compliance(files, version),
}

for check, result in validations.items():
    if not result["valid"]:
        pass
```

### STEP 6: Output Results

Save code and structure. Output a summary to the user.

```python
output = {
    "status": "success",
    "module_name": input_data["module_name"],
    "odoo_version": input_data["odoo_version"],
    "files": files_to_generate,
    "file_tree": generate_file_tree(files_to_generate),
    "version_notes": collect_version_notes(version),
    "warnings": collect_warnings(),
    "github_verified": True,
    "manifest_data_order": [
        "security/{module}_security.xml",
        "security/ir.model.access.csv",
        "views/{model}_views.xml",
        "views/menuitems.xml",
    ],
}

for path, content in files_to_generate.items():
    full_path = f"{output_directory}/{input_data['module_name']}/{path}"
    pass
```
