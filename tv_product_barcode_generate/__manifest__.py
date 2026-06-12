# -*- coding: utf-8 -*-
# Powered by Techvoot Solutions.
# © 2018 Techvoot Solutions. (<https://www.techvoot.com/>).
# See LICENSE file for full copyright & licensing details.

{
    "name": "Product Barcode Generator",
    "version": "19.0.1.0.0",
    "category": "Inventory",
    "summary": """In "Product Barcode Generator" Module Users Can Automatically Generate Unique Product Barcodes Using Configurable Barcode Formats And Sequence Rules This Simplifies Barcode Management Reduces Manual Entry Errors And Ensures Consistent Barcode Generation Across Products
    product barcode | barcode generator | barcode management | generate barcode | automatic barcode | inventory barcode | product identification | barcode sequence | EAN barcode | UPC barcode | Code 128 barcode""",
    "description": """In "Product Barcode Generator" Module Users Can Generate Product Barcodes Automatically Through Configurable Settings And Barcode Generation Tools The Module Helps Maintain Unique And Standardized Barcodes For Products While Improving Inventory Accuracy Reducing Manual Work And Simplifying Product Identification Across Business Operations""",
    "author": "Techvoot Solutions",
    'website': "https://www.techvoot.com",
    "license": "OPL-1",
    "depends": [
        "base",
        "base_setup",
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/barcode_security.xml",
        "data/sequence.xml",
        "views/product_template_views.xml",
        "views/barcode_generate_wizard_views.xml",
        "views/res_config_settings_views.xml",
    ],

    "installable": True,
    "application": False,
    "auto_install": False,
    'images': ['static/description/banner.gif'],
}
