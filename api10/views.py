from rest_framework import viewsets
from .models import pago
from .serializers import PagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = pago.objects.all()
    serializer_class = PagoSerializer
