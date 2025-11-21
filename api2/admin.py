from django.contrib import admin
from api2.models import categoria

@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre',)
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)
