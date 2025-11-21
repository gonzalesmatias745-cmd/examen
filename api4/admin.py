from django.contrib import admin
from api4.models import provedor

@admin.register(provedor)
class ProvedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email')
    search_fields = ('nombre', 'direccion', 'email')
