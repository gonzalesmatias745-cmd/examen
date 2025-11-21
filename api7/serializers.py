from rest_framework import serializers
from api7.models import reseña
class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reseña
        fields = ['id', 'producto', 'usuario', 'calificacion', 'comentario', 'fecha_reseña']