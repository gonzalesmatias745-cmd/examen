from rest_framework import serializers
from api3.models import producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'categoria']
        