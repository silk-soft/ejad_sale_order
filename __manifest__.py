# -*- coding: utf-8 -*-

# noinspection PyStatementEffect
{
    'name': 'Ejad Quotation Edits',
    'version': '14.0.1.0001',
    'category': 'Sales',
    'sequence': 105,
    'summary': 'Module to handle all small customization requests in sale module for Ejad ',
    'description': """Edits requested by Ejad for quotation view""",
    'website': 'https://silksoft.org',
    'author': 'SilkSoft Inc',
    'license': 'AGPL-3',
    'depends': ["sale"],
    'data': [
        'security/security.xml',
        'views/sale.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}