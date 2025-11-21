from rest_framework import serializers
from api2.models import categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion']
