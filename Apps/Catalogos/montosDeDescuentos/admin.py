from django.contrib import admin
from .models import TbMontodedescuento

class TbMontodedescuentoAdmin(admin.ModelAdmin):
    list_display = ('idmontodedescuento', 'porcentajedescuento')  # Campos a mostrar
    search_fields = ('porcentajedescuento',)  # Permite buscar por porcentaje de descuento
    ordering = ('idmontodedescuento',)  # Ordenar por ID

admin.site.register(TbMontodedescuento, TbMontodedescuentoAdmin)
