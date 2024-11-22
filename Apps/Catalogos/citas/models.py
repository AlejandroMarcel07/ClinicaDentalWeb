from django.db import models
from Apps.Catalogos.estadosCitas.models import TbEstadocita
from Apps.Catalogos.pacientes.models import TbPaciente


class TbCita(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey(TbPaciente, models.DO_NOTHING, db_column='IdPaciente')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    idestadocita = models.ForeignKey(TbEstadocita, models.DO_NOTHING, db_column='IdEstadoCita')  # Field name made lowercase.
    horaentrada = models.TimeField(db_column='HoraEntrada')  # Field name made lowercase.
    horasalida = models.TimeField(db_column='HoraSalida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Cita'
