from rest_framework import serializers
from api6.models import detallespedido
class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = detallespedido
        fields = ['id', 'pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal']