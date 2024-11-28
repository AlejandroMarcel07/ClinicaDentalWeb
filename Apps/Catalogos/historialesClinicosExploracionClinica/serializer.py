from rest_framework import serializers
from .models import TbHistorialclinicotbExploracionclinica
from django.core.exceptions import ValidationError


class TbHistorialExploracionClinicaSerializer(serializers.ModelSerializer):
    nombreexploracion = serializers.CharField(source='idexploracionclinica.tipo', read_only=True)

    class Meta:
        model = TbHistorialclinicotbExploracionclinica
        fields = [
            'id', 'idhistorialclinico','idexploracionclinica', 'nombreexploracion'
        ]
    def validate(self, data):

        idhistorialclinico = data.get('idhistorialclinico')
        count = TbHistorialclinicotbExploracionclinica.objects.filter(idhistorialclinico=idhistorialclinico).count()

        if count >= 3:
            raise ValidationError("Un historial clínico solo puede tener un máximo de 3 exploraciones clínicas.")

        return data

