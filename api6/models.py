from django.db import models

class detallespedido(models.Model):
    pedido = models.ForeignKey('api5.pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('api3.producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"DetallePedido: Pedido {self.pedido.id}, Producto {self.producto.nombre}, Cantidad {self.cantidad}, Precio Unitario {self.precio_unitario}, Subtotal {self.subtotal}"
        