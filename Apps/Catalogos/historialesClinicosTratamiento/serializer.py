from rest_framework import serializers
from .models import TbHistorialclinicotbTbTratamiento
from django.core.exceptions import ValidationError


class TbHistorialTratamientoSerializer(serializers.ModelSerializer):
    nombretratamiento = serializers.CharField(source='idtratamiento.nombretratamiento', read_only=True)

    class Meta:
        model = TbHistorialclinicotbTbTratamiento
        fields = [
            'id', 'idhistorialclinico','idtratamiento', 'nombretratamiento', 'precio'
        ]

    def validate(self, data):

        idhistorialclinico = data.get('idhistorialclinico')
        count = TbHistorialclinicotbTbTratamiento.objects.filter(idhistorialclinico=idhistorialclinico).count()

        if count >= 3:
            raise ValidationError("Un historial clínico solo puede tener un máximo de 3 tratamientos.")

        return data