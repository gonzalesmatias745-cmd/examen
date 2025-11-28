from rest_framework import serializers
from .models import pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = ['id', 'usuario', 'fecha_pedido', 'estado', 'total', 'direccion_envio']