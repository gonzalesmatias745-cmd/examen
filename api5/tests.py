from django.test import TestCase
from .models import pedido
from .serializers import PedidoSerializer
class PedidoSerializerTest(TestCase):
    def setUp(self):
        self.pedido = pedido.objects.create (
            cliente='Juan Perez',
            direccion_envio='Calle Falsa 123',
            fecha_pedido='2024-06-01',
            total=150.75
        )
        self.pedido= pedido.objects.create(
            cliente='Juan Perez',
            direccion_envio='Calle Falsa 123',
            fecha_pedido='2024-06-01',
            total=150.75
        )
        self.pedido = pedido.objects.create(
            cliente='Ana Gomez',
            direccion_envio='Avenida Siempre Viva 456',
            fecha_pedido='2024-06-02',
            total=200.00
        )
        self.pedido = pedido.objects.create(
            cliente='Luis Martinez',
            direccion_envio='Boulevard Central 789',
            fecha_pedido='2024-06-03',
            total=300.50
        )
        self.pedido = pedido.objects.create(
            cliente='Maria Lopez',
            direccion_envio='Plaza Mayor 101',
            fecha_pedido='2024-06-04',
            total=120.00
        )
    def test_pedido_serialization(self):
        pedidos = pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        self.assertEqual(len(serializer.data), 5)