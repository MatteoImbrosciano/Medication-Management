# Gestor de Dependencias

En el proyecto de gestión de medicamentos, es necesario elegir un gestor de dependencias adecuado. Este proyecto utiliza Python y requiere automatizar la instalación de librerías y garantizar la consistencia en todos los entornos. Basándome en la estructura y necesidades del proyecto, he definido criterios específicos para seleccionar el gestor más adecuado.

---

## Criterios de Selección

1. **Soporte a `pyproject.toml`:** El gestor debe utilizar el estándar `pyproject.toml` para garantizar la conformidad con las prácticas modernas de Python.
2. **Manejo de versiones:** El gestor debe proporcionar un archivo de bloqueo que permita garantizar la coherencia de las dependencias entre entornos.
3. **Simplicidad de integración:** El gestor debe ser fácil de configurar y usar, permitiendo al equipo centrarse en el desarrollo del proyecto en lugar de resolver problemas relacionados con dependencias.
4. **Relevancia para el proyecto:** El gestor debe ser capaz de satisfacer las necesidades específicas del proyecto, como el desarrollo local, los entornos de prueba y el despliegue futuro.
5. **Soporte de la comunidad:** Debe ser una herramienta activa, con actualizaciones regulares y una comunidad amplia que pueda ofrecer recursos adicionales en caso de problemas.

---

## Análisis de Alternativas

### **1. PDM**
- **Soporte a `pyproject.toml`:** Totalmente compatible.
- **Manejo de versiones:** Proporciona un archivo de bloqueo (`pdm.lock`) que asegura la consistencia de las dependencias.
- **Simplicidad de integración:** Su configuración inicial es rápida, pero la curva de aprendizaje puede ser mayor para usuarios que no conocen el PEP 582.
- **Relevancia para el proyecto:** Puede cubrir las necesidades básicas, pero su enfoque en entornos globales podría complicar la separación entre proyectos.
- **Soporte de la comunidad:** En crecimiento, pero menos extendido que Poetry.

### **2. Hatch**
- **Soporte a `pyproject.toml`:** Totalmente compatible.
- **Manejo de versiones:** Genera un archivo de bloqueo (`hatch.lock`) similar a PDM y Poetry.
- **Simplicidad de integración:** Fácil de usar para proyectos pequeños, pero requiere configuraciones adicionales para gestionar entornos virtuales.
- **Relevancia para el proyecto:** Es útil, pero no crea automáticamente entornos virtuales, lo cual es una necesidad para este proyecto.
- **Soporte de la comunidad:** A pesar de ser nuevo, cuenta con un soporte activo, aunque no tan grande como el de Poetry.

### **3. Poetry**
- **Soporte a `pyproject.toml`:** Totalmente compatible.
- **Manejo de versiones:** Genera un archivo de bloqueo (`poetry.lock`) para asegurar la consistencia de las dependencias.
- **Simplicidad de integración:** Comandos claros (`poetry add`, `poetry update`) que facilitan la gestión.
- **Relevancia para el proyecto:** Es capaz de cubrir todas las necesidades del proyecto, incluyendo la gestión automática de entornos virtuales.
- **Soporte de la comunidad:** Es una herramienta madura y ampliamente utilizada, lo que la hace ideal para un proyecto de largo plazo.

---

## Elección Final

Tras comparar las herramientas mencionadas, **Poetry** es la elección más adecuada para este proyecto por los siguientes motivos:

1. **Automatización completa:** Poetry gestiona tanto dependencias como entornos virtuales, reduciendo la necesidad de herramientas adicionales.
2. **Consistencia garantizada:** El archivo `poetry.lock` asegura que las versiones de las dependencias sean las mismas en todos los entornos.
3. **Soporte sólido:** Es una herramienta estable, con amplio respaldo de la comunidad Python.
4. **Alineación con el proyecto:** Poetry se adapta perfectamente a las necesidades específicas de un sistema de gestión de medicamentos en Python, desde el desarrollo hasta el despliegue.

---

## Reflexión

El análisis presentado aquí se centra exclusivamente en las necesidades y características de este proyecto. Evité recurrir a patrones genéricos y tomé decisiones informadas basadas en los criterios definidos.
