from django.db import models
from Apps.Catalogos.exploracionesClinicas.models import TbExploracionclinica
from Apps.Catalogos.historialesClinicos.models import TbHistorialclinico


class TbHistorialclinicotbExploracionclinica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')  # Field name made lowercase.
    idexploracionclinica = models.ForeignKey(TbExploracionclinica, models.DO_NOTHING, db_column='IdExploracionClinica')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_ExploracionClinica'