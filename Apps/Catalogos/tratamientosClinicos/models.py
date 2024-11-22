from django.db import models

class TbTratamientoclinico(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombretratamiento = models.CharField(db_column='NombreTratamiento', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_TratamientoClinico'