import locale
from datetime import datetime
from medication_management.medicamento import Medicamento

class Ticket:
    def __init__(self):
        self.cliente = None
        self.fecha = None
        self.medicamentos = []
        self.totale = None

    def cargar_ticket_desde_txt(self, file_path):

        locale.setlocale(locale.LC_TIME, 'it_IT')  

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line.startswith("Cliente:"):
                self.cliente = line.replace("Cliente:", "").strip()

            elif line.startswith("Data:"):
                self.fecha = datetime.strptime(
                    line.replace("Data:", "").strip(), "%d %B %Y"
                )

            elif line.startswith("Totale:"):
                self.totale = float(line.replace("Totale:", "").strip().replace("€", ""))

            elif "|" in line and not line.startswith("Articolo"):
                parts = line.split("|")
                if len(parts) == 4:
                    nombre = parts[0].strip()
                    cantidad = parts[1].strip()
                    unitad = parts[2].strip()
                    precio = float(parts[3].strip().replace("€", ""))
                    medicamento = Medicamento(nombre, 1, precio, cantidad)
                    self.medicamentos.append(medicamento)
    
