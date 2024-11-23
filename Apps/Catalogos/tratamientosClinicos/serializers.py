from rest_framework.serializers import ModelSerializer
from .models import TbTratamientoclinico

class TbTratamientosClinicosSerializes(ModelSerializer):
    class Meta:
        model = TbTratamientoclinico
        fields =['id','nombretratamiento']