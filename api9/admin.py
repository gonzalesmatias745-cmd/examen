from django.contrib import admin
from api9.models import direccionenvio

@admin.register(direccionenvio)
class DireccionEnvioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'direccion', 'ciudad', 'codigo_postal', 'principal')
    search_fields = ('usuario__nombre', 'direccion', 'ciudad', 'codigo_postal')
    list_filter = ('principal',)
    ordering = ('-usuario__nombre',)
    search_fields = ('usuario__nombre', 'direccion', 'ciudad', 'codigo_postal')
    
