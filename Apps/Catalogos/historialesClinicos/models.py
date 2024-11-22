from django.db import models
from Apps.Catalogos.citas.models import TbCita


class TbHistorialclinico(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='Motivo', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    historiadeldolor = models.TextField(db_column='HistoriaDelDolor', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    interpretacionradiografica = models.CharField(db_column='InterpretacionRadiografica', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    observacion = models.CharField(db_column='Observacion', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinico'