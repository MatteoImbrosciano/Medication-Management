import unittest
from medication_management.medicamento import Medicamento

class TestMedicamento(unittest.TestCase):

    def test_creazione_medicamento_valido(self):
        m = Medicamento("Aspirina", 10, 2.5, "pz")
        self.assertEqual(m.nombre, "Aspirina")
        self.assertEqual(m.cantidad, 10)
        self.assertEqual(m.precio, 2.5)
        self.assertEqual(m.unidad, "pz")

    def test_cantidad_invalida(self):
        with self.assertRaises(ValueError) as context:
            Medicamento("Aspirina", -1, 2.5, "pz")
        self.assertIn("La cantidad debe ser un valor numérico positivo", str(context.exception))

    def test_precio_invalido(self):
        with self.assertRaises(ValueError) as context:
            Medicamento("Aspirina", 10, -2.5, "pz")
        self.assertIn("El precio debe ser un valor numérico positivo", str(context.exception))


if __name__ == "__main__":
    unittest.main()
