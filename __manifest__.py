# -*- coding: utf-8 -*-

{
    "name": """User Signature Key""",
    'version': '1.0.0.0',
    'category': 'Utilities',
    'sequence': 12,
    'author':  'Daniel Santibáñez Polanco, La Otra Opcion, BMyA SA - Blanco Martín & Asociados',
    'website': 'http://blancomartin.cl',
    'license': 'AGPL-3',
    'summary': '',
    'description': """
Allow Users to upload a private key certificate, in order to authenticate or
sign electronic documents.
=============================================================================
""",
    'external_dependencies': {
        'python': [
            'base64',
            'OpenSSL'
        ]
    },
    'depends': [
        'base',
    ],
    'data': [
        'views/res_users_view.xml',
        'views/res_company_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
