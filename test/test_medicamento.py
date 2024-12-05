from medication_management.medicamento import Medicamento
import pytest

def test_medicamento_valido():
    medicamento = Medicamento("Paracetamol", 10, 5.99, "500 mg")
    assert medicamento.nombre == "Paracetamol"
    assert medicamento.cantidad == 10
    assert medicamento.precio == 5.99
    assert medicamento.unidad == "500 mg"

def test_medicamento_invalido():
    # Test quantità non valida
    with pytest.raises(ValueError):
        Medicamento("Ibuprofeno", 0, 4.99, "200 mg")
    
    # Test prezzo non valido
    with pytest.raises(ValueError):
        Medicamento("Ibuprofeno", 10, -4.99, "200 mg")
