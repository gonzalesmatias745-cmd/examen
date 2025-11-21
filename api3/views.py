from django.shortcuts import render
from rest_framework import generics
from api3.models import producto
from api3.serializers import ProductoSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer

