from django.contrib import admin
from .models import TbHistorialclinico

class TbHistorialclinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'idcita', 'motivo', 'historiadeldolor', 'interpretacionradiografica', 'observacion')  # Campos a mostrar
    search_fields = ('motivo', 'historiadeldolor', 'interpretacionradiografica')  # Permite buscar por estos campos
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbHistorialclinico, TbHistorialclinicoAdmin)
