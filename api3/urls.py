from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.listar_productos, name='producto-listar'),
    path('productos/crear/', views.crear_producto, name='producto-crear'),
]
