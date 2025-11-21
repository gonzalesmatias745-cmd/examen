from django.test import TestCase
from .models import carritocompras
from .serializers import CarritoComprasSerializer

class CarritoComprasModelTest(TestCase):
    def setUp(self):
        self.carrito = carritocompras.objects.create(
            usuario_id=1,
            producto_id=1,
            cantidad=2
        )
    carritocompras.objects.create(
            usuario_id=2,
            producto_id=2,
            cantidad=1
        )
    carritocompras.objects.create(
            usuario_id=1,
            producto_id=3,
            cantidad=5
        )
    carritocompras.objects.create(
            usuario_id=3,
            producto_id=1,
            cantidad=3
        )
    carritocompras.objects.create(
            usuario_id=2,
            producto_id=3,
            cantidad=4
        )
    def test_carrito_creation(self):
        total_carritos = carritocompras.objects.count()
        self.assertEqual(total_carritos, 5)
