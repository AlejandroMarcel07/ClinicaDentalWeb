from django.contrib import admin
from .models import TbFactura

class TbFacturaAdmin(admin.ModelAdmin):
    list_display = ('idfactura', 'idcita', 'costototal', 'idtipodepago', 'descuentoaplicado', 'idmontodedescuento',
                    'totaldescuentoaplicado', 'idmodalidaddepago', 'cantidadcuotas', 'cuotaspagadas', 'costoporcuota', 'idestadocuenta')  # Campos a mostrar
    search_fields = ('idfactura', 'idcita__id', 'idtipodepago__nombre', 'idestadocuenta__nombreestado')  # Permite buscar por estos campos
    ordering = ('idfactura',)  # Ordenar por ID de factura

admin.site.register(TbFactura, TbFacturaAdmin)
