from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api4.views import ProvedorListCreateView, ProvedorRetrieveUpdateDestroyView

urlpatterns = [
    path('provedores/', ProvedorListCreateView.as_view(), name='provedor-list-create'),
    path('provedores/<int:pk>/', ProvedorRetrieveUpdateDestroyView.as_view(), name='provedor-detail'),
]
