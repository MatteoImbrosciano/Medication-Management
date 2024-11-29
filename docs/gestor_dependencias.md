# Gestore di Dipendenze

## **Criterios de Selección**
Para elegir el gestor de dependencias para nuestro proyecto, hemos considerado los siguientes criterios:

1. **Compatibilidad**: El gestor de dependencias debe ser compatible con el runtime elegido (en este caso Python) y admitir estándares modernos como `pyproject.toml`.
2. **Simplicidad**: Debe ser fácil de usar, con comandos intuitivos y una configuración mínima.
3. **Comunidad**: Debe contar con una comunidad activa que proporcione soporte en caso de problemas.

---

## **Gestores de Dependencias**
Existen varios gestores de dependencias para Python. Entre los principales, hemos considerado **Poetry**, **PDM** y **Hatch**.

### 1. **Poetry**
- **Descripción**: Poetry es un gestor moderno que utiliza `pyproject.toml` como archivo principal de configuración.
- **Ventajas**:
  - Compatible con los estándares de Python, incluida la PEP 518.
  - Bloquea las versiones de las dependencias mediante un archivo `poetry.lock`.
  - Amplia comunidad y actualizaciones regulares.
- **Desventajas**:
  - Requiere instalación inicial, aunque está bien documentada.
- **Snyk - Análisis de Vulnerabilidades**: [Snyk sobre Poetry](https://snyk.io/advisor/python/poetry)

---

### 2. **PDM**
- **Descripción**: PDM es una herramienta minimalista para la gestión de dependencias, que también utiliza `pyproject.toml`.
- **Ventajas**:
  - Ligero y rápido.
  - Soporta la PEP 582, permitiendo su uso sin entornos virtuales.
- **Desventajas**:
  - Menos popular que Poetry, con una comunidad más pequeña.
- **Snyk - Análisis de Vulnerabilidades**: [Snyk sobre PDM](https://snyk.io/advisor/python/pdm)

---

### 3. **Hatch**
- **Descripción**: Hatch es un gestor de dependencias enfocado en la gestión de entornos virtuales y configuraciones avanzadas.
- **Ventajas**:
  - Soporte para configuraciones multi-entorno, ideal para proyectos complejos.
  - Integración con herramientas de desarrollo, como la gestión de múltiples versiones.
- **Desventajas**:
  - Comunidad más pequeña en comparación con Poetry.
  - Puede ser complejo para proyectos simples.
- **Snyk - Análisis de Vulnerabilidades**: [Snyk sobre Hatch](https://snyk.io/advisor/python/hatch)

---

## **Selección del Gestor de Dependencias**
Para nuestro proyecto, hemos elegido **Poetry** como gestor de dependencias. Las razones son:

1. Es compatible con `pyproject.toml`, que es el estándar moderno para la configuración de proyectos Python.
2. Ofrece una gestión avanzada de dependencias con bloqueo de versiones.
3. Cuenta con una comunidad activa y actualizada regularmente, facilitando el soporte y la evolución del proyecto.
