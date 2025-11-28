from django.contrib import admin
from api6.models import DetallePedido
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario', 'subtotal')
    search_fields = ('pedido__id', 'producto__nombre')
    list_filter = ('pedido',)
    ordering = ('-pedido',)
    search_fields = ('pedido__id', 'producto__nombre')
