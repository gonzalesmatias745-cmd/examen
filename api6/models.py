from django.db import models

class DetallePedido(models.Model):
    pedido = models.ForeignKey('api5.pedido', on_delete=models.CASCADE)
    producto = models.ForeignKey('api3.producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['pedido']

    def __str__(self):
        return (
            f"DetallePedido: Pedido {self.pedido.id} | "
            f"Producto {self.producto.nombre} | "
            f"Cantidad {self.cantidad} | "
            f"Subtotal {self.subtotal}"
        )
