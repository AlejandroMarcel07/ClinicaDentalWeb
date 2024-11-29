from rest_framework import serializers
from .models import TbHistorialclinico
from ..citas.models import TbCita
from ..historialesClinicosExploracionClinica.models import TbHistorialclinicotbExploracionclinica
from ..historialesClinicosTratamiento.models import TbHistorialclinicotbTbTratamiento
from ..pacientes.models import TbPaciente
from ..recetasMedicas.models import TbRecetamedica


class TbHistorialClinicoViewSerializer(serializers.ModelSerializer):
    nombrepaciente = serializers.CharField(source='idcita.idpaciente.nombrecompleto', read_only=True)

    class Meta:
        model = TbHistorialclinico
        fields = [
            'id',
            'idcita',
            'nombrepaciente',
            'motivo',
            'historiadeldolor',
            'interpretacionradiografica',
            'observacion'
        ]


    def validate_idcita(self, value):
        if TbHistorialclinico.objects.filter(idcita=value).exists():
            raise serializers.ValidationError("Ya existe un historial clínico para esta cita.")
        return value


class DetalleHistorialClinicoSerializer(serializers.ModelSerializer):

    cita = serializers.SerializerMethodField()
    paciente = serializers.SerializerMethodField()

    exploraciones_clinicas = serializers.SerializerMethodField()
    tratamientos = serializers.SerializerMethodField()
    recetas = serializers.SerializerMethodField()

    class Meta:
        model = TbHistorialclinico
        fields = [
            'id',
            'cita',
            'paciente',
            'motivo',
            'historiadeldolor',
            'interpretacionradiografica',
            'observacion',
            'exploraciones_clinicas',
            'tratamientos',
            'recetas',
        ]

    def get_cita(self, obj):
        cita = TbCita.objects.get(id=obj.idcita.id)
        return {
            "fecha": cita.fecha,
            "idestadocita": cita.idestadocita.nombreestado,
            "horaentrada": cita.horaentrada,
            "horasalida": cita.horasalida,
        }

    def get_paciente(self, obj):
        paciente = TbPaciente.objects.get(id=obj.idcita.idpaciente.id)

        if paciente.isdeleted == 1:
            raise serializers.ValidationError("Historial no encontrado. El paciente está eliminado.")

        return {
            "nombrecompleto": paciente.nombrecompleto,
            "cedula": paciente.cedula,
            "edad": paciente.edad,
            "idgenero": paciente.idgenero.genero,
            "direccion": paciente.direccion,
            "telefono": paciente.telefono,
            "ocupacion": paciente.ocupacion,
            "antecedentes": paciente.antecedentes,
        }

    def get_exploraciones_clinicas(self, obj):
        exploraciones = TbHistorialclinicotbExploracionclinica.objects.filter(idhistorialclinico=obj.id)
        return [
            {
                "nombreexploracion": exp.idexploracionclinica.tipo
            }
            for exp in exploraciones
        ]

    def get_tratamientos(self, obj):
        tratamientos = TbHistorialclinicotbTbTratamiento.objects.filter(idhistorialclinico=obj.id)
        return [
            {
                "nombretratamiento": tratamiento.idtratamiento.nombretratamiento,
                "precio": tratamiento.precio
            }
            for tratamiento in tratamientos
        ]

    def get_recetas(self, obj):
        recetas = TbRecetamedica.objects.filter(idcita=obj.idcita)
        return [
            {
                "descripcion": receta.descripcion,
            }
            for receta in recetas
        ]


