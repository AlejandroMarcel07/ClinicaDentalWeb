from rest_framework.serializers import ModelSerializer
from .models import TbTipodepago

class TbTiposDePagosSerializes(ModelSerializer):
    class Meta:
        model = TbTipodepago
        fields =['idtipodepago','nombretipodepago']