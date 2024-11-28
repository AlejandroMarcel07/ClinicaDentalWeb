from rest_framework import serializers
from Apps.Catalogos.generos.serializers import TbGeneroSerializers
from .models import TbPaciente

class TbPacienteSerializer(serializers.ModelSerializer):
    nombregenero = serializers.CharField(source='idgenero.genero', read_only=True)

    class Meta:
        model = TbPaciente
        fields = [
            'id',
            'nombrecompleto',
            'cedula',
            'edad',
            'idgenero',
            'nombregenero',
            'direccion',
            'telefono',
            'ocupacion',
            'antecedentes',
            'isdeleted'
        ]
