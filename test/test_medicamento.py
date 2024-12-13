import pytest
from medication_management.medicamento import Medicamento

def test_medicamento_valido():
    medicamento = Medicamento(nombre="Paracetamolo", cantidad="50 mg", precio=0.50, unitad=2)
    assert medicamento.nombre == "Paracetamolo"
    assert medicamento.cantidad == "50 mg"
    assert medicamento.precio == 0.50
    assert medicamento.unitad == 2

def test_medicamento_precio_negativo():
    with pytest.raises(ValueError, match="El precio debe ser un valor numérico positivo"):
        Medicamento(nombre="Ibuprofeno", cantidad="10 mg", precio=-0.30, unitad=1)

def test_medicamento_unitad_negativa():
    with pytest.raises(ValueError, match="El unitad debe ser un valor positivo"):
        Medicamento(nombre="Aspirina", cantidad="20 mg", precio=0.20, unitad=-1)