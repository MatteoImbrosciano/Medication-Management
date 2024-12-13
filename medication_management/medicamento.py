class Medicamento:
    def __init__(self, nombre, cantidad, precio, unitad):

        if precio <= 0:
            raise ValueError("El precio debe ser un valor numérico positivo")
        if not isinstance(unitad, (int, float)) or unitad <= 0:
            raise ValueError("El unitad debe ser un valor positivo")
        
        # Validazione opzionale per cantidad
        if not isinstance(cantidad, str) or not cantidad.strip():
            raise ValueError("La cantidad debe ser una cadena no vacía")
        
        self.nombre = nombre
        self.cantidad = cantidad  
        self.precio = precio
        self.unitad = unitad
