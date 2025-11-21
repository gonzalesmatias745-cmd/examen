from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api10.views import PagoListCreateView, PagoRetrieveUpdateDestroyView

urlpatterns = [
    path('pagos/', PagoListCreateView.as_view(), name='pago-list-create'),
    path('pagos/<int:pk>/', PagoRetrieveUpdateDestroyView.as_view(), name='pago-detail'),
]