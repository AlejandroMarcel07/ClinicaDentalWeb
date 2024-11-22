from django.db import models

class TbMontodedescuento(models.Model):
    idmontodedescuento = models.AutoField(db_column='IdMontoDeDescuento', primary_key=True)  # Field name made lowercase.
    porcentajedescuento = models.DecimalField(db_column='PorcentajeDescuento', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_MontoDeDescuento'
