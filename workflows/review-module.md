# WORKFLOW: Review Module

This workflow guides the AI agent through scanning an existing Odoo module, checking for standard patterns, and identifying security, design, or version compliance issues.

## Overview

```text
Path -> Scan Files -> Load Skills -> Analyze -> Report Issues
```

---

## Step-by-Step Execution

### STEP 1: Scan Module Structure

Locate and catalog all Python, XML, CSV, and JavaScript assets in the module path.

```python
module_files = {
    "manifest": glob(f"{module_path}/__manifest__.py"),
    "python": glob(f"{module_path}/**/*.py"),
    "xml": glob(f"{module_path}/**/*.xml"),
    "csv": glob(f"{module_path}/**/*.csv"),
    "js": glob(f"{module_path}/static/**/*.js"),
}

manifest_content = read(f"{module_path}/__manifest__.py")
```

### STEP 2: Load Review Skills

Read guidelines matching the module's target Odoo version.

```python
skills_to_load = [
    f"skills/odoo-models/references/odoo-model-patterns-{version}.md",
    f"skills/odoo-security/references/odoo-security-guide-{version}.md",
    "skills/odoo-quality/references/odoo-performance-guide.md",
    "skills/odoo-upgrade/references/odoo-troubleshooting-guide.md",
    "skills/odoo-operations/references/logging-debugging-patterns.md",
    "rules/security.md",
    "rules/coding-style.md",
]

if module_files["js"]:
    skills_to_load.append(f"skills/odoo-owl/references/odoo-owl-components-{version}.md")

if any("controllers" in path or "static" in path for path in module_files["python"] + module_files["xml"] + module_files["js"]):
    skills_to_load.append("skills/odoo-integrations/references/controller-api-patterns.md")
    if version in ["17", "18", "19"]:
        skills_to_load.append(f"skills/odoo-integrations/references/api-version-notes-{version}.md")

if any("data" in path or "cron" in path for path in module_files["xml"]):
    skills_to_load.extend([
        "skills/odoo-automation/references/cron-automation-patterns.md",
        "skills/odoo-module-generation/references/xml-data-loading-patterns.md",
    ])

if any("mail.thread" in read(py) or "mail.activity.mixin" in read(py) or "portal.mixin" in read(py) or "rating.mixin" in read(py) for py in module_files["python"]):
    skills_to_load.append("skills/odoo-models/references/mixin-composition-patterns.md")

if any("@api.model_create_multi" in read(py) or "@api.onchange" in read(py) or "@api.constrains" in read(py) or "@api.ondelete" in read(py) for py in module_files["python"]):
    skills_to_load.append("skills/odoo-models/references/decorator-decision-patterns.md")

if any("savepoint" in read(py) or "cr.execute" in read(py) or "commit(" in read(py) or "rollback(" in read(py) for py in module_files["python"]):
    skills_to_load.append("skills/odoo-operations/references/transaction-safety-patterns.md")

if any("TransactionCase" in read(py) or "HttpCase" in read(py) or "Form(" in read(py) or "assertQueryCount" in read(py) for py in module_files["python"]):
    skills_to_load.append("skills/odoo-quality/references/test-tooling-patterns.md")
```

### STEP 3: Analyze Each Area

Evaluate code quality, performance traps, security holes, and deprecated patterns.

```python
issues = []

for csv_file in module_files["csv"]:
    issues.extend(check_access_rights(csv_file, version))

for xml_file in module_files["xml"]:
    if "security" in xml_file:
        issues.extend(check_record_rules(xml_file, version))

for py_file in module_files["python"]:
    if "models" in py_file:
        issues.extend(check_model_patterns(py_file, version))
        issues.extend(check_deprecated_patterns(py_file, version))

for xml_file in module_files["xml"]:
    if "views" in xml_file:
        issues.extend(check_view_patterns(xml_file, version))

issues.extend(check_performance_patterns(module_files["python"]))
```

### STEP 4: Generate Report

Compile structural analysis findings into a clean issue log.

```python
report = {
    "status": "success",
    "module_path": module_path,
    "odoo_version": version,
    "summary": {
        "total_issues": len(issues),
        "critical": len([i for i in issues if i["severity"] == "critical"]),
        "warnings": len([i for i in issues if i["severity"] == "warning"]),
        "suggestions": len([i for i in issues if i["severity"] == "suggestion"]),
    },
    "issues": issues,
    "recommendations": generate_recommendations(issues),
}
```

