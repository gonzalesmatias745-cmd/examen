from rest_framework import serializers
from api10.models import pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ['id', 'pedido', 'metodo_pago', 'estado_pago', 'monto', 'fecha_pago']