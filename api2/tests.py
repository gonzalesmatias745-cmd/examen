from django.test import TestCase
from .models import categoria
class CategoriaModelTest(TestCase):
    def setUp(self):
        self.categoria = categoria.objects.create(
            nombre="Tecnologia",
            descripcion="Categoria relacionada con tecnologia."
        )
        categoria.objects.create(
            nombre="Salud",
            descripcion="Categoria relacionada con salud."
        )
        categoria.objects.create(
            nombre="Educacion",
            descripcion="Categoria relacionada con educacion."
        )
        categoria.objects.create(
            nombre="Deportes",
            descripcion="Categoria relacionada con deportes."
        )
        categoria.objects.create(
            nombre="Arte",
            descripcion="Categoria relacionada con arte."
        )
    def test_categoria_creation(self):
      total_categorias = categoria.objects.count()
      self.assertEqual(total_categorias, 5)