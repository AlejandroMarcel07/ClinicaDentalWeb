from django.db import models

class TbModalidaddepago(models.Model):
    idmodalidaddepago = models.AutoField(db_column='IdModalidadDePago', primary_key=True)  # Field name made lowercase.
    nombremodalidad = models.CharField(db_column='NombreModalidad', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_ModalidadDePago'
