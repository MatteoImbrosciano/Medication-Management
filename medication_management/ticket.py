from medication_management.medicamento import Medicamento
from datetime import datetime

class Ticket:
    def __init__(self):
        self.medicamentos = []
        self.fecha = datetime.now()

    def agregar_medicamento(self, medicamento: Medicamento):
        if not isinstance(medicamento, Medicamento):
            raise TypeError("Solo se pueden agregar instancias de Medicamento")
        self.medicamentos.append(medicamento)

    def generar_ticket(self) -> str:
        ticket = f"Ticket - Farmacia Italia\nFecha: {self.fecha.strftime('%d %B %Y')}\n\n"
        if not self.medicamentos:
            ticket += "Ticket vacío."
            return ticket

        detalles = "\n".join(
            [f"{m.nombre} x{m.unitad} = {m.unitad * m.precio}€" for m in self.medicamentos]
        )
        total = sum(m.unitad * m.precio for m in self.medicamentos)
        ticket += f"Artículos:\n{detalles}\n\nTotal: {total}€"
        return ticket
