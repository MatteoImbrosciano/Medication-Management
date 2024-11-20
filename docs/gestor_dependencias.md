# Gestor de Dependencias

En este proyecto de Python para la gestión de medicamentos, es necesario elegir un gestor de dependencias que garantice consistencia, simplicidad y soporte a largo plazo. Para identificar la mejor herramienta, se han definido los siguientes **criterios de selección**.

---

## Criterios de Selección

1. **Conformidad con los estándares de Python:** El gestor debe ser compatible con el formato `pyproject.toml`, el estándar moderno para la configuración de proyectos en Python.
2. **Gestión de versiones:** Debe garantizar la consistencia de las versiones de las dependencias entre diferentes entornos mediante un archivo de bloqueo.
3. **Facilidad de uso:** Debe ofrecer comandos simples para agregar, actualizar y eliminar dependencias.
4. **Creación de entornos virtuales:** Debe facilitar la creación y administración de entornos virtuales específicos para cada proyecto.
5. **Soporte de la comunidad y actualizaciones regulares:** La herramienta debe estar mantenida activamente y contar con amplio soporte para evitar problemas a largo plazo.

---

## Análisis Comparativo

Se evaluaron las siguientes herramientas con base en los criterios establecidos:

### **PDM**
- **Conformidad con los estándares:** Soporta `pyproject.toml` y sigue el estándar PEP 582.
- **Gestión de versiones:** Proporciona un archivo de bloqueo (`pdm.lock`) para garantizar la consistencia de las versiones.
- **Facilidad de uso:** Ofrece comandos sencillos, pero requiere cierta curva de aprendizaje para usuarios nuevos.
- **Creación de entornos virtuales:** Utiliza entornos globales, lo que dificulta la separación clara entre proyectos.
- **Soporte de la comunidad:** Menos popular que otras soluciones, con una comunidad en crecimiento pero todavía pequeña.

### **Hatch**
- **Conformidad con los estándares:** Compatible con `pyproject.toml` y orientado a la gestión moderna de proyectos Python.
- **Gestión de versiones:** Ofrece un archivo de bloqueo (`hatch.lock`).
- **Facilidad de uso:** Los comandos son claros, pero algunas funcionalidades avanzadas pueden ser más complejas de implementar.
- **Creación de entornos virtuales:** No crea entornos virtuales automáticamente, lo que requiere configuraciones adicionales.
- **Soporte de la comunidad:** Relativamente nuevo, con una adopción creciente pero no tan extendida como Poetry.

### **Poetry**
- **Conformidad con los estándares:** Compatible con `pyproject.toml` y los estándares PEP 517/518.
- **Gestión de versiones:** Genera automáticamente un archivo de bloqueo (`poetry.lock`), asegurando la consistencia entre entornos.
- **Facilidad de uso:** Comandos intuitivos como `poetry add` y `poetry update` simplifican la gestión de dependencias.
- **Creación de entornos virtuales:** Administra automáticamente entornos virtuales para cada proyecto.
- **Soporte de la comunidad:** Herramienta madura, con una amplia comunidad y actualizaciones regulares.

---

## Elección Final

Tras analizar las opciones, se ha seleccionado **Poetry** como gestor de dependencias para este proyecto por las siguientes razones:

1. **Soporte a estándares modernos:** Utiliza `pyproject.toml`, cumpliendo con los estándares actuales de Python.
2. **Gestión confiable de versiones:** El archivo `poetry.lock` garantiza la consistencia en diferentes entornos.
3. **Facilidad de uso:** Comandos claros como `poetry install` y `poetry run` simplifican la configuración y gestión del proyecto.
4. **Entornos virtuales:** Automatiza la creación y administración de entornos, mejorando la organización.
5. **Soporte activo:** Amplia adopción y mantenimiento continuo, lo que garantiza estabilidad a largo plazo.

---

## Conclusión

La elección de **Poetry** satisface plenamente los criterios establecidos, ofreciendo una combinación óptima de simplicidad, consistencia y compatibilidad con los estándares de Python.

