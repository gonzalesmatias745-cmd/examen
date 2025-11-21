from django.contrib import admin
from api8.models import carritocompras

@admin.register(carritocompras)
class CarritoComprasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'cantidad', 'fecha_agregado')
    search_fields = ('usuario__nombre', 'producto__nombre')
    list_filter = ('fecha_agregado',)
    ordering = ('-fecha_agregado',)
    search_fields = ('usuario__nombre', 'producto__nombre')
    
