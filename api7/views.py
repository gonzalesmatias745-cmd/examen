from django.shortcuts import render
from rest_framework import generics
from api7.models import reseña
from api7.serializers import ReseñaSerializer

class ReseñaListCreateView(generics.ListCreateAPIView):
    queryset = reseña.objects.all()
    serializer_class = ReseñaSerializer
class ReseñaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = reseña.objects.all()
    serializer_class = ReseñaSerializer
