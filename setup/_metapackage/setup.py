import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-invoicing",
    description="Meta package for oca-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_invoice_blocking>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_change_currency>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_check_picking_date>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_check_total>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_date_due>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_fiscal_position_update>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_fixed_discount>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_payment_term_date_due>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_pricelist>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_refund_link>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_search_by_reference>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_section_sale_order>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_supplier_ref_unique>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_supplier_self_invoice>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tax_note>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tax_required>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_transmit_method>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_tree_currency>=15.0dev,<15.1dev',
        'odoo-addon-account_invoice_triple_discount>=15.0dev,<15.1dev',
        'odoo-addon-account_move_exception>=15.0dev,<15.1dev',
        'odoo-addon-account_move_post_block>=15.0dev,<15.1dev',
        'odoo-addon-account_move_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-account_move_tier_validation_forward>=15.0dev,<15.1dev',
        'odoo-addon-account_tax_group_widget_base_amount>=15.0dev,<15.1dev',
        'odoo-addon-portal_account_personal_data_only>=15.0dev,<15.1dev',
        'odoo-addon-purchase_stock_picking_return_invoicing>=15.0dev,<15.1dev',
        'odoo-addon-sale_line_refund_to_invoice_qty>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_invoicing_grouping_criteria>=15.0dev,<15.1dev',
        'odoo-addon-sale_timesheet_invoice_description>=15.0dev,<15.1dev',
        'odoo-addon-stock_picking_return_refund_option>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
