from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api2.views import CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),
]
