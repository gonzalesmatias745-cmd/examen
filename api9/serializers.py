from rest_framework import serializers
from api9.models import direccionenvio

class DireccionEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = direccionenvio
        fields = ['id', 'usuario', 'direccion', 'ciudad', 'codigo_postal', 'pais']