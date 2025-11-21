from rest_framework import serializers
from api5.models import pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = ['id', 'cliente', 'fecha_pedido', 'estado', 'total']
        