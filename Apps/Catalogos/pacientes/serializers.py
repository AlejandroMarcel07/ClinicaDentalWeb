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

class TbPacienteEstadisticasSerializer(serializers.Serializer):
    total_activos = serializers.IntegerField()
    total_borrados = serializers.IntegerField()
    hombres = serializers.IntegerField()
    mujeres = serializers.IntegerField()
    edades = serializers.DictField(child=serializers.FloatField())
    rangos_edades = serializers.DictField(child=serializers.IntegerField())
    ocupaciones_comunes = serializers.ListField(child=serializers.DictField())
    sin_antecedentes = serializers.IntegerField()

