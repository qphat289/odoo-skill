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
    f"skills/odoo-development/references/odoo-model-patterns-{version}.md",
    f"skills/odoo-development/references/odoo-security-guide-{version}.md",
    "skills/odoo-development/references/odoo-performance-guide.md",
    "skills/odoo-development/references/odoo-troubleshooting-guide.md",
    "rules/security.md",
    "rules/coding-style.md",
]
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
