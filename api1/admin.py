from django.contrib import admin
from api1.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_registro', 'telefono', 'activo')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('activo', 'fecha_registro')
    ordering = ('-fecha_registro',)
    search_fields = ('nombre', 'email', 'telefono')
    
