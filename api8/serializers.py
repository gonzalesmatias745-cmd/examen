from rest_framework import serializers
from api8.models import carritocompras

class CarritoComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = carritocompras
        fields = ['id', 'usuario', 'producto', 'cantidad', 'fecha_agregado']
        