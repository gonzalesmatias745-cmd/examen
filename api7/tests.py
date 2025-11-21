from django.test import TestCase
from .models import reseña
from .serializers import ReseñaSerializer

class ReseñaSerializerTest(TestCase):
    def setUp(self):
     self.reseña=reseña.objects.create(
            producto_id=1,
            usuario_id=1,
            calificacion=5,
            comentario="Excelente producto"
        )
     reseña.objects.create(
            producto_id=2,
            usuario_id=2,
            calificacion=4,
            comentario="Muy bueno"
        )
     reseña.objects.create(
            producto_id=1,
            usuario_id=3,
            calificacion=3,
            comentario="Aceptable"
        )
     reseña.objects.create(
            producto_id=3,
            usuario_id=1,
            calificacion=2,
            comentario="No me gustó"
        )
     reseña.objects.create(
            producto_id=2,
            usuario_id=3,
            calificacion=1,
            comentario="Muy mala calidad"
        )
    def test_reseña_serialization(self):
        serializer = ReseñaSerializer(self.reseña)
        expected_data = {
            'id': self.reseña.id,
            'producto': self.reseña.producto_id,
            'usuario': self.reseña.usuario_id,
            'calificacion': self.reseña.calificacion,
            'comentario': self.reseña.comentario,
            'fecha_creacion': self.reseña.fecha_creacion.isoformat().replace('+00:00', 'Z'),
        }
        self.assertEqual(serializer.data, expected_data)
    def test_reseña_count(self):
        total_reseñas = reseña.objects.count()
        self.assertEqual(total_reseñas, 5)
