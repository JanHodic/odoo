# veterinary_module/__manifest__.py

var = {
    'name': 'Veterinary Module',
    'version': '1.0.0',
    'summary': 'Module for managing animals and medical data',
    'description': 'An Odoo module to handle animal records, diagnoses, and related veterinary operations.',
    'author': 'Your Name or Company',
    'website': 'https://your-website.com',
    'category': 'Services',
    'depends': ['base', 'web'],
    'data': [
        # views, security, data files, here
        # 'security/ir.model.access.csv',
        # 'views/animal_views.xml',
    ],
    'assets': {
        # react belongs here
    },
    'application': True,  # = to show in odoo as an app
    'installable': True,  # = prepared for installation
    'auto_install': False,  # = automatically not installed
}
