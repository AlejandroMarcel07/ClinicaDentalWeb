from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import logging

from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

from .serializers import TbEstadoCitaSerializers
from .models import TbEstadocita

class TbEstadoCitaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbEstadocita

    @swagger_auto_schema(
        responses={200: TbEstadoCitaSerializers(many=True)}
    )
    def get(self, request):
        serializer = TbEstadoCitaSerializers(TbEstadocita.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbEstadoCitaSerializers,
        responses={201: TbEstadoCitaSerializers}
    )
    def post(self, request):
        serializer = TbEstadoCitaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El estado de cita se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbEstadoCitaSerializers,
        responses={200: TbEstadoCitaSerializers}
    )
    def patch(self, request, pk):
        objeto_citas = get_object_or_404(TbEstadocita, idestadocita=pk)
        serializer = TbEstadoCitaSerializers(objeto_citas, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "EL estado de cita se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        objeto_cia = get_object_or_404(TbEstadocita, idestadocita=pk)
        nombre_estado = objeto_cia.nombreestado

        self.check_object_permissions(request, objeto_cia)
        objeto_cia.delete()

        logger.info("Estado de cita deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Estado de cita '{nombre_estado}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )