from django.contrib import admin
from .models import TbHistorialclinicotbTbTratamiento

class TbHistorialclinicotbTbTratamientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'idhistorialclinico', 'idtratamiento', 'precio')  # Campos a mostrar
    search_fields = ('idhistorialclinico__motivo', 'idtratamiento__nombretratamiento')  # Permite buscar por estos campos relacionados
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbHistorialclinicotbTbTratamiento, TbHistorialclinicotbTbTratamientoAdmin)
