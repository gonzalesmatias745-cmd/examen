from django.db import models

class direccionenvio(models.Model):
    usuario = models.ForeignKey('api1.usuario', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    principal = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.direccion}, {self.ciudad} - {self.usuario.nombre}"
