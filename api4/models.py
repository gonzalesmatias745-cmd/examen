from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.email})"

