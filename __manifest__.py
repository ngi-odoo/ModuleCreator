{
    'name': "ModuleCreator",
    'version': '0.1',
    'category': 'Technical',
    'summary': 'Create modules',
    'description': "",
    'website': "https://github.com/ngi-odoo",
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        'security/creator_security.xml',
        'security/ir.model.access.csv',
        'views/creator_field_views.xml',
        'views/creator_model_views.xml',
        'views/creator_project_views.xml',
        'views/creator_menuitem.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'license': 'AGPL-3',
    'application': True
}
