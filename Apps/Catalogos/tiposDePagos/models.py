from django.db import models

class TbTipodepago(models.Model):
    idtipodepago = models.AutoField(db_column='IdTipoDePago', primary_key=True)  # Field name made lowercase.
    nombretipodepago = models.CharField(db_column='NombreTipoDePago', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_TipoDePago'
