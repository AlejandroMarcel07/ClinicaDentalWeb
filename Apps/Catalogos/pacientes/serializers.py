from rest_framework import serializers
from Apps.Catalogos.generos.serializers import TbGeneroSerializers
from .models import TbPaciente

class TbPacienteSerializer(serializers.ModelSerializer):
    idgenero = TbGeneroSerializers()

    class Meta:
        model = TbPaciente
        fields = [
            'id',
            'nombrecompleto',
            'cedula',
            'edad',
            'idgenero',
            'direccion',
            'telefono',
            'ocupacion',
            'antecedentes',
            'isdeleted'
        ]

class TbPacienteCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbPaciente
        fields = [
            'nombrecompleto',
            'cedula',
            'edad',
            'idgenero',
            'direccion',
            'telefono',
            'ocupacion',
            'antecedentes',
            'isdeleted'
        ]
