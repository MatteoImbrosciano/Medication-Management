from medication_management.medicamento import Medicamento
import pytest

def test_medicamento_valido():
    medicamento = Medicamento("Paracetamol", 10, 5.99)
    assert medicamento.nombre == "Paracetamol"
    assert medicamento.cantidad == 10
    assert medicamento.precio == 5.99

def test_medicamento_invalido():
    with pytest.raises(ValueError):
        Medicamento("Ibuprofeno", 0, 4.99)  # Quantità non valida
