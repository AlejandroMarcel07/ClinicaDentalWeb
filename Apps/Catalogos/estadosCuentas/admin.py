from django.contrib import admin
from .models import TbEstadocuenta

class TbEstadocuentaAdmin(admin.ModelAdmin):
    list_display = ('idestadocuenta', 'nombreestado')  # Campos a mostrar en la lista de administración
    search_fields = ('nombreestado',)  # Permite buscar por el nombre del estado
    list_filter = ('nombreestado',)  # Filtro por nombre de estado
    ordering = ('idestadocuenta',)  # Ordenar por id

admin.site.register(TbEstadocuenta, TbEstadocuentaAdmin)
