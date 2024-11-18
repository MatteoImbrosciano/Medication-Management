# Gestor de Tareas

En este proyecto de Python, es necesario automatizar tareas repetitivas como la instalación de dependencias, la ejecución de pruebas y la verificación de sintaxis del código. Para seleccionar el gestor de tareas más adecuado, se han definido los siguientes **criterios de aceptación**.

### Criterios de Aceptación

1. **Conformidad con los estándares del lenguaje:**
   El gestor de tareas debe ser compatible con el estándar moderno de Python, preferentemente utilizando `pyproject.toml` como archivo de configuración principal.

2. **Facilidad de uso:**
   Debe ofrecer una sintaxis clara y comandos intuitivos, con una curva de aprendizaje baja para nuevos desarrolladores.

3. **Integración con dependencias:**
   Debe facilitar la gestión de dependencias y permitir integrar tareas automatizadas sin la necesidad de herramientas adicionales.

4. **Mantenimiento activo:**
   El gestor debe estar mantenido por la comunidad y ofrecer actualizaciones frecuentes para minimizar riesgos técnicos a largo plazo.

5. **Simplicidad en el MVP:**
   Para cumplir con el producto mínimamente viable, debe ser suficiente para automatizar tareas básicas como instalar dependencias, verificar la sintaxis y ejecutar pruebas.

---

### Análisis 

#### **Poetry**
- **Ventajas:**
  1. Compatible con los estándares modernos de Python (`pyproject.toml`).
  2. Permite gestionar dependencias y tareas en un solo archivo.
  3. Ofrece comandos intuitivos como `poetry install`, `poetry run pytest`, y `poetry check`.
  4. Está activamente mantenido por la comunidad de Python.
  5. Suficiente para automatizar tareas esenciales en el MVP sin agregar complejidad.
- **Desventajas:** Menos flexible que herramientas como `Make` para tareas avanzadas, pero esto no es un problema para este proyecto.

---

### Elección Final

Para este proyecto, se ha elegido **Poetry** como gestor de tareas debido a que cumple con todos los criterios establecidos. En particular:

1. **Cumple con los estándares modernos:** Utiliza `pyproject.toml`, el estándar actual de Python para configuración.
2. **Facilita la gestión de dependencias y tareas:** Todo está centralizado en un solo archivo, lo que simplifica la configuración y el mantenimiento.
3. **Intuitivo y fácil de usar:** Los comandos como `poetry install` y `poetry run` son simples y claros.
4. **Adecuado para el MVP:** Es suficiente para gestionar tareas básicas como instalar dependencias, verificar la sintaxis (`poetry check`) y ejecutar pruebas (`poetry run pytest`).

---

### Conclusión

La elección de **Poetry** permite mantener el proyecto alineado con las mejores prácticas de Python, garantizando simplicidad y efectividad en la gestión de tareas automatizadas.
