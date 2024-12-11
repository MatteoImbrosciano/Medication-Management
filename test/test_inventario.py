import unittest
from medication_management.inventario import Inventario
from medication_management.medicamento import Medicamento

class TestInventario(unittest.TestCase):

    def test_aggiunta_medicamento(self):
        inv = Inventario()
        m = Medicamento("Aspirina", 10, 2.5, "pz")
        inv.medicamentos.append(m)
        self.assertEqual(len(inv.medicamentos), 1)
        self.assertEqual(inv.medicamentos[0].nombre, "Aspirina")


if __name__ == "__main__":
    unittest.main()
