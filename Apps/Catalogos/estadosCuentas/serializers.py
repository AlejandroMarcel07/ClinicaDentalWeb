from rest_framework.serializers import ModelSerializer
from .models import TbEstadocuenta

class TbEstadoCuentaSerializers(ModelSerializer):
    class Meta:
        model = TbEstadocuenta
        fields =['idestadocuenta','nombreestado']