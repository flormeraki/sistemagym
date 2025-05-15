# test_recupero_contraseña.py
import unittest
from clases.recupero_contraseña import RecuperoContraseña
from datetime import datetime, timedelta

class TestRecuperoContraseña(unittest.TestCase):

    def setUp(self):
        self.recupero = RecuperoContraseña(usuario_id=1)
        self.recupero.generar_token()
        self.token_generado = self.recupero.get_token()

    def test_token_generado(self):
        self.assertIsNotNone(self.token_generado)
        self.assertFalse(self.recupero.fue_usado())

    def test_validar_token_correcto(self):
        self.assertTrue(self.recupero.validar_token(self.token_generado))

    def test_validar_token_usado(self):
        self.recupero.marcar_usado()
        self.assertFalse(self.recupero.validar_token(self.token_generado))

    def test_validar_token_incorrecto(self):
        self.assertFalse(self.recupero.validar_token("token-falso"))

if __name__ == '__main__':
    unittest.main()
