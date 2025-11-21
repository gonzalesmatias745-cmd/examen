from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api7.views import ReseñaListCreateView, ReseñaRetrieveUpdateDestroyView

urlpatterns = [
    path('reseñas/', ReseñaListCreateView.as_view(), name='reseña-list-create'),
    path('reseñas/<int:pk>/', ReseñaRetrieveUpdateDestroyView.as_view(), name='reseña-detail'),
]
