from django.db import models

class TbEstadocita(models.Model):
    idestadocita = models.AutoField(db_column='IdEstadoCita', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='NombreEstado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_EstadoCita'
