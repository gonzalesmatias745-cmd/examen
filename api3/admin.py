from django.contrib import admin
from api3.models import producto

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)