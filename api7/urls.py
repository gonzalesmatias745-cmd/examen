from django.urls import path
from .views import (
    listar_reseñas,
    crear_reseña,
    ReseñaListCreateView,
    ReseñaRetrieveUpdateDestroyView
)

urlpatterns = [
    # HTML
    path("reseñas/", listar_reseñas, name="reseña-listar"),
    path("reseñas/crear/", crear_reseña, name="reseña-crear"),

    # API JSON
    path("api/", ReseñaListCreateView.as_view(), name="reseña-api"),
    path("api/<int:pk>/", ReseñaRetrieveUpdateDestroyView.as_view(), name="reseña-api-detalle"),
]
