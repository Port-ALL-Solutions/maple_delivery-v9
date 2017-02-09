# -*- coding: utf-8 -*-
{
    'name': "Livraison",

    'summary': """
        Livraison aux clients et fournisseurs""",

    'description': """
		Gestion de la livraison de barils et de totes aux clients et fournisseurs
    """,

    'author': "Global Technologie",
    'website': "http://www.globaltechnologie.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['mapletransform'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
#        'views/templates.xml',
    ],
    # only loaded in demonstration mode
#    'demo': [
#        'demo/demo.xml',
#    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}