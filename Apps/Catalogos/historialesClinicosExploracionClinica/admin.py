from django.contrib import admin
from .models import TbHistorialclinicotbExploracionclinica

class TbHistorialclinicotbExploracionclinicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'idhistorialclinico', 'idexploracionclinica')  # Campos a mostrar
    search_fields = ('idhistorialclinico__motivo', 'idexploracionclinica__tipo')  # Permite buscar por estos campos relacionados
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbHistorialclinicotbExploracionclinica, TbHistorialclinicotbExploracionclinicaAdmin)
