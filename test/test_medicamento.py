import pytest
from medication_management.medicamento import Medicamento

def test_crear_medicamento_valido():
    med = Medicamento("Paracetamol", 10, 5.0, "mg")
    assert med.nombre == "Paracetamol"
    assert med.cantidad == 10
    assert med.precio == 5.0
    assert med.unitad == "mg"

def test_crear_medicamento_invalido():
    with pytest.raises(ValueError):
        Medicamento("", 10, 5.0, "mg")
    with pytest.raises(ValueError):
        Medicamento("Paracetamol", -1, 5.0, "mg")
    with pytest.raises(ValueError):
        Medicamento("Paracetamol", 10, -5.0, "mg")
