# Gestión de Medicamentos - Milestones

## **[M0] Milestone 0: Estructura del problema**

Analizar las historias de usuario para identificar y codificar los elementos del dominio problemático relacionados con la gestión de medicamentos y recibos electrónicos. En esta fase, el sistema permitirá la creación manual de medicamentos y del inventario, proporcionando una base para las fases siguientes y se deberá establecer una código que represente el modelo de gestión de medicamentos, permitiendo agregar manualmente medicamentos al inventario.

El milestone se considera completo cuando el sistema permite la gestión manual de medicamentos y existencias, con una interfaz que permita visualizar la información de manera clara y organizada.

---

**[M1] Milestone 1: Gestión del inventario**

Implementar una funcionalidad que permita actualizar automáticamente el inventario de medicamentos cargando los recibos electrónicos. Esto reducirá el error humano y facilitará la gestión de las existencias de medicamentos. 
Deberá entregar código fuente que permita la carga y procesamiento automático de recibos electrónicos (PDF o XML), actualizando el inventario con datos extraídos de los tickets.

El milestone será completado cuando el sistema cargue con éxito los recibos electrónicos, extrayendo la información de los medicamentos y actualizando correctamente el inventario.

---

**[M2] Milestone 2: Sistema de notificaciones**

El sistema comenzará a admitir funciones básicas de notificación. Esta fase introduce notificaciones simples que avisan al usuario cuando las existencias de un medicamento caen por debajo de un umbral predefinido, gestionado manualmente por el usuario.

El milestone se considerará completado cuando el sistema envíe correctamente notificaciones basadas en reglas predefinidas (como fecha de caducidad o nivel mínimo de existencias).
