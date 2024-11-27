from rest_framework import serializers
from .models import TbHistorialclinico
from ..citas.serializers import TbCitaNombrePacienteSerializer


class TbHistorialClinicoViewSerializer(serializers.ModelSerializer):
    idcita = TbCitaNombrePacienteSerializer()
    class Meta:
        model = TbHistorialclinico
        fields = [
            'idcita',
            'motivo',
            'historiadeldolor',
            'interpretacionradiografica',
            'observacion'
        ]

class TbHistorialClinicoCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbHistorialclinico
        fields = [
            'idcita',
            'motivo',
            'historiadeldolor',
            'interpretacionradiografica',
            'observacion'
        ]