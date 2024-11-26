from symtable import Class

from rest_framework import serializers
from Apps.Catalogos.citas.serializers import TbCitaNombrePacienteSerializer
from .models import TbRecetamedica

class TbRecetaMedicaConNombreSerializer(serializers.ModelSerializer):
    idcita = TbCitaNombrePacienteSerializer()
    class Meta:
        model = TbRecetamedica
        fields = [
            'id',
            'idcita',
            'descripcion',
        ]

class TbRecetaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbRecetamedica
        fields = [
            'id', 'idcita', 'descripcion'
        ]
