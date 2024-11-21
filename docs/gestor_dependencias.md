# Gestión de Dependencias

En el desarrollo del sistema de gestión de medicamentos en Python, la elección de una herramienta adecuada para la gestión de dependencias es crucial. Este sistema requiere un entorno estable, reproducible y eficiente, que permita a los desarrolladores trabajar de manera coordinada y minimizar los errores relacionados con versiones inconsistentes de las librerías. 

---

## Metodología de Selección

Para identificar las herramientas más adecuadas, se siguieron estos pasos:

1. **Definición de criterios:** Basados en las necesidades del proyecto, se establecieron requisitos claros (ver criterios más abajo).
2. **Investigación inicial:** Se consultaron fuentes oficiales de Python, documentación de herramientas y discusiones en foros técnicos.
3. **Filtrado:** Entre las opciones disponibles, se priorizaron aquellas compatibles con los estándares actuales (`pyproject.toml`) y ampliamente utilizadas en la comunidad Python.
4. **Criterio de exclusión:** Se descartaron herramientas que no ofrecieran automatización o soporte sólido para entornos virtuales.

Las herramientas consideradas para este proyecto fueron **PDM**, **Hatch**, **Poetry** y **Makefile** (como alternativa generalista para la automatización).

---

## Criterios de Selección

1. **Compatibilidad con estándares modernos de Python:** El formato `pyproject.toml` debe ser soportado.
2. **Gestión de versiones consistente:** La herramienta debe ofrecer un archivo de bloqueo para garantizar entornos reproducibles.
3. **Facilidad de uso:** Los comandos deben ser intuitivos y fáciles de adoptar por el equipo.

---

## Cómo se cumplen los criterios

### **1. Automatización de tareas repetitivas**
- **Poetry:** Permite definir y ejecutar tareas personalizadas directamente desde el archivo `pyproject.toml`, como `poetry run pytest` para pruebas y `poetry run flake8` para verificar estilo.
- **Hatch:** Ofrece funcionalidades similares mediante su sistema modular, pero requiere configuraciones adicionales para tareas avanzadas.
- **PDM:** No incluye una funcionalidad integrada para la automatización de tareas, lo que exige el uso de herramientas externas.

### **2. Compatibilidad con estándares modernos**
- Todas las herramientas evaluadas soportan `pyproject.toml` y cumplen con los estándares definidos en los PEP 517 y 518.

### **3. Facilidad para proyectos colaborativos**
- **Poetry:** Automatiza la gestión de entornos virtuales, asegurando que todos los desarrolladores trabajen en condiciones consistentes.
- **Hatch:** No automatiza la creación de entornos virtuales, lo que requiere configuraciones manuales adicionales.
- **PDM:** Usa directorios locales en lugar de entornos virtuales tradicionales, lo que puede generar confusión en equipos grandes.

### **4. Soporte y mantenimiento a largo plazo**
- **Poetry:** Es ampliamente adoptada en la comunidad Python, con actualizaciones regulares y una documentación extensa.
- **Hatch:** Aunque es prometedora, tiene una comunidad más pequeña y menos recursos disponibles.
- **PDM:** Su adopción es limitada y su comunidad aún está en crecimiento.

---

## Análisis Comparativo

Se evaluaron tres herramientas principales para la gestión de dependencias en Python: **PDM**, **Hatch** y **Poetry**. A continuación, se presenta un resumen de su análisis:

- **PDM:** Innovador al eliminar los entornos virtuales tradicionales mediante el uso de directorios locales. Sin embargo, su falta de automatización de tareas y comunidad limitada lo hacen menos adecuado para este proyecto.
- **Hatch:** Versátil y modular, ideal para proyectos complejos gracias a su soporte de plugins. No obstante, la falta de automatización de entornos virtuales y su adopción limitada dificultan su uso en proyectos colaborativos.
- **Poetry:** Herramienta madura, con automatización integral de entornos virtuales y tareas repetitivas. Su interfaz intuitiva y comunidad sólida la convierten en la opción más confiable para este proyecto.

---

## Elección Final

Basándonos en los criterios definidos, **Poetry** es la herramienta seleccionada para la gestión de dependencias. Esta decisión se debe a:

1. Su compatibilidad total con los estándares actuales (`pyproject.toml`).
2. Su capacidad para gestionar versiones de manera consistente mediante el archivo `poetry.lock`.
3. La facilidad de uso y comandos claros, que simplifican la adopción.

---

## Conclusión

La elección de Poetry no solo responde a las necesidades técnicas del proyecto. Cada herramienta fue evaluada con criterios claros, asegurando que la decisión final no fuera arbitraria ni influenciada por patrones genéricos. Este enfoque garantiza que el sistema de gestión de medicamentos contará con una base estable y eficiente, facilitando tanto el desarrollo como el mantenimiento a largo plazo.

