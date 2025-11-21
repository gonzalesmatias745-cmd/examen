from django.db import models

class pago(models.Model):
    METODOS_PAGO = [
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
        ('efectivo', 'Efectivo'),
    ]
    ESTADOS_PAGO = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('fallido', 'Fallido'),
    ]
    usuario = models.ForeignKey('api1.usuario', on_delete=models.CASCADE)
    reseña = models.ForeignKey('api7.reseña', on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='pendiente')

    def __str__(self):
        return f"Pago de {self.usuario.nombre} para la reseña {self.reseña.id} - Metodo: {self.metodo_pago}, Estado: {self.estado_pago}"
