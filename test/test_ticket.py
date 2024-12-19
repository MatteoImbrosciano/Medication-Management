import pytest
from medication_management.ticket import Ticket
from datetime import datetime

def test_cargar_ticket_desde_file_esistente():
    
    file_path = "C:/Users/matte/OneDrive/Desktop/Medication-Management/docs/pharmacy_receipt_1.txt"

    ticket = Ticket()
    ticket.cargar_ticket_desde_txt(file_path)

    assert ticket.cliente == "Matteo Imbrosciano"
    assert ticket.fecha == datetime(2024, 2, 15)
    assert ticket.totale == 55.70
    assert len(ticket.medicamentos) == 6
    assert ticket.medicamentos[0].nombre == "Sintrom"
    assert ticket.medicamentos[0].unitad == "1 mg"
    assert ticket.medicamentos[0].precio == 7.50
