from rest_framework import generics
from .models import reseña
from .serializers import ReseñaSerializer

# API JSON
class ReseñaListCreateView(generics.ListCreateAPIView):
    queryset = reseña.objects.all()
    serializer_class = ReseñaSerializer


class ReseñaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = reseña.objects.all()
    serializer_class = ReseñaSerializer


# ----- HTML -----
from django.shortcuts import render, redirect
from .models import reseña

def listar_reseñas(request):
    reseñas = reseña.objects.all()
    return render(request, "api7/reseñas_list.html", {"reseñas": reseñas})


def crear_reseña(request):
    if request.method == "POST":
        producto = request.POST.get("producto")
        usuario = request.POST.get("usuario")
        calificacion = request.POST.get("calificacion")
        comentario = request.POST.get("comentario")

        reseña.objects.create(
            producto_id=producto,
            usuario_id=usuario,
            calificacion=calificacion,
            comentario=comentario,
        )
        return redirect("reseña-listar")

    return render(request, "api7/reseñas_create.html")
