{
    'name': 'Contacts Security',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Restringe la creación y edición de contactos a un grupo específico.',
    'description': """
    Módulo para Odoo 17 que añade un grupo especial de "Gestores de Contactos"
    y asigna permisos para que solo ellos puedan crear y editar contactos,
    mientras que el resto de usuarios internos tendrán acceso de lectura sola.
    """,
    'author': 'Alphaqueb Consulting S.A.S.',
    'website': 'https://www.tusitio.com',
    'depends': [
        'contacts',  
    ],
    'data': [
        'security/contact_security.xml',
        'security/ir.model.access.csv',
        # 'security/ir_rule.xml',  # Descomentar si deseas usar record rules adicionales
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
