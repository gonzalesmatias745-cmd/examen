from django.test import TestCase
from .models import direccionenvio
from .serializers import DireccionEnvioSerializer

class DireccionEnvioSerializerTest(TestCase):
    def setUp(self):
        self.direccion= direccionenvio.objects.create(
            usuario_id=1,
            direccion="Calle Falsa 123",
            ciudad="Springfield",
            codigo_postal="12345",
            principal=True
        )
        direccionenvio.objects.create(
            usuario_id=2,
            direccion="Avenida Siempre Viva 742",
            ciudad="Shelbyville",
            codigo_postal="67890",
            principal=False
        )
        direccionenvio.objects.create(
            usuario_id=3,
            direccion="Boulevard de los Sueños Rotos 456",
            ciudad="Ogdenville",
            codigo_postal="54321",
            principal=True
        )
        direccionenvio.objects.create(
            usuario_id=4,
            direccion="Plaza Mayor 1",
            ciudad="North Haverbrook",
            codigo_postal="98765",
            principal=False
        )
        direccionenvio.objects.create(
            usuario_id=5,
            direccion="Camino Real 789",
            ciudad="Capital City",
            codigo_postal="11223",
            principal=True
        )
    def test_direccionenvio_count(self):
        total_direcciones = direccionenvio.objects.count()
        self.assertEqual(total_direcciones, 5)