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

### **1. Compatibilidad con estándares modernos**
Poetry, PDM y Hatch soportan completamente el formato `pyproject.toml`, cumpliendo con los estándares definidos en los PEP 517 y 518.

### **2. Gestión de versiones consistente**
Todas las herramientas analizadas (Poetry, PDM, Hatch) generan un archivo de bloqueo (`lock file`) que asegura la coherencia de las dependencias entre entornos.

### **3. Facilidad de uso**
- **Poetry:** Destaca por comandos simples como `poetry add` y `poetry update`, facilitando la gestión.
- **Hatch:** Su enfoque modular puede ser más complejo para proyectos pequeños.
- **PDM:** Tiene una curva de aprendizaje mayor debido al PEP 582, pero sigue siendo accesible.

---

## Análisis Comparativo

Se evaluaron tres herramientas principales para la gestión de dependencias en Python: **PDM**, **Hatch** y **Poetry**. A continuación, se presenta un análisis narrativo de cada una.

### Evaluación de PDM

**PDM** utiliza pyproject.toml y sigue el PEP 582. Simplifica la gestión de dependencias eliminando los entornos virtuales tradicionales, usando directorios locales. Ofrece un archivo de bloqueo (pdm.lock) para garantizar consistencia, pero su enfoque puede ser poco intuitivo y tiene una comunidad pequeña con adopción limitada.

### Evaluación de Hatch

**Hatch** compatible con pyproject.toml y soporta archivos de bloqueo (hatch.lock). Es versátil y modular, ideal para proyectos complejos gracias a los plugins. Sin embargo, no automatiza la creación de entornos virtuales y su popularidad aún es limitada, lo que dificulta su adopción en proyectos más simples.
### Evaluación de Poetry

**Poetry** es una herramienta madura y ampliamente reconocida en la comunidad Python. Es totalmente compatible con `pyproject.toml` y cumple con los estándares definidos en los PEP 517 y PEP 518. Uno de sus mayores beneficios es la capacidad de automatizar completamente la creación y gestión de entornos virtuales, lo que reduce la complejidad de la configuración inicial y garantiza una separación clara entre proyectos.

Poetry compatible con los estándares PEP 517 y 518, automatiza completamente la gestión de entornos virtuales y asegura consistencia con poetry.lock. Su interfaz es intuitiva, con comandos simples (poetry add, poetry update), y cuenta con una comunidad sólida y amplia documentación. Es una opción madura y confiable para proyectos de cualquier escala.

---

## Elección Final

Basándonos en los criterios definidos, **Poetry** es la herramienta seleccionada para la gestión de dependencias. Esta decisión se debe a:

1. Su compatibilidad total con los estándares actuales (`pyproject.toml`).
2. Su capacidad para gestionar versiones de manera consistente mediante el archivo `poetry.lock`.
3. La facilidad de uso y comandos claros, que simplifican la adopción.

---

## Conclusión

La elección de Poetry no solo responde a las necesidades técnicas del proyecto. Cada herramienta fue evaluada con criterios claros, asegurando que la decisión final no fuera arbitraria ni influenciada por patrones genéricos. Este enfoque garantiza que el sistema de gestión de medicamentos contará con una base estable y eficiente, facilitando tanto el desarrollo como el mantenimiento a largo plazo.
