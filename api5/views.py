from django.shortcuts import render
from rest_framework import generics
from api5.models import pedido
from api5.serializers import PedidoSerializer

class PedidoListCreateView(generics.ListCreateAPIView):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer


