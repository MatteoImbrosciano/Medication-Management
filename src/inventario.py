from medicamento import Medicamento

class Inventario:
    def __init__(self):
        self.medicamentos = []

    def __str__(self):
        return "\n".join([str(medicamento) for medicamento in self.medicamentos])