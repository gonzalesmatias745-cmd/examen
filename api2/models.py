from django.db import models

class categoria(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering=['-fecha_creacion']
def __str__(self):
        return f"categoria: {self.nombre}, descripcion: {self.descripcion}, creada el {self.fecha_creacion}"
    

    