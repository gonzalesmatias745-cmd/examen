from django.urls import path
from .views import (
    listar_pedidos,
    crear_pedido,
    PedidoListCreateView,
    PedidoRetrieveUpdateDestroyView
)

urlpatterns = [
    # HTML
    path('pedidos/', listar_pedidos, name='pedido-listar'),
    path('pedidos/crear/', crear_pedido, name='pedido-crear'),

    # API JSON
    path('api/', PedidoListCreateView.as_view(), name='pedido-api'),
    path('api/<int:pk>/', PedidoRetrieveUpdateDestroyView.as_view(), name='pedido-api-detalle'),
]

