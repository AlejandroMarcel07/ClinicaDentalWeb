from rest_framework.serializers import ModelSerializer
from .models import TbExploracionclinica

class TbExploracionClinicaSerializers(ModelSerializer):
    class Meta:
        model = TbExploracionclinica
        fields =['id','tipo']