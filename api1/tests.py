from django.test import TestCase
from .models import usuario

class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = usuario.objects.create(
            nombre="Juan Perez",
            email="juanito@gmail.com",
            telefono="123456789",
            activo=True
        )
        usuario.objects.create(
            nombre="Ana Gomez",
            email="anita@gmail.com",
            telefono="987654321",
            activo=True
        )
        usuario.objects.create(
            nombre="Luis Martinez",
            email="luisito@gmail.com",
            telefono="555555555",
            activo=False
        )
        usuario.objects.create(
            nombre="Maria Lopez",
            email="marianita@gmail.com",
            telefono="444444444",
            activo=True
        )
        usuario.objects.create(
            nombre="Carlos Sanchez",
            email="carlitos@gmail.com",
            telefono="333333333",
            activo=False
        )
    def test_usuario_creation(self):
      total_usuarios = usuario.objects.count()
      self.assertEqual(total_usuarios, 5)
      