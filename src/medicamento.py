class Medicamento:
    def __init__(self, nombre, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un valor positivo")
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}"
