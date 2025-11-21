from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class reseña(models.Model):
    producto = models.ForeignKey('api3.producto', on_delete=models.CASCADE)
    usuario = models.ForeignKey('api1.usuario', on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña: Producto {self.producto.nombre}, Usuario {self.usuario.nombre}, Calificación {self.calificacion}, Comentario {self.comentario}, Fecha {self.fecha_creacion}"
