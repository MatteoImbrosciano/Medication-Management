# Gestión de Medicamentos - Milestones

## **[M0] Milestone 0: Modelado y planificación del dominio del problema**
Entregar un modelo inicial del dominio que defina claramente las entidades clave y sus relaciones, basado en las historias de usuario. Este modelo incluirá conceptos como medicamentos, tickets electrónicos (PDF, XML) e inventario.

**Producto**:
- Código fuente que represente el modelo del dominio del problema, basado en las historias de usuario [HU1] y [HU2].
- Diagramas UML que describan las relaciones entre las entidades clave y los procesos involucrados en la gestión de medicamentos y tickets electrónicos.
  
**Factibilidad**:  
Se considerará factible cuando el código fuente entregado represente correctamente el dominio del problema en función de la información recopilada en las historias de usuario antes mencionadas.

**Historias de usuario asociadas**:  
- [HU1]: Paciente que desea cargar tickets electrónicos para actualizar automáticamente el inventario de medicamentos.
- [HU2]: Responsable de las compras para varias personas que desea gestionar el inventario familiar con tickets electrónicos.
 
---

## **[M1] Milestone 1: Gestión completa del inventario**
Entregar un sistema que permita mantener un registro completo del inventario de medicamentos, definiendo niveles mínimos y máximos para cada medicamento y monitoreando fechas de caducidad y uso. El sistema enviará notificaciones automáticas cuando las existencias estén por debajo o por encima de los límites establecidos.

**Producto**:  
- Código que implemente un registro detallado del inventario, con la posibilidad de agregar, actualizar y visualizar manualmente la información de los medicamentos.
- Funcionalidad para establecer umbrales mínimos y máximos de existencias, con monitoreo continuo de las fechas de caducidad y cantidades restantes.
- Integración con un sistema de notificaciones que avise cuando las existencias estén por debajo del nivel mínimo configurado por el usuario.

**Factibilidad**:  
El hito se considerará completado cuando el sistema permita la gestión y visualización completa del inventario

**Historias de usuario asociadas**:  
- [HU1]: Paciente que desea rastrear sus existencias de medicamentos y recibir alertas en caso de fechas de caducidad.

---

## **[M2] Milestone 2: Carga de tickets electrónicos y actualización automática del inventario**
Entregar una funcionalidad que permita a los usuarios cargar tickets electrónicos (como recibos de farmacia) y actualizar automáticamente el inventario de medicamentos con la información extraída. Esta función debe soportar formatos de tickets como PDF y XML.

**Producto**:  
- Sistema que permita la carga y el reconocimiento de tickets electrónicos en diferentes formatos (PDF, XML).
- Actualización automática del inventario con la información extraída de los tickets.

**Factibilidad**:  
El hito se completará cuando el inventario se actualice automática y correctamente con la información extraída de los tickets electrónicos, y el sistema sea validado a través de pruebas de carga de tickets en varios formatos.

**Historias de usuario asociadas**:  
- [HU2]: Responsable de las compras que carga tickets electrónicos para actualizar el inventario familiar de manera automática

---

## **[M3] Milestone 3: Sistema de notificaciones inteligentes**
Entregar un sistema de notificaciones automáticas que avise al usuario cuando un medicamento esté a punto de caducar o cuando las existencias de un medicamento estén por debajo del nivel mínimo predeterminado (sin personalización). En esta primera fase, el sistema enviará notificaciones básicas basadas en reglas predefinidas.

**Producto**:  
- Código para el envío de notificaciones configurables basadas en fechas de caducidad inminentes o existencias bajas.

**Factibilidad**:  
El hito se completará cuando el sistema envíe correctamente las notificaciones configurables, basadas en los criterios definidos por el usuario, y será validado a través de pruebas funcionales de envío de notificaciones en eventos críticos (caducidades y existencias).

**Historias de usuario asociadas**:  
- [HU3]: Usuario que desea ser alertado cuando un medicamento esté por caducar.
---
