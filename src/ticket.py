from medicamento import Medicamento

class Ticket:
    def __init__(self):
        self.medicamentos = []
    
    def __init__(self,medicamentos):
        self.medicamentos = medicamentos
    
    def __str__(self):
        return "\n".join(str(medicamento) for medicamento in self.medicamentos)