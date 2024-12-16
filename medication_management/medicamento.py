class Medicamento:
    def __init__(self, nombre, cantidad, precio, unitad):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un valor numérico positivo.")
        if precio <= 0:
            raise ValueError("El precio debe ser un valor numérico positivo.")
        if not isinstance(unitad, str) or not unitad.strip():
            raise ValueError("La unidad debe ser una cadena no vacía.")

        self.nombre = nombre.strip()
        self.cantidad = cantidad
        self.precio = precio
        self.unitad = unitad.strip()

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} {self.unitad}): €{self.precio:.2f}"
