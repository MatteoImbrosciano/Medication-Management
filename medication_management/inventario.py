from medication_management.medicamento import Medicamento

from pathlib import Path

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

    def importar_desde_txt(self, ruta: str):
        file_path = Path(ruta)
        if not file_path.exists():
            raise FileNotFoundError(f"El archivo {ruta} no existe.")
        contenido = file_path.read_text(encoding='utf-8')
        lineas = contenido.strip().split("\n")
        for linea in lineas:
            partes = linea.split("|")
            if len(partes) == 4:  
                nombre, cantidad, unitad, precio = partes
                medicamento = Medicamento(
                    nombre=nombre.strip(),
                    cantidad=cantidad.strip(),
                    unitad=int(unitad.strip()),
                    precio=float(precio.strip())
                )
                self.agregar_medicamento(medicamento)