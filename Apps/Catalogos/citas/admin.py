from django.contrib import admin
from .models import TbCita

class TbCitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'idpaciente', 'fecha', 'idestadocita', 'horaentrada', 'horasalida')  # Campos a mostrar en la lista de administración
    search_fields = ('idpaciente__nombre', 'idestadocita__nombreestado')  # Permite buscar por el nombre del paciente y estado de cita
    list_filter = ('idestadocita', 'fecha')  # Filtros por estado de cita y fecha
    ordering = ('id',)  # Ordenar por id

admin.site.register(TbCita, TbCitaAdmin)
