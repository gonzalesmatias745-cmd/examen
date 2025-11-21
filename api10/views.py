from django.shortcuts import render
from rest_framework import generics
from api10.models import pago
from api10.serializers import PagoSerializer

class PagoListCreateView(generics.ListCreateAPIView):
    queryset = pago.objects.all()
    serializer_class = PagoSerializer

class PagoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = pago.objects.all()
    serializer_class = PagoSerializer
