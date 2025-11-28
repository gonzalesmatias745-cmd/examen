from django.urls import path
from .views import (
    listar_carrito,
    agregar_carrito,
    CarritoListCreateView,
    CarritoRetrieveUpdateDestroyView
)

urlpatterns = [
    # HTML
    path('carrito/', listar_carrito, name="carrito-listar"),
    path('carrito/agregar/', agregar_carrito, name="carrito-agregar"),

    # API JSON
    path('api/', CarritoListCreateView.as_view(), name="carrito-api"),
    path('api/<int:pk>/', CarritoRetrieveUpdateDestroyView.as_view(), name="carrito-api-detalle"),
]
