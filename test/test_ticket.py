from medication_management.ticket import Ticket
from medication_management.medicamento import Medicamento
import pytest
from datetime import date

def test_ticket_aggiungi_medicamento():
    ticket = Ticket()
    medicamento = Medicamento("Aspirina", 5, 2.50, "100 mg")
    ticket.medicamentos.append(medicamento)
    assert len(ticket.medicamentos) == 1
    assert ticket.medicamentos[0].nombre == "Aspirina"
    assert ticket.medicamentos[0].unidad == "100 mg"

def test_ticket_data():
    ticket = Ticket()
    ticket.fecha = date.today()
    assert ticket.fecha == date.today()

def test_ticket_medicamento_invalido():
    with pytest.raises(ValueError):
        Medicamento("Ibuprofeno", 0, 4.99, "200 mg")
