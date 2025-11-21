from django.test import TestCase
from .models import pago
from .serializers import PagoSerializer

class PagoModelTest(TestCase):
    def setUp(self):
        self.pago = pago.objects.create(
            usuario_id=1,
            monto=100.50,
            metodo_pago='Tarjeta de Crédito'
        )
        pago.objects.create(
            usuario_id=2,
            monto=250.00,
            metodo_pago='efectivo'
        )
        pago.objects.create(
            usuario_id=3,
            monto=75.25,
            metodo_pago='PayPal'
        )
        pago.objects.create(
            usuario_id=4,
            monto=300.00,
            metodo_pago='Transferencia Bancaria'
        )
        pago.objects.create(
            usuario_id=5,
            monto=150.75,
            metodo_pago='Tarjeta de Débito'
        )

    def test_pago_creation(self):
        total_pagos = pago.objects.count()
        self.assertEqual(total_pagos, 5)
