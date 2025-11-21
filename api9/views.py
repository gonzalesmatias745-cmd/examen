from django.shortcuts import render
from rest_framework import generics
from api9.models import direccionenvio
from api9.serializers import DireccionEnvioSerializer

class DireccionEnvioListCreateView(generics.ListCreateAPIView):
    queryset = direccionenvio.objects.all()
    serializer_class = DireccionEnvioSerializer
class DireccionEnvioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = direccionenvio.objects.all()
    serializer_class = DireccionEnvioSerializer
