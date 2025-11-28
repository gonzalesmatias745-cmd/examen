from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='usuario-listar'),
    path('usuarios/crear/', views.crear_usuario, name='usuario-crear'),
]
