from django.contrib import admin
from .models import TbPaciente

class TbPacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombrecompleto', 'cedula', 'edad', 'idgenero', 'direccion', 'telefono', 'ocupacion', 'isdeleted')  # Campos a mostrar
    search_fields = ('nombrecompleto', 'cedula')  # Permite buscar por nombre completo y cédula
    list_filter = ('idgenero', 'isdeleted')  # Filtros por género y estado de eliminación
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbPaciente, TbPacienteAdmin)
