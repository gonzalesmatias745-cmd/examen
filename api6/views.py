from django.shortcuts import render
from rest_framework import generics
from api6.models import detallespedido
from api6.serialeizers import DetallePedidoSerializer

class DetallePedidoListCreateView(generics.ListCreateAPIView):
    queryset = detallespedido.objects.all()
    serializer_class = DetallePedidoSerializer

class DetallePedidoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = detallespedido.objects.all()
    serializer_class = DetallePedidoSerializer

