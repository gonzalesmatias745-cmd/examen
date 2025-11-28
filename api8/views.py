from rest_framework import generics
from .models import carritocompras
from .serializers import CarritoComprasSerializer
from django.shortcuts import render, redirect, get_object_or_404

# API JSON
class CarritoListCreateView(generics.ListCreateAPIView):
    queryset = carritocompras.objects.all()
    serializer_class = CarritoComprasSerializer

class CarritoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = carritocompras.objects.all()
    serializer_class = CarritoComprasSerializer


# ------------------------
#     VISTAS HTML
# ------------------------

def listar_carrito(request):
    carrito = carritocompras.objects.all()
    return render(request, "carrito/listar.html", {"carrito": carrito})

def agregar_carrito(request):
    if request.method == "POST":
        usuario_id = request.POST["usuario"]
        producto_id = request.POST["producto"]
        cantidad = request.POST["cantidad"]

        carritocompras.objects.create(
            usuario_id=usuario_id,
            producto_id=producto_id,
            cantidad=cantidad
        )
        return redirect("carrito-listar")

    return render(request, "carrito/crear.html")
