{
    'name': "RE_Training",

    'summary': "Real Estate Training Module",

    'author': "Karim Hesham",

    'description': "This is a Real Estate module for odoo 17 documentation training ",

    'category': '',

    'version': '17.0.0.1.0',

    'depends': ['base', 'sale_management'],

    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tags_view.xml',
        'views/sale_order_view.xml',
    ],
    'assets' : {
        'web.assets_backend' : ['re__training/static/src/css/property.css']
    },
    'application': True,
}

