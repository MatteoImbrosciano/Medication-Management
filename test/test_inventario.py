from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento
import pytest

def test_inventario_aggiungi_medicamento():
    # Crea un inventario
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 5, 2.50, "100 mg")
    
    # Aggiungi un farmaco
    inventario.medicamentos.append(medicamento)
    
    # Verifica che il farmaco sia stato aggiunto
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0].nombre == "Aspirina"
    assert inventario.medicamentos[0].cantidad == 5
    assert inventario.medicamentos[0].precio == 2.50
    assert inventario.medicamentos[0].unidad == "100 mg"

def test_inventario_rimuovi_medicamento():
    # Crea un inventario
    inventario = Inventario()
    medicamento = Medicamento("Ibuprofeno", 10, 3.50, "200 mg")
    
    # Aggiungi e poi rimuovi un farmaco
    inventario.medicamentos.append(medicamento)
    inventario.medicamentos.remove(medicamento)
    
    # Verifica che il farmaco sia stato rimosso
    assert len(inventario.medicamentos) == 0

def test_inventario_lista_medicamenti():
    # Crea un inventario
    inventario = Inventario()
    
    # Aggiungi due farmaci
    medicamento1 = Medicamento("Paracetamol", 10, 5.99, "500 mg")
    medicamento2 = Medicamento("Aspirina", 5, 2.50, "100 mg")
    inventario.medicamentos.extend([medicamento1, medicamento2])
    
    # Verifica che i farmaci siano stati aggiunti
    assert len(inventario.medicamentos) == 2
    assert inventario.medicamentos[0].nombre == "Paracetamol"
    assert inventario.medicamentos[1].nombre == "Aspirina"
    assert inventario.medicamentos[0].unidad == "500 mg"
    assert inventario.medicamentos[1].unidad == "100 mg"
