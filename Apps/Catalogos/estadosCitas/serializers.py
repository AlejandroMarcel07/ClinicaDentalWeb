from rest_framework.serializers import ModelSerializer
from .models import TbEstadocita

class TbEstadoCitaSerializers(ModelSerializer):
    class Meta:
        model = TbEstadocita
        fields =['idestadocita','nombreestado']