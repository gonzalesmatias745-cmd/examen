from django.test import TestCase
from .models import provedor

class ProvedorModelTest(TestCase):
    def setUp(self):
        self.provedor = provedor.objects.create(
            nombre="Proveedor Test",
            telefono="123456789",
            email="sisi@gmail.com",
            direccion="Calle Falsa 123"
        )
        provedor.objects.create(
            nombre="Otro Proveedor",
            telefono="987654321",
            email="aa@gmail.com",
            direccion="Avenida Siempre Viva 742"
        )
        provedor.objects.create(
            nombre="Proveedor 3",
            telefono="555555555",
            email="w@gmail.com",
            direccion="Boulevard de los Sueños Rotos 456"
        )
        provedor.objects.create(
            nombre="Proveedor 4",
            telefono="444444444",
            email="siu@gmail.com",
            direccion="Plaza Mayor 1"
        )
        provedor.objects.create(
            nombre="Proveedor 5",
            telefono="333333333",
            email="5perro@gmail.com",
            direccion="Camino Real 99"
        )
    def test_provedor_creation(self):
        total_provedores = provedor.objects.count()
        self.assertEqual(total_provedores, 5)