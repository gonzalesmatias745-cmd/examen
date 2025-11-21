from django.shortcuts import render
from rest_framework import generics
from api2.models import categoria
from api2.serializers import CategoriaSerializer

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer