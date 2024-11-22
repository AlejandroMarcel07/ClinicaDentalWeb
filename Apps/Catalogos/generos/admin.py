from django.contrib import admin
from .models import TbGenero

class TbGeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'genero')  # Campos a mostrar
    search_fields = ('genero',)  # Permite buscar por el campo genero
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbGenero, TbGeneroAdmin)
