from django.urls import path
from .views import (
    listar_direcciones,
    crear_direccion,
    DireccionListCreateView,
    DireccionRetrieveUpdateDestroyView
)

urlpatterns = [
    # HTML
    path('direcciones/', listar_direcciones, name='direccion-listar'),
    path('direcciones/crear/', crear_direccion, name='direccion-crear'),

    # API JSON
    path('api/', DireccionListCreateView.as_view(), name='direccion-api'),
    path('api/<int:pk>/', DireccionRetrieveUpdateDestroyView.as_view(), name='direccion-api-detalle'),
]
