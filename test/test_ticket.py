from medication_management.ticket import Ticket
from medication_management.medicamento import Medicamento

def test_ticket_aggiungi_medicamento():
    ticket = Ticket()
    medicamento = Medicamento("Aspirina", 5, 2.50)
    ticket.medicamentos.append(medicamento)
    assert len(ticket.medicamentos) == 1
    assert ticket.medicamentos[0].nombre == "Aspirina"

def test_ticket_data():
    from datetime import date
    ticket = Ticket()
    ticket.fecha = date.today()
    assert ticket.fecha == date.today()

def test_ticket_medicamentos_vuoti():
    ticket = Ticket()
    assert len(ticket.medicamentos) == 0
