from symtable import Class
from rest_framework import serializers
from .models import TbRecetamedica


class TbRecetaMedicaSerializer(serializers.ModelSerializer):
    nombrepaciente = serializers.CharField(source='idcita.idpaciente.nombrecompleto', read_only=True)
    class Meta:
        model = TbRecetamedica
        fields = [
            'id', 'idcita','nombrepaciente', 'descripcion'
        ]
