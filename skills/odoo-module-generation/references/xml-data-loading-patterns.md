# Odoo XML and CSV Data Loading Patterns

Use this file when authoring or reviewing `data/`, `demo/`, `security/`, or `views/` files and when the question is about `record`, `ref`, `eval`, `noupdate`, or CSV references.

## Version guardrails

- XML data loading semantics are mostly stable across Odoo 14-19.
- The main version-sensitive area here is x2many command style:
  - Odoo 14-15: legacy tuple syntax is still common.
  - Odoo 16+: `Command` syntax should be preferred in new code.
- View visibility syntax is not covered by this file; use the active version skill plus view references for `attrs` versus direct attributes.

## Structure baseline

```xml
<?xml version="1.0" encoding="UTF-8"?>
<odoo>
    <record id="my_record" model="my.model">
        <field name="name">Demo</field>
    </record>

    <data noupdate="1">
        <record id="my_default_config" model="my.model">
            <field name="name">Install once</field>
        </record>
    </data>
</odoo>
```

Rules:
- Operations run top to bottom.
- A record can only reference records loaded earlier.
- Put install-once records inside `noupdate="1"` when users may edit them later.

## External ID rules

- Same module: `ref="my_record"`
- Cross module: `ref="base.user_admin"`
- Keep IDs stable once released.
- Prefer explicit XML IDs for every reusable record.

## `record` and `field` patterns

### Plain values

```xml
<record id="my_sequence" model="ir.sequence">
    <field name="name">My Sequence</field>
    <field name="code">my.model</field>
    <field name="padding" eval="5"/>
</record>
```

### `ref`

```xml
<record id="my_partner_link" model="my.model">
    <field name="partner_id" ref="base.res_partner_1"/>
</record>
```

### `eval` with `Command`

```xml
<record id="my_rule" model="my.model">
    <field name="tag_ids" eval="[Command.set([ref('my_tag_a'), ref('my_tag_b')])]"/>
</record>
```

### HTML/XML content

```xml
<record id="mail_template_demo" model="mail.template">
    <field name="body_html" type="html">
        <div>
            <p>Hello</p>
        </div>
    </field>
</record>
```

### Binary file

```xml
<record id="attachment_logo" model="ir.attachment">
    <field name="name">Logo</field>
    <field name="datas" type="base64" file="my_module/static/description/icon.png"/>
</record>
```

## `noupdate` guidance

Use `noupdate="1"` for:
- default configuration users may change
- scheduled actions users may tune
- demo seed data
- sequences or starter records meant to be edited after install

Do not use `noupdate="1"` for:
- views
- access rights
- record rules
- actions and menus that should stay aligned with code

## XML shortcuts worth preferring

### Menu

```xml
<menuitem id="menu_my_root" name="My App" sequence="10"/>
<menuitem id="menu_my_records" name="Records" parent="menu_my_root" action="action_my_model"/>
```

### Template

```xml
<template id="my_template" name="My Template">
    <div class="container">
        <h1>Hello</h1>
    </div>
</template>
```

Use shortcut tags when they are clearer than raw `record` syntax.

## CSV patterns

### Access rights

```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_my_model_user,my.model.user,my_module.model_my_model,base.group_user,1,1,1,0
```

### Related records with `:id`

```csv
id,country_id:id,name,code
state_demo,base.us,Demo State,DS
```

Rules:
- Use CSV for flat bulk data.
- Use XML when you need `eval`, nested structure, HTML, or complex relationships.

Version note:
- CSV semantics stay stable; the bigger cross-version risks usually come from what those records reference, not from CSV itself.

## `delete` and `function`

### Delete obsolete data

```xml
<delete model="ir.ui.menu" id="my_module.menu_legacy"/>
```

### Call a setup helper

```xml
<function model="my.model" name="post_init_seed_defaults"/>
```

Rules:
- Avoid heavy or opaque logic in XML `function` calls.
- Prefer hooks or explicit migration scripts for bigger upgrade actions.

## Ordering checklist

1. Security groups before access CSV or menu restrictions.
2. Base records before inherited or dependent records.
3. Views before actions that target specific view IDs when needed.
4. Actions before menus that reference them.
5. Reports after the templates they depend on.

## Common mistakes

- Menu references an action loaded later.
- `noupdate="1"` wrapped around records that should keep tracking code changes.
- CSV access file references a group XML ID not loaded yet.
- XML record tries to `ref` something declared lower in the same file.
- Many2many XML still uses legacy tuple syntax even though `Command` is clearer in modern code.
