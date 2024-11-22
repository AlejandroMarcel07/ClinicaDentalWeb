from django.db import models
from Apps.Catalogos.facturas.models import TbFactura


class TbDetalledefactura(models.Model):
    iddetallefactura = models.AutoField(db_column='IdDetalleFactura', primary_key=True)  # Field name made lowercase.
    idfactura = models.ForeignKey(TbFactura, models.DO_NOTHING, db_column='IdFactura')  # Field name made lowercase.
    nombretratamiento = models.CharField(db_column='NombreTratamiento', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_DetalleDeFactura'