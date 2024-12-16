from medication_management.medicamento import Medicamento

class Inventario:
    def __init__(self):
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("El objeto debe ser una instancia de la clase Medicamento.")
        for med in self.medicamentos:
            if med.nombre == medicamento.nombre:
                med.cantidad += medicamento.cantidad
                return
        self.medicamentos.append(medicamento)

    def eliminar_medicamento(self, nombre):
        self.medicamentos = [
            med for med in self.medicamentos if med.nombre != nombre.strip()
        ]

    def obtener_inventario(self):
        return [(med.nombre, med.cantidad, med.unitad) for med in self.medicamentos]

    def __str__(self):
        if not self.medicamentos:
            return "El inventario está vacío."
        return "\n".join(str(med) for med in self.medicamentos)
