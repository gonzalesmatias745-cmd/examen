from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api6.views import DetallePedidoListCreateView, DetallePedidoRetrieveUpdateDestroyView

urlpatterns = [
    path('detallespedidos/', DetallePedidoListCreateView.as_view(), name='detallepedido-list-create'),
    path('detallespedidos/<int:pk>/', DetallePedidoRetrieveUpdateDestroyView.as_view(), name='detallepedido-detail'),
]
