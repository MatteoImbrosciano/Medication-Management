# Gestor de Tareas

Para automatizar las tareas en este proyecto de Python, como la ejecución de pruebas o la verificación del estilo de código, hemos optado por **Poetry**. A continuación se explican las razones que hacen de Poetry la mejor opción para gestionar las tareas del proyecto:

Poetry permite que toda la configuración, incluidos los scripts de automatización, se almacene en el archivo `pyproject.toml`, eliminando la necesidad de archivos adicionales como `Makefile`. Esto facilita la administración del proyecto al mantener toda la configuración centralizada en un único lugar.

Poetry ofrece una manera fácil de definir y ejecutar comandos personalizados, como realizar pruebas (`poetry run pytest`) o verificar el estilo de código (`poetry run flake8`). Esto evita depender de otras herramientas como Make o Invoke, simplificando el flujo de trabajo.

Diseñado específicamente para Python, Poetry permite optimizar el flujo de trabajo de un proyecto sin requerir herramientas externas, lo que lo convierte en una opción ideal para este entorno.

### Comparación con otras herramientas
Aunque herramientas como Make e Invoke son ampliamente utilizadas y ofrecen muchas funcionalidades, suelen requerir configuraciones y archivos adicionales. Con Poetry, es posible centralizar todas las tareas en el archivo `pyproject.toml`, reduciendo la complejidad del proyecto y mejorando la organización.