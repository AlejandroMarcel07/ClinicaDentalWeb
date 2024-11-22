from django.db import models
from Apps.Catalogos.citas.models import TbCita


class TbRecetamedica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_RecetaMedica'