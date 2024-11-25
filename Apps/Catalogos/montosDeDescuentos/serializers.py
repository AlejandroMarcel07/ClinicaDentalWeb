from rest_framework.serializers import ModelSerializer
from .models import TbMontodedescuento

class TbMontoDeDescuentoSerializers(ModelSerializer):
    class Meta:
        model = TbMontodedescuento
        fields =['idmontodedescuento','porcentajedescuento']