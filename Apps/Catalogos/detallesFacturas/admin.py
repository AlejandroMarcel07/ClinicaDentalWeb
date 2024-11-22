from django.contrib import admin
from .models import TbDetalledefactura
from Apps.Catalogos.facturas.models import TbFactura

class TbDetalledefacturaAdmin(admin.ModelAdmin):
    list_display = ('iddetallefactura', 'idfactura', 'nombretratamiento', 'precio')  # Campos a mostrar en la lista de administración
    search_fields = ('idfactura__id', 'nombretratamiento')  # Permite buscar por el ID de la factura y nombre del tratamiento
    list_filter = ('idfactura',)  # Filtros por ID de factura
    ordering = ('iddetallefactura',)  # Ordenar por ID de detalle de factura

admin.site.register(TbDetalledefactura, TbDetalledefacturaAdmin)
