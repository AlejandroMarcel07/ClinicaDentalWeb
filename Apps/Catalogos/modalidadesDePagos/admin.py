from django.contrib import admin
from .models import TbModalidaddepago

class TbModalidaddepagoAdmin(admin.ModelAdmin):
    list_display = ('idmodalidaddepago', 'nombremodalidad')  # Campos a mostrar
    search_fields = ('nombremodalidad',)  # Permite buscar por el nombre de la modalidad de pago
    ordering = ('idmodalidaddepago',)  # Ordenar por ID

admin.site.register(TbModalidaddepago, TbModalidaddepagoAdmin)
