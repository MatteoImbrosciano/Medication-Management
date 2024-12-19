# test_inventario.py
import pytest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

def test_aggiunta_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    inventario.agregar_medicamento(medicamento)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0] == medicamento

def test_aggiunta_medicamento_duplicato():
    inventario = Inventario()
    medicamento1 = Medicamento("Aspirina", 100, 4.50, "mg")
    medicamento2 = Medicamento("Aspirina", 50, 4.50, "mg")
    inventario.agregar_medicamento(medicamento1)
    inventario.agregar_medicamento(medicamento2)
    assert len(inventario.medicamentos) == 1
    assert inventario.medicamentos[0].cantidad == 150

def test_rimozione_medicamento():
    inventario = Inventario()
    medicamento = Medicamento("Aspirina", 100, 4.50, "mg")
    inventario.agregar_medicamento(medicamento)
    inventario.eliminar_medicamento("Aspirina")
    assert len(inventario.medicamentos) == 0

def test_ottenere_inventario():
    inventario = Inventario()
    medicamento1 = Medicamento("Aspirina", 100, 4.50, "mg")
    medicamento2 = Medicamento("Ibuprofene", 200, 8.00, "mg")
    inventario.agregar_medicamento(medicamento1)
    inventario.agregar_medicamento(medicamento2)
    result = inventario.obtener_inventario()
    assert len(result) == 2
    assert ("Aspirina", 100, "mg") in result
    assert ("Ibuprofene", 200, "mg") in result
