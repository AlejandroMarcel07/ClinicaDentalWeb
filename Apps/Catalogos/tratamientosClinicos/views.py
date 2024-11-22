from idlelib.pyparse import trans
from operator import truediv
from drf_yasg.utils import swagger_auto_schema

from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status

from .models import TbTratamientoclinico
from .serializers import TbTratamientosClinicosSerializes

class TbTratamientoclinioApiView(APIView):
    @swagger_auto_schema(
        responses={200: TbTratamientosClinicosSerializes(many=True)}
    )
    #Este es como una funcion que me permite obtener los datos
    def get(self, request):
        serializer = TbTratamientosClinicosSerializes(TbTratamientoclinico.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbTratamientosClinicosSerializes,
        responses={201: TbTratamientosClinicosSerializes}
    )
    #Este es una funcion que me permite insertar datos
    def post(self, request):
        serializer= TbTratamientosClinicosSerializes(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status= status.HTTP_201_CREATED, data=serializer.data)




