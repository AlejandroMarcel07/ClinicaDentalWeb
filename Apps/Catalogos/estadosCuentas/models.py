from django.db import models

class TbEstadocuenta(models.Model):
    idestadocuenta = models.AutoField(db_column='IdEstadoCuenta', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='NombreEstado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_EstadoCuenta'
