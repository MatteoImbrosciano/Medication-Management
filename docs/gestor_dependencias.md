# Gestor de Dependencias

En el proyecto de gestión de medicamentos en Python, hemos elegido **Poetry** como gestor de dependencias, una herramienta moderna y ampliamente utilizada en la comunidad de Python. A continuación se explican las razones por las que Poetry es la opción más adecuada para este proyecto:

Poetry utiliza el estándar `pyproject.toml` para gestionar tanto las dependencias como la configuración del proyecto, permitiendo una estructura centralizada y organizada. Esto facilita su integración con otras herramientas y entornos de desarrollo modernos en Python.

Poetry genera automáticamente un archivo `poetry.lock`, lo que garantiza que las versiones de las dependencias se mantengan consistentes en distintos entornos. Este archivo de bloqueo ayuda a prevenir conflictos y asegura que el proyecto funcione correctamente en cada configuración.

Poetry facilita la creación y administración de entornos virtuales específicos para cada proyecto, proporcionando una separación clara entre proyectos y una instalación más segura y ordenada de las dependencias.

Con comandos como `poetry add` y `poetry update`, Poetry permite instalar y actualizar dependencias de manera sencilla, asegurando que las versiones sean siempre compatibles con el proyecto.

### Comparación con otras herramientas
Aunque existen otras herramientas que también usan `pyproject.toml`, como **PDM** y **Hatch**, **Poetry** destaca por su popularidad y su conjunto completo de funciones para manejar tanto dependencias como entornos virtuales de forma intuitiva y eficiente.