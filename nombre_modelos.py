# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bitacora(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=128, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    operation = models.CharField(db_column='Operation', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recordid = models.IntegerField(db_column='RecordId', blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.TextField(db_column='OldValue', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    newvalue = models.TextField(db_column='NewValue', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='ChangeDate', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=128, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bitacora'


class TbCita(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idpaciente = models.ForeignKey('TbPaciente', models.DO_NOTHING, db_column='IdPaciente')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    idestadocita = models.ForeignKey('TbEstadocita', models.DO_NOTHING, db_column='IdEstadoCita')  # Field name made lowercase.
    horaentrada = models.TimeField(db_column='HoraEntrada')  # Field name made lowercase.
    horasalida = models.TimeField(db_column='HoraSalida')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Cita'


class TbDetalledefactura(models.Model):
    iddetallefactura = models.AutoField(db_column='IdDetalleFactura', primary_key=True)  # Field name made lowercase.
    idfactura = models.ForeignKey('TbFactura', models.DO_NOTHING, db_column='IdFactura')  # Field name made lowercase.
    nombretratamiento = models.CharField(db_column='NombreTratamiento', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_DetalleDeFactura'


class TbEstadocita(models.Model):
    idestadocita = models.AutoField(db_column='IdEstadoCita', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='NombreEstado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_EstadoCita'


class TbEstadocuenta(models.Model):
    idestadocuenta = models.AutoField(db_column='IdEstadoCuenta', primary_key=True)  # Field name made lowercase.
    nombreestado = models.CharField(db_column='NombreEstado', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_EstadoCuenta'


class TbExploracionclinica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_ExploracionClinica'


class TbFactura(models.Model):
    idfactura = models.AutoField(db_column='IdFactura', primary_key=True)  # Field name made lowercase.
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita')  # Field name made lowercase.
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=18, decimal_places=0)  # Field name made lowercase.
    idtipodepago = models.ForeignKey('TbTipodepago', models.DO_NOTHING, db_column='IdTipoDePago')  # Field name made lowercase.
    descuentoaplicado = models.BooleanField(db_column='DescuentoAplicado')  # Field name made lowercase.
    idmontodedescuento = models.ForeignKey('TbMontodedescuento', models.DO_NOTHING, db_column='IdMontoDeDescuento', blank=True, null=True)  # Field name made lowercase.
    totaldescuentoaplicado = models.DecimalField(db_column='TotalDescuentoAplicado', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idmodalidaddepago = models.ForeignKey('TbModalidaddepago', models.DO_NOTHING, db_column='IdModalidadDePago')  # Field name made lowercase.
    cantidadcuotas = models.IntegerField(db_column='CantidadCuotas', blank=True, null=True)  # Field name made lowercase.
    cuotaspagadas = models.IntegerField(db_column='CuotasPagadas', blank=True, null=True)  # Field name made lowercase.
    costoporcuota = models.DecimalField(db_column='CostoPorCuota', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    idestadocuenta = models.ForeignKey(TbEstadocuenta, models.DO_NOTHING, db_column='IdEstadoCuenta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Factura'


class TbGenero(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=9, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_Genero'


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


class TbHistorialclinicotbExploracionclinica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')  # Field name made lowercase.
    idexploracionclinica = models.ForeignKey(TbExploracionclinica, models.DO_NOTHING, db_column='IdExploracionClinica')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_ExploracionClinica'


class TbHistorialclinicotbTbTratamiento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idhistorialclinico = models.ForeignKey(TbHistorialclinico, models.DO_NOTHING, db_column='IdHistorialClinico')  # Field name made lowercase.
    idtratamiento = models.ForeignKey('TbTratamientoclinico', models.DO_NOTHING, db_column='IdTratamiento')  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=18, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_HistorialClinicoTb_Tb_Tratamiento'


class TbModalidaddepago(models.Model):
    idmodalidaddepago = models.AutoField(db_column='IdModalidadDePago', primary_key=True)  # Field name made lowercase.
    nombremodalidad = models.CharField(db_column='NombreModalidad', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_ModalidadDePago'


class TbMontodedescuento(models.Model):
    idmontodedescuento = models.AutoField(db_column='IdMontoDeDescuento', primary_key=True)  # Field name made lowercase.
    porcentajedescuento = models.DecimalField(db_column='PorcentajeDescuento', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_MontoDeDescuento'


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


class TbRecetamedica(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idcita = models.ForeignKey(TbCita, models.DO_NOTHING, db_column='IdCita')  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_RecetaMedica'


class TbTipodepago(models.Model):
    idtipodepago = models.AutoField(db_column='IdTipoDePago', primary_key=True)  # Field name made lowercase.
    nombretipodepago = models.CharField(db_column='NombreTipoDePago', max_length=50, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_TipoDePago'


class TbTratamientoclinico(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nombretratamiento = models.CharField(db_column='NombreTratamiento', max_length=100, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tb_TratamientoClinico'
