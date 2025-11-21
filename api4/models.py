from django.db import models

class provedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    direccion = models.TextField()

def __str__(self):
    return self.nombre
class Meta:
    ordering = ['nombre']
def __str__(self):
    return f"provedor: {self.nombre}, telefono: {self.telefono}, email: {self.email}, direccion: {self.direccion}"
