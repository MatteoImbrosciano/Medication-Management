# test/test_ticket.py
import unittest
import os
from medication_management.ticket import Ticket
from medication_management.medicamento import Medicamento

class TestTicket(unittest.TestCase):

    def test_aggiunta_medicamento_ticket(self):
        t = Ticket()
        m = Medicamento("Aspirina", 5, 2.5, "pz")
        t.aggiungi_medicamento(m)
        self.assertEqual(len(t.medicamentos), 1)
        self.assertEqual(t.medicamentos[0].nombre, "Aspirina")

    def test_genera_txt(self):
        t = Ticket()
        m = Medicamento("Aspirina", 5, 2.5, "pz")
        t.aggiungi_medicamento(m)
        nome_file = "test_ricevuta.txt"
        
        if os.path.exists(nome_file):
            os.remove(nome_file)

        t.genera_txt("Mario Rossi", nome_file)
        self.assertTrue(os.path.exists(nome_file))

        with open(nome_file, "r", encoding="utf-8") as f:
            contenuto = f.read()

        self.assertIn("Aspirina", contenuto)
        self.assertIn("Mario Rossi", contenuto)
        self.assertIn("Pharmacy Receipt - Farmacia Italia", contenuto)

        os.remove(nome_file)


if __name__ == "__main__":
    unittest.main()
