# XML View Patterns Reference

Reference for Odoo view definitions with emphasis on version-sensitive visibility syntax.

## View types

| View Type | Purpose | Element |
|-----------|---------|---------|
| Form | Single-record editing | `<form>` |
| Tree/List | Multiple-record display | `<tree>` or `<list>` |
| Kanban | Card-based workflow view | `<kanban>` |
| Search | Filtering and grouping | `<search>` |
| Graph | Charts and analytics | `<graph>` |
| Pivot | Pivot tables | `<pivot>` |
| Calendar | Date-based display | `<calendar>` |
| Gantt | Timeline view | `<gantt>` |

## Form view

### Basic structure

```xml
<record id="my_model_view_form" model="ir.ui.view">
    <field name="name">my.model.form</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <form string="My Model">
            <header>
                <!-- Status bar and buttons -->
            </header>
            <sheet>
                <!-- Main content -->
            </sheet>
            <div class="oe_chatter">
                <!-- Mail integration -->
            </div>
        </form>
    </field>
</record>
```

### Example form view

```xml
<record id="my_model_view_form" model="ir.ui.view">
    <field name="name">my.model.form</field>
    <field name="model">my.model</field>
    <field name="arch" type="xml">
        <form string="My Model">
            <header>
                <button name="action_confirm"
                        type="object"
                        string="Confirm"
                        class="btn-primary"
                        invisible="state != 'draft'"/>
                <button name="action_cancel"
                        type="object"
                        string="Cancel"
                        invisible="state not in ('draft', 'confirmed')"/>
                <field name="state" widget="statusbar"
                       statusbar_visible="draft,confirmed,done"/>
            </header>
            <sheet>
                <div class="oe_button_box" name="button_box">
                    <button name="action_view_invoices"
                            type="object"
                            class="oe_stat_button"
                            icon="fa-pencil-square-o">
                        <field name="invoice_count" widget="statinfo" string="Invoices"/>
                    </button>
                </div>
                <widget name="web_ribbon" title="Archived"
                        bg_color="bg-danger"
                        invisible="active"/>
                <div class="oe_title">
                    <h1>
                        <field name="name" placeholder="Name"/>
                    </h1>
                </div>
                <group>
                    <group string="General">
                        <field name="partner_id"/>
                        <field name="date"/>
                        <field name="user_id"/>
                    </group>
                    <group string="Details">
                        <field name="company_id" groups="base.group_multi_company"/>
                        <field name="currency_id" invisible="1"/>
                        <field name="amount"/>
                    </group>
                </group>
                <notebook>
                    <page string="Lines" name="lines">
                        <field name="line_ids">
                            <tree editable="bottom">
                                <field name="sequence" widget="handle"/>
                                <field name="name"/>
                                <field name="quantity"/>
                                <field name="price_unit"/>
                                <field name="subtotal"/>
                            </tree>
                        </field>
                    </page>
                    <page string="Notes" name="notes">
                        <field name="notes" placeholder="Internal notes..."/>
                    </page>
                </notebook>
            </sheet>
            <div class="oe_chatter">
                <field name="message_follower_ids"/>
                <field name="activity_ids"/>
                <field name="message_ids"/>
            </div>
        </form>
    </field>
</record>
```

## Visibility syntax by version

### v14-v16: `attrs`

```xml
<field name="partner_id"
       attrs="{'invisible': [('state', '=', 'draft')],
               'readonly': [('state', '!=', 'draft')],
               'required': [('type', '=', 'customer')]}"/>
```

### v17+: inline expressions

```xml
<field name="partner_id"
       invisible="state == 'draft'"
       readonly="state != 'draft'"
       required="type == 'customer'"/>
```

### Expression conversion table

| `attrs` Domain | v17+ Expression |
|----------------|-----------------|
| `[('field', '=', 'value')]` | `field == 'value'` |
| `[('field', '!=', 'value')]` | `field != 'value'` |
| `[('field', '=', True)]` | `field` |
| `[('field', '=', False)]` | `not field` |
| `[('field', 'in', ['a', 'b'])]` | `field in ('a', 'b')` |
| `[('field', '>', 0)]` | `field > 0` |
| `['&', A, B]` | `A and B` |
| `['|', A, B]` | `A or B` |

### Complex expressions

```xml
<field name="x" invisible="state == 'draft' and not is_manager"/>
<field name="y" invisible="state == 'cancelled' or archived"/>
```

## Practical guidance

- Prefer minimal, targeted XML changes.
- Keep IDs and names consistent and module-scoped.
- Use the correct syntax for the target version rather than writing "compatible-looking" XML.
- When working on v17+, do not reintroduce `attrs`.

## Related sources

- `odoo-version-routing.md`
- `odoo-version-knowledge-17.md`
- `odoo-version-knowledge-18.md`
- `odoo-version-knowledge-19.md`
