from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging.handlers

# Configura el logger
logger = logging.getLogger(__name__)




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


    @swagger_auto_schema(
        request_body=TbTratamientosClinicosSerializes,
        responses={200: TbTratamientosClinicosSerializes}
    )
    def patch(self, request, pk):
        tratamiento = get_object_or_404(TbTratamientoclinico, id=pk)
        serializer = TbTratamientosClinicosSerializes(tratamiento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        tratamiento = get_object_or_404(TbTratamientoclinico, id=pk)
        nombre_tratamiento = tratamiento.nombretratamiento

        if not tratamiento:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, tratamiento)
        tratamiento.delete()
        logger.info(
            "Tratamiento deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Tratamiento '{nombre_tratamiento}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT)



