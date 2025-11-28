from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Proveedor
from .serializers import ProveedorSerializer


def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores/listar.html', {'proveedores': proveedores})

def crear_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion=request.POST['direccion']
        )
        return redirect('proveedor-listar')

    return render(request, 'proveedores/crear.html')



class ProveedorListCreateView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
