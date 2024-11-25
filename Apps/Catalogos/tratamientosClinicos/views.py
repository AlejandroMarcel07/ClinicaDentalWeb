from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging.handlers

from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

from .models import TbTratamientoclinico
from .serializers import TbTratamientosClinicosSerializes

class TbTratamientoclinioApiView(APIView):

    #Nos permite antes de entrar a la clase que el usuario este permitido acceder alguna funcion
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbTratamientoclinico  # Aquí definimos el modelo explícitamente


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
        return Response(
            {
                "message": "El tipo de tratamiento se inserto exitosamente.",
                "data": serializer.data
            },
            status= status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbTratamientosClinicosSerializes,
        responses={200: TbTratamientosClinicosSerializes}
    )
    def patch(self, request, pk):
        tratamiento = get_object_or_404(TbTratamientoclinico, id=pk)
        serializer = TbTratamientosClinicosSerializes(tratamiento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El tratamiento clinico se actualizó exitosamente.",
                "data": serializer.data
            },
          status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        tratamiento = get_object_or_404(TbTratamientoclinico, id=pk)
        nombre_tratamiento = tratamiento.nombretratamiento


        self.check_object_permissions(request, tratamiento)
        tratamiento.delete()
        logger.info(
            "Tratamiento deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Tratamiento '{nombre_tratamiento}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT)



