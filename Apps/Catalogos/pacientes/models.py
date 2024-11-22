from django.db import models

from Apps.Catalogos.generos.models import TbGenero


class TbPaciente(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=60, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=16, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    edad = models.IntegerField(db_column='Edad')  # Field name made lowercase.
    idgenero = models.ForeignKey(TbGenero, models.DO_NOTHING, db_column='IdGenero')  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    ocupacion = models.CharField(db_column='Ocupacion', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    antecedentes = models.TextField(db_column='Antecedentes', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Paciente'