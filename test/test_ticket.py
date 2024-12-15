import pytest
from medication_management.ticket import Ticket
from medication_management.medicamento import Medicamento
from datetime import datetime

def test_ticket_iniziale():
    ticket = Ticket()
    assert ticket.medicamentos == []
    assert isinstance(ticket.fecha, datetime)

def test_agregar_medicamento_al_ticket():
    ticket = Ticket()
    medicamento = Medicamento(nombre="Aspirina", cantidad="10 mg", precio=0.20, unitad=3)
    ticket.agregar_medicamento(medicamento)
    assert len(ticket.medicamentos) == 1
    assert ticket.medicamentos[0] == medicamento

def test_generare_ticket_vuoto():
    ticket = Ticket()
    ticket_generato = ticket.generar_ticket()
    assert "Ticket - Farmacia Italia" in ticket_generato
    assert "Ticket vacío." in ticket_generato

def test_generare_ticket_con_medicamentos():
    ticket = Ticket()
    medicamento1 = Medicamento(nombre="Paracetamolo", cantidad="50 mg", precio=0.50, unitad=2)
    medicamento2 = Medicamento(nombre="Ibuprofeno", cantidad="30 mg", precio=0.30, unitad=1)
    ticket.agregar_medicamento(medicamento1)
    ticket.agregar_medicamento(medicamento2)
    ticket_generato = ticket.generar_ticket()
    assert "Paracetamolo x2 = 1.00€" in ticket_generato  
    assert "Ibuprofeno x1 = 0.30€" in ticket_generato
    assert "Total: 1.30€" in ticket_generato

def test_agregar_medicamento_tipo_errato():
    ticket = Ticket()
    with pytest.raises(TypeError, match="Solo se pueden agregar instancias de Medicamento"):
        ticket.agregar_medicamento(123) 
