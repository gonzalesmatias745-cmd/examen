from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api8.views import CarritoComprasListCreateView, CarritoComprasRetrieveUpdateDestroyView

urlpatterns = [
    path('carritocompras/', CarritoComprasListCreateView.as_view(), name='carrito-compras-list-create'),
    path('carritocompras/<int:pk>/', CarritoComprasRetrieveUpdateDestroyView.as_view(), name='carrito-compras-detail'),
]