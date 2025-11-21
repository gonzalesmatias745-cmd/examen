from django.test import TestCase
from .models import detallespedido
class DetallePedidoModelTest(TestCase):
    def setUp(self):
        self.detalle = detallespedido.objects.create(
            pedido_id=1,
            producto_id=1,
            cantidad=2,
            precio_unitario=50.00,
            subtotal=100.00
        )
        detallespedido.objects.create(
            pedido_id=1,
            producto_id=2,
            cantidad=1,
            precio_unitario=75.00,
            subtotal=75.00
        )
        detallespedido.objects.create(
            pedido_id=2,
            producto_id=1,
            cantidad=3,
            precio_unitario=50.00,
            subtotal=150.00
        )
        detallespedido.objects.create(
            pedido_id=2,
            producto_id=3,
            cantidad=2,
            precio_unitario=100.00,
            subtotal=200.00
        )
        detallespedido.objects.create(
            pedido_id=3,
            producto_id=2,
            cantidad=1,
            precio_unitario=75.00,
            subtotal=75.00
        )
    def test_detalle_creation(self):
        total_detalles = detallespedido.objects.count()
        self.assertEqual(total_detalles, 5)
