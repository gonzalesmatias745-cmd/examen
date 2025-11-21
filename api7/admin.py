from django.contrib import admin
from api7.models import reseña

@admin.register(reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'calificacion', 'comentario', 'fecha_creacion')
    search_fields = ('producto__nombre', 'usuario__nombre', 'comentario')
    list_filter = ('calificacion', 'fecha_creacion')
    ordering = ('-fecha_creacion',)
    search_fields = ('producto__nombre', 'usuario__nombre', 'comentario')
