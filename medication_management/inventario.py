from medication_management.medicamento import Medicamento

class Inventario:
    def __init__(self):
        self.medicamentos = []

    def agregar_medicamento(self, medicamento: Medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("Solo se pueden agregar instancias de Medicamento")
        self.medicamentos.append(medicamento)

    def visualizar_inventario(self) -> str:
        if not self.medicamentos:
            return "Inventario vacío."
        inventario = "\n".join(
            [f"{m.nombre}: Cantidad={m.cantidad}, Precio={m.precio}€, Unitad={m.unitad}" for m in self.medicamentos]
        )
        return inventario
