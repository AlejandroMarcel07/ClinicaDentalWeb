from rest_framework.serializers import ModelSerializer
from .models import TbGenero

class TbGeneroSerializers(ModelSerializer):
    class Meta:
        model = TbGenero
        fields =['id','genero']