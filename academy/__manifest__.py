# -*- coding: utf-8 -*-
{
    "name": "Academy",
    "summary": """
        University system""",
    "description": """
        Testing new features with a university based system
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
    "depends": ["base", "website", "mail"],
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/academy_menu.xml",
        "views/academy.xml",
        "views/templates.xml",
        "views/instructor.xml",
    ],
    # only loaded in demonstration mode
    # "demo": ["demo/demo.xml",],
}
