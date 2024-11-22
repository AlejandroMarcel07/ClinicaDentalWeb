from django.contrib import admin
from .models import TbRecetamedica

class TbRecetamedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'idcita', 'descripcion')  # Campos a mostrar
    search_fields = ('idcita__id',)  # Permite buscar por ID de la cita
    list_filter = ('idcita',)  # Filtro por ID de la cita
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbRecetamedica, TbRecetamedicaAdmin)
