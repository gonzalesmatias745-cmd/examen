from rest_framework import generics
from .models import direccionenvio
from .serializers import DireccionEnvioSerializer
from django.shortcuts import render, redirect, get_object_or_404

# API JSON
class DireccionListCreateView(generics.ListCreateAPIView):
    queryset = direccionenvio.objects.all()
    serializer_class = DireccionEnvioSerializer

class DireccionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = direccionenvio.objects.all()
    serializer_class = DireccionEnvioSerializer


# ------------------------
#     VISTAS HTML
# ------------------------

def listar_direcciones(request):
    direcciones = direccionenvio.objects.all()
    return render(request, "direccion/listar.html", {"direcciones": direcciones})

def crear_direccion(request):
    if request.method == "POST":
        usuario_id = request.POST["usuario"]
        direccion = request.POST["direccion"]
        ciudad = request.POST["ciudad"]
        codigo_postal = request.POST["codigo_postal"]
        principal = "principal" in request.POST

        direccionenvio.objects.create(
            usuario_id=usuario_id,
            direccion=direccion,
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            principal=principal
        )
        return redirect("direccion-listar")

    return render(request, "direccion/crear.html")

