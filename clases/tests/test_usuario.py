# test_usuario.py
import unittest
from clases.usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        # Este método se ejecuta antes de cada test
        self.usuario = Usuario(1, "Ana López", "ana@example.com", "1234")

    def test_nombre(self):
        self.assertEqual(self.usuario.get_nombre(), "Ana López")

    def test_contraseña_correcta(self):
        self.assertTrue(self.usuario.verificar_contraseña("1234"))

    def test_contraseña_incorrecta(self):
        self.assertFalse(self.usuario.verificar_contraseña("0000"))

if __name__ == '__main__':
    unittest.main()
