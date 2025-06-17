import unittest
from pos import PuntoDeVenta

class TestPuntoDeVenta(unittest.TestCase):
    def test_agregar_producto(self):
        pdv = PuntoDeVenta()
        pdv.agregar_producto("manzana", 1.0)
        self.assertIn("manzana", pdv.productos)

if __name__ == "__main__":
    unittest.main()
