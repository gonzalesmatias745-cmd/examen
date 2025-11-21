from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['-fecha_creacion']
    def __str__(self):
        return f"producto: {self.nombre}, descripcion: {self.descripcion}, precio: {self.precio}, creado el {self.fecha_creacion}, activo: {self.activo}"

