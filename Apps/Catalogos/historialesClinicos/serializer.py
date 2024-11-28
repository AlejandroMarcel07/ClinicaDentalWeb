from rest_framework import serializers
from .models import TbHistorialclinico


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
