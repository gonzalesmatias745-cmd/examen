from rest_framework import serializers
from api4.models import provedor
class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = provedor
        fields = ['id', 'nombre', 'direccion', 'telefono', 'email']