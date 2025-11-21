from django.urls import path
from .views import UsuarioListCreateView, UsuarioRetrieveUpdateDestroyView

urlpatterns = [
    path('usuarios/', UsuarioListCreateView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
]