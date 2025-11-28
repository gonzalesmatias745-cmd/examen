from django.urls import path
from . import views

urlpatterns = [
    
    path('proveedores/', views.listar_proveedores, name='proveedor-listar'),
    path('proveedores/crear/', views.crear_proveedor, name='proveedor-crear'),

    
    path('api/', views.ProveedorListCreateView.as_view(), name='proveedor-api'),
    path('api/<int:pk>/', views.ProveedorRetrieveUpdateDestroyView.as_view(), name='proveedor-api-detalle'),
]

