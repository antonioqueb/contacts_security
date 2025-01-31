# Contacts Security

Este módulo para Odoo 17 añade reglas de seguridad para que **solo** los usuarios
con el **grupo "Gestores de Contactos"** puedan crear y editar registros de `res.partner`.
El resto de usuarios internos podrán ver los contactos, pero no tendrán la opción
de crearlos ni editarlos.

---

## Características

1. Crea un grupo nuevo (`Gestores de Contactos`) que tiene permisos totales
   sobre el modelo `res.partner`.
2. Limita a los usuarios del grupo `base.group_user` (usuarios internos normales)
   a solo lectura (`perm_read`) sobre `res.partner`.
3. (Opcional) Incluye reglas de registros (`record rules`) si se requiere mayor granularidad.

## Instalación

1. Copia la carpeta `contacts_security` dentro de tu carpeta `addons` o en una
   ruta reconocida por Odoo.
2. Actualiza la lista de aplicaciones desde el **Apps** en Odoo o usando el comando:
 odoo -u contacts_security -d <nombre_base_datos>
3. Instala el módulo **Contacts Security** en Odoo.

## Uso

1. Navega a **Configuración** → **Usuarios y Empresas** → **Usuarios**.
2. Edita un usuario y márcalo en el grupo **"Gestores de Contactos"**.
- Ese usuario ahora podrá crear, editar y borrar contactos.
3. Cualquier usuario que no sea parte de ese grupo, pero que sea un usuario interno
(`base.group_user`), tendrá permiso únicamente de lectura sobre los contactos.
4. Comprueba que el botón **"Crear"** y la acción **"Editar"** aparezcan solo para
los "Gestores de Contactos".

## Créditos

- Autor: Alphaqueb Consulting
- Basado en la documentación oficial de Odoo y buenas prácticas de seguridad.



