from django.db import models

from Apps.Catalogos.historialesClinicos.models import TbHistorialclinico
from Apps.Catalogos.tratamientosClinicos.models import TbTratamientoclinico


class TbHistorialclinicotbTbTratamiento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')  # Field name made lowercase.
    idtratamiento = models.ForeignKey(TbTratamientoclinico, models.DO_NOTHING, db_column='IdTratamiento')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_Tb_Tratamiento'