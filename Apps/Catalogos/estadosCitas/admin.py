from django.contrib import admin
from .models import TbEstadocita

class TbEstadocitaAdmin(admin.ModelAdmin):
    list_display = ('idestadocita', 'nombreestado')  # Campos a mostrar en la lista de administración
    search_fields = ('nombreestado',)  # Permite buscar por el nombre del estado
    ordering = ('idestadocita',)  # Ordenar por ID de estado de cita

admin.site.register(TbEstadocita, TbEstadocitaAdmin)
