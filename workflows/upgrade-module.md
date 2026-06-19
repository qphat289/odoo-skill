# WORKFLOW: Upgrade Module

This workflow guides the AI agent through upgrading a module from a source Odoo version to a target Odoo version.

## Overview

```text
Source -> Target -> Calculate Path -> Load Migrations -> Transform -> Validate
```

---

## Step-by-Step Execution

### STEP 1: Determine Migration Path

Specify the upgrade hops necessary to reach the target Odoo version.

```python
source_version = "16.0"
target_version = "18.0"

migration_path = calculate_path(source_version, target_version)
# Result: ["16.0", "17.0", "18.0"]

hops = [
    ("16", "17"),  # attrs removal, create_multi required
    ("17", "18"),  # _check_company_auto, SQL() builder
]
```

### STEP 2: Load Migration Skills

Read migration-specific guides to prevent syntax issues.

```python
for source, target in hops:
    skills_to_load = [
        f"skills/odoo-development/references/odoo-module-generator-{source}-{target}.md",
        f"skills/odoo-development/references/odoo-model-patterns-{source}-{target}.md",
        f"skills/odoo-development/references/odoo-security-guide-{source}-{target}.md",
        f"skills/odoo-development/references/odoo-version-knowledge-{source}-{target}.md",
    ]

    if has_owl_components(module_path):
        skills_to_load.append(f"skills/odoo-development/references/odoo-owl-components-{source}-{target}.md")
```

### STEP 3: Apply Transformations

Apply regex or structural transformations to files.

```python
transformations = []

for source, target in hops:
    if (source, target) == ("16", "17"):
        transformations.extend([
            transform_create_to_create_multi,
            transform_attrs_to_inline,
        ])
    elif (source, target) == ("17", "18"):
        transformations.extend([
            add_check_company_auto,
            add_check_company_fields,
            transform_sql_to_builder,
            add_type_hints,
        ])

for transform in transformations:
    files = transform(module_files)
```

### STEP 4: Generate Migration Scripts

Set up Odoo pre/post migration SQL and data scripts.

```python
migration_files = {
    f"migrations/{target_version}.1.0.0/pre-migration.py": generate_pre_migration(),
    f"migrations/{target_version}.1.0.0/post-migration.py": generate_post_migration(),
}
```

### STEP 5: Output Upgraded Module

Verify modifications and output details.

```python
output = {
    "status": "success",
    "source_version": source_version,
    "target_version": target_version,
    "migration_path": migration_path,
    "updated_files": updated_files,
    "migration_scripts": migration_files,
    "breaking_changes": list_breaking_changes(hops),
    "manual_review_required": list_manual_items(),
}
```
