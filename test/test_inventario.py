from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

def test_inventario_aggiungi_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 5, 2.50)
    inventario.medicamentos.append(medicamento)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0].nombre == "Aspirina"

def test_inventario_rimuovi_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Ibuprofeno", 10, 3.50)
    inventario.medicamentos.append(medicamento)
    inventario.medicamentos.remove(medicamento)
    assert len(inventario.medicamentos) == 0

def test_inventario_lista_medicamentos():
    inventario = Inventario()
    medicamento1 = Medicamento("Paracetamol", 10, 5.99)
    medicamento2 = Medicamento("Aspirina", 5, 2.50)
    inventario.medicamentos.extend([medicamento1, medicamento2])
    assert len(inventario.medicamentos) == 2
    assert inventario.medicamentos[1].nombre == "Aspirina"
