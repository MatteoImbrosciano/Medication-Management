class Medicamento:
    
    def __init__(self, nombre, cantidad, precio):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un valor numérico positivo")
        if precio <= 0:
            raise ValueError("El precio debe ser un valor numérico positivo")
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
