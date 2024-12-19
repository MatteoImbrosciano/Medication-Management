import locale
from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from .medicamento import Medicamento

@dataclass
class Ticket:
    cliente: str = None
    fecha: datetime = None
    medicamentos: List[Medicamento] = field(default_factory=list)
    totale: float = None

    def cargar_ticket_desde_txt(self, file_path: str):
        locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')  # Imposta la locale italiana

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        self.medicamentos.clear()  # Pulisce la lista dei medicamenti prima del caricamento

        for line in lines:
            line = line.strip()

            if line.startswith("Cliente:"):
                self.cliente = line.split(":", 1)[1].strip()

            elif line.startswith("Data:"):
                self.fecha = datetime.strptime(line.split(":", 1)[1].strip(), "%d %B %Y")

            elif line.startswith("Totale:"):
                self.totale = float(line.split(":", 1)[1].strip().replace("€", "").replace(",", "."))

            elif "|" in line and not line.startswith("Articolo"):
                parts = line.split("|")
                if len(parts) == 4:
                    nombre = parts[0].strip()
                    cantidad_info = parts[1].strip().split()
                    cantidad = float(cantidad_info[0])
                    unitad = cantidad_info[1] if len(cantidad_info) > 1 else ''
                    precio = float(parts[3].strip().replace("€", "").replace(",", "."))
                    medicamento = Medicamento(nombre, cantidad, precio, unitad)
                    self.medicamentos.append(medicamento)
