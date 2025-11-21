from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api9.views import DireccionEnvioListCreateView, DireccionEnvioRetrieveUpdateDestroyView

urlpatterns = [
    path('direcciones-envio/', DireccionEnvioListCreateView.as_view(), name='direccion-envio-list-create'),
    path('direcciones-envio/<int:pk>/', DireccionEnvioRetrieveUpdateDestroyView.as_view(), name='direccion-envio-detail'),
]
