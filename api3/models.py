from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.FloatField()  # ← YA NO USA DECIMALES ESTRICTOS
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return (
            f"producto: {self.nombre}, descripcion: {self.descripcion}, "
            f"precio: {self.precio}, creado el {self.fecha_creacion}, activo: {self.activo}"
        )

