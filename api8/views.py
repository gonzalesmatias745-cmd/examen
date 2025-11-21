from django.shortcuts import render
from rest_framework import generics
from api8.models import carritocompras
from api8.serializers import CarritoComprasSerializer

class CarritoComprasListCreateView(generics.ListCreateAPIView):
    queryset = carritocompras.objects.all()
    serializer_class = CarritoComprasSerializer
class CarritoComprasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = carritocompras.objects.all()
    serializer_class = CarritoComprasSerializer
