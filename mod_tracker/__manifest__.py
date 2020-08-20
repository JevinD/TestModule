# -*- coding: utf-8 -*-
{
    "name": "Module Tracker",
    "summary": """
        OSI module project tracking system""",
    "description": """
        Ability to search for modules that are used in projects or past projects
    """,
    "author": "Jevin Dement",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    "application": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "hr", "project"],
    # always loaded
    "data": [
        #    "security/security.xml",
        "security/ir.model.access.csv",
        "views/module_tracker.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml",],
}
