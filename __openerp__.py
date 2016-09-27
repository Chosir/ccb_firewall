# -*- coding: utf-8 -*-
{
    'name': "ccb_firewall",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nantian",
    'website': "http://nantian.com.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'CCB_fwall',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ccb_firewall_view.xml',
        'views/ccb_firewall_menu.xml',
        'templates.xml',
        'views/ccb_firewall_link.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'application':True,
    'qweb':[
        'static/src/xml/firewall.xml',
    ],
}