from django.db import models

class carritocompras(models.Model):
    usuario = models.ForeignKey('api1.usuario', on_delete=models.CASCADE)
    producto = models.ForeignKey('api3.producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField (default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Carrito de {self.usuario.nombre}: {self.producto.nombre} x {self.cantidad}, agregado el {self.fecha_agregado}"
