from django.test import TestCase
from .models import producto

class ProductoModelTest(TestCase):
    def setUp(self):
        self.producto = producto.objects.create(
            nombre="Laptop",
            descripcion="Una laptop de alta gama.",
            precio=1500.00,
            stock=10
        )
        producto.objects.create(
            nombre="Smartphone",
            descripcion="Un smartphone con buena cámara.",
            precio=800.00,
            stock=25
        )
        producto.objects.create(
            nombre="Tablet",
            descripcion="Una tablet para uso educativo.",
            precio=300.00,
            stock=15
        )
        producto.objects.create(
            nombre="Monitor",
            descripcion="Un monitor 4K para diseño gráfico.",
            precio=400.00,
            stock=8
        )
        producto.objects.create(
            nombre="Teclado",
            descripcion="Un teclado mecánico para gamers.",
            precio=120.00,
            stock=30
        )

    def test_producto_creation(self):
        total_productos = producto.objects.count()
        self.assertEqual(total_productos, 5)