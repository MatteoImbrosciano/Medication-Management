import pytest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

def test_agregar_y_obtener_inventario():
    inventario = Inventario()
    med = Medicamento("Ibuprofeno", 10, 3.0, "mg")
    inventario.agregar_medicamento(med)
    assert inventario.obtener_inventario() == [("Ibuprofeno", 10, "mg")]
