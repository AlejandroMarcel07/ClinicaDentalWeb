from django.contrib import admin
from .models import TbTipodepago

class TbTipodepagoAdmin(admin.ModelAdmin):
    list_display = ('idtipodepago', 'nombretipodepago')  # Campos a mostrar
    search_fields = ('nombretipodepago',)  # Permite buscar por nombre del tipo de pago
    list_filter = ('nombretipodepago',)  # Filtro por nombre del tipo de pago
    ordering = ('idtipodepago',)  # Ordenar por ID

admin.site.register(TbTipodepago, TbTipodepagoAdmin)
