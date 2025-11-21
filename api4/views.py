from django.shortcuts import render
from rest_framework import generics
from api4.models import provedor
from api4.serializers import ProvedorSerializer

class ProvedorListCreateView(generics.ListCreateAPIView):
    queryset = provedor.objects.all()
    serializer_class = ProvedorSerializer

class ProvedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = provedor.objects.all()
    serializer_class = ProvedorSerializer
