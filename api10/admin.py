from django.contrib import admin
from api10.models import pago

@admin.register(pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'reseña', 'metodo_pago', 'estado_pago')
    search_fields = ('usuario__nombre', 'reseña__producto__nombre', 'metodo_pago', 'estado_pago')
    list_filter = ('estado_pago',)
