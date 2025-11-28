from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.listar_categorias, name='categoria-listar'),
    path('categorias/crear/', views.crear_categoria, name='categoria-crear'),
]
