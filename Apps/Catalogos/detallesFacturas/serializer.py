from rest_framework.serializers import ModelSerializer
from .models import TbDetalledefactura

class TbDetalledefacturaSerializers(ModelSerializer):
    class Meta:
        model = TbDetalledefactura
        fields =['iddetallefactura','idfactura', 'nombretratamiento', 'precio']
