# Gestor Dependencias

Según la documentación oficial de Python, la gestión de dependencias se realiza comúnmente con herramientas como pip y archivos requirements.txt. Sin embargo, en este proyecto hemos optado por Poetry como gestor de dependencias.

Poetry es una herramienta moderna que permite definir todas las dependencias en un único archivo, pyproject.toml, que además incluye información sobre el proyecto como la versión de Python requerida, el nombre del proyecto y el autor. Esto simplifica la gestión de dependencias y elimina la necesidad de herramientas adicionales.

Otra ventaja de Poetry es su capacidad para gestionar automáticamente entornos virtuales y asegurar que todos los colaboradores utilicen la misma versión de Python, en este caso, 3.9, como se especifica en pyproject.toml.

Por estas razones, Poetry es la opción más recomendable para este proyecto, ya que facilita el control de versiones, la instalación de dependencias y el mantenimiento a largo plazo.
