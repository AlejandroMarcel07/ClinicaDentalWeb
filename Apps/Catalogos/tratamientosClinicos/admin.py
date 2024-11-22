from django.contrib import admin
from .models import TbTratamientoclinico

class TbTratamientoclinicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombretratamiento')  # Campos a mostrar
    search_fields = ('nombretratamiento',)  # Permite buscar por nombre del tratamiento
    list_filter = ('nombretratamiento',)  # Filtro por nombre del tratamiento
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbTratamientoclinico, TbTratamientoclinicoAdmin)
