from django.urls import path
from .views import (
    listar_detalles,
    crear_detalle,
    DetallePedidoListCreateView,
    DetallePedidoRetrieveUpdateDestroyView
)

urlpatterns = [
    # HTML
    path('detalles/', listar_detalles, name='detalle-listar'),
    path('detalles/crear/', crear_detalle, name='detalle-crear'),

    # API JSON
    path('api/', DetallePedidoListCreateView.as_view(), name='detalle-api'),
    path('api/<int:pk>/', DetallePedidoRetrieveUpdateDestroyView.as_view(), name='detalle-api-detalle'),
]
