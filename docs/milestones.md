# Gestión de Medicamentos - Milestones

## **[M0] Milestone 0: Estructura del problema**
En este paso fundamental se delinea la arquitectura general del sistema, identificando las entidades principales como medicamentos, inventario y usuarios, pero sin entrar en relaciones ni detalles complejos. El objetivo es proporcionar un prototipo mínimo que permita sentar las bases para el desarrollo futuro. En esta fase se deberá establecer una estructura sencilla y funcional que se irá ampliando en etapas posteriores.

El milestone será completado cuando el código represente correctamente el problema, en base a la información recopilada en las historias de usuario antes mencionadas.

**Historias de usuario asociadas**:  
- [HU1]

---

## **[M1] Milestone 1: Gestión esencial del inventario**
crear un sistema de gestión del inventario funcional, aunque básico. El sistema permitirá visualizar los medicamentos insertados manualmente y monitorizar las cantidades. Todavía no habrá una integración automática para la adquisición de datos, pero el usuario podrá consultar y actualizar la información de manera manual.

**Historias de usuario asociadas**:  
- [HU2]

---

## **[M2] Milestone 2: Sistema de notificaciones**
El sistema comenzará a admitir funciones básicas de notificación. Esta fase introduce notificaciones simples que avisan al usuario cuando las existencias de un medicamento caen por debajo de un umbral predefinido, gestionado manualmente por el usuario.

El milestone se considerará completado cuando el sistema envíe correctamente notificaciones basadas en reglas predefinidas (como fecha de caducidad o nivel mínimo de existencias).

**Historias de usuario asociadas**:  
- [HU3]

---

## **[M3] Milestone 3: Inserción automática**
En este punto, el sistema mejora con la adición de una funcionalidad de inserción automática de medicamentos a través de tickets electrónicos(PDF). Esta versión será sencilla, limitándose a extraer los datos clave (nombre, cantidad, fecha de compra) de los tickets proporcionados por el usuario e insertarlos automáticamente en el inventario.

El milestone se considerará completado cuando el sistema permita gestionar automáticamente las existencias y enviar notificaciones basadas en los niveles mínimos y las fechas de caducidad.

**Historias de usuario asociadas**:  
- [HU4]
---
