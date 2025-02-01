# contacts_security

## Descripción

Este módulo para Odoo 17 restringe la **creación y edición de contactos** (`res.partner`)
solo a usuarios que pertenezcan al grupo **"Gestores de Contactos"**. Todos los demás
usuarios, incluyendo los de Ventas, quedan con acceso de solo lectura. Esto impide que
en un presupuesto/venta, al buscar o teclear un nombre de contacto inexistente, aparezca
el botón "Crear y Editar…" para usuarios sin permiso.

## Características

1. Crea un grupo **"Gestores de Contactos"** con acceso total (crear, editar, eliminar) sobre `res.partner`.
2. Deja a los usuarios internos (`base.group_user`) únicamente con lectura.
3. **Sobrescribe** los permisos en los grupos de ventas (`sales_team.group_sale_salesman` y `sales_team.group_sale_manager`) para que no puedan crear ni editar contactos.
4. Añade **record rules** que refuerzan que solo el grupo "Gestores de Contactos" tenga escritura y creación.

## Instalación

1. Copia la carpeta `contacts_security` en tu carpeta de addons reconocida por Odoo.
2. Actualiza la lista de aplicaciones y luego instala **"Restricción de Creación de Contactos"**.
3. Asigna el grupo "Gestores de Contactos" a quienes necesiten crear/editar contactos.

## Uso

- Un usuario sin el grupo "Gestores de Contactos" no verá el botón "Crear" en el módulo de contactos
  ni podrá crear contactos desde formularios de ventas (desaparecerá la opción "Crear y Editar…").
- Un usuario con el grupo "Gestores de Contactos" sí tendrá permisos para crear, editar o borrar contactos.

---

## Notas

- Si el usuario pertenece al grupo “Administrador” o “Configuración”, tendrá permisos totales
  independientemente de este módulo, ya que Odoo considera a los administradores como superusuarios.
- Si deseas permitir que los gerentes de ventas sí creen contactos, puedes ajustar la línea CSV correspondiente
  en `ir.model.access.csv` y/o en las record rules, devolviendo `perm_create=1`.
