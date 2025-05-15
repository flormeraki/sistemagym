# test_sesion.py
import unittest
from clases.sesion import Sesion
from datetime import datetime

class TestSesion(unittest.TestCase):

    def setUp(self):
        self.sesion = Sesion(usuario_id=1)

    def test_iniciar_sesion(self):
        self.sesion.iniciar_sesion()
        self.assertTrue(self.sesion.esta_activa())
        self.assertIsNotNone(self.sesion.get_hora_inicio())

    def test_cerrar_sesion(self):
        self.sesion.iniciar_sesion()
        self.sesion.cerrar_sesion()
        self.assertFalse(self.sesion.esta_activa())
        self.assertIsNotNone(self.sesion.get_hora_fin())

if __name__ == '__main__':
    unittest.main()
