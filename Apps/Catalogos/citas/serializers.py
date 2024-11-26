from datetime import datetime
from rest_framework import serializers

from .models import TbCita
from django.db.models import Q

from ..estadosCitas.models import TbEstadocita


class TbCitaSerializer(serializers.ModelSerializer):
    # Gracias al charfield nos permite obtener solo una propiedad del objeto en sí y no todo el objeto
    idpaciente = serializers.CharField(source='idpaciente.nombrecompleto')
    idestadocita = serializers.CharField(source='idestadocita.nombreestado')

    class Meta:
        model = TbCita
        fields = [
            'id',
            'idpaciente',
            'fecha',
            'idestadocita',
            'horaentrada',
            'horasalida'
        ]


class TbCitaCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCita
        fields = [
            'idpaciente',
            'fecha',
            'idestadocita',
            'horaentrada',
            'horasalida'
        ]

    def validate_fecha(self, value):
        # Asegura que la fecha no sea del pasado
        if value < datetime.now().date():
            raise serializers.ValidationError("La fecha de la cita no puede ser en el pasado.")
        return value

    def validate(self, data):
        """Validar conflictos de horarios y establecer valores por defecto."""
        # Validar horas no superpuestas
        fecha = data.get('fecha')
        horaentrada = data.get('horaentrada')
        horasalida = data.get('horasalida')
        idpaciente = data.get('idpaciente')

        if fecha and horaentrada and horasalida:
            conflictos = TbCita.objects.filter(
                Q(fecha=fecha) &
                (
                    Q(horaentrada__lt=horasalida, horasalida__gt=horaentrada)
                )
            )
            if conflictos.exists():
                raise serializers.ValidationError("El horario de la cita se superpone con otra existente.")

        # Establecer estado por defecto si no se proporciona
        if 'idestadocita' not in data or not data['idestadocita']:
            try:
                data['idestadocita'] = TbEstadocita.objects.get(idestadocita=1)  # Ajusta si el nombre del campo es otro
            except TbEstadocita.DoesNotExist:
                raise serializers.ValidationError("Estado de cita con ID 1 no encontrado.")

        return data