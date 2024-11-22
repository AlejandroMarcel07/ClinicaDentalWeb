from django.db import models

from Apps.Catalogos.citas.models import TbCita
from Apps.Catalogos.estadosCuentas.models import TbEstadocuenta
from Apps.Catalogos.modalidadesDePagos.models import TbModalidaddepago
from Apps.Catalogos.montosDeDescuentos.models import TbMontodedescuento
from Apps.Catalogos.tiposDePagos.models import TbTipodepago


class TbFactura(models.Model):
    idfactura = models.AutoField(db_column='IdFactura', primary_key=True)  # Field name made lowercase.
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita')  # Field name made lowercase.
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=18, decimal_places=0)  # Field name made lowercase.
    idtipodepago = models.ForeignKey(TbTipodepago, models.DO_NOTHING, db_column='IdTipoDePago')  # Field name made lowercase.
    descuentoaplicado = models.BooleanField(db_column='DescuentoAplicado')  # Field name made lowercase.
    idmontodedescuento = models.ForeignKey(TbMontodedescuento, models.DO_NOTHING, db_column='IdMontoDeDescuento', blank=True, null=True)  # Field name made lowercase.
    totaldescuentoaplicado = models.DecimalField(db_column='TotalDescuentoAplicado', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idmodalidaddepago = models.ForeignKey(TbModalidaddepago, models.DO_NOTHING, db_column='IdModalidadDePago')  # Field name made lowercase.
    cantidadcuotas = models.IntegerField(db_column='CantidadCuotas', blank=True, null=True)  # Field name made lowercase.
    cuotaspagadas = models.IntegerField(db_column='CuotasPagadas', blank=True, null=True)  # Field name made lowercase.
    costoporcuota = models.DecimalField(db_column='CostoPorCuota', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idestadocuenta = models.ForeignKey(TbEstadocuenta, models.DO_NOTHING, db_column='IdEstadoCuenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Factura'
