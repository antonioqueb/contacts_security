{
    'name': 'Restricción de Creación de Contactos',
    'version': '1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Restringe la creación y edición de contactos a un grupo específico',
    'description': """
Este módulo de Odoo 17 crea un grupo "Gestores de Contactos" con permisos completos
para crear y editar contactos (res.partner). 
Todos los demás usuarios (incluyendo los de Ventas) se limitan a solo lectura.
""",
    'author': 'Alphaqueb Consulting',
    'website': 'https://www.tusitio.com',
    'license': 'LGPL-3',  # Siempre conviene especificar la licencia
    'depends': [
        'contacts',        # Para asegurarte de que el modelo res.partner ya exista
        'sales_team',      # Donde se definen los grupos de ventas
        'sale_management', # Si usas la app "Ventas" completa
        'base',            # Para los permisos básicos
    ],
    'data': [
        'security/contact_security.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
    ],
    'installable': True,
    'application': False,
}
