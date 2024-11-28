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
