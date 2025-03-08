# -*- coding: utf-8 -*-
{
    'name': "Coworking Management",

    'summary': """
        This module purpose is to build Coworking Space module""",

    'description': """
        Build Coworking Space modul
    """,

    'author': "K.Yudha.F",
    'website': "https://www.houseofluzka.com",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Services',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hol_menu.xml',
        'views/hol_space_view.xml',
        'views/hol_booking_view.xml',
        'views/hol_member_view.xml',
        'views/hol_membership_plan_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}