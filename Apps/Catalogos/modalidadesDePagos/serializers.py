from rest_framework.serializers import ModelSerializer
from .models import TbModalidaddepago

class TbModalidaddePagoSerializers(ModelSerializer):
    class Meta:
        model = TbModalidaddepago
        fields =['idmodalidaddepago','nombremodalidad']