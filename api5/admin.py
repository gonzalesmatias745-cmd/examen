from django.contrib import admin
from api5.models import pedido
@admin.register(pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha_pedido', 'estado', 'total')
    list_filter = ('estado', 'fecha_pedido')
    ordering = ('-fecha_pedido',)
    