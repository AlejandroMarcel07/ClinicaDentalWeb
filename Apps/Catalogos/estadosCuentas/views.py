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

from .serializers import TbEstadoCuentaSerializers
from .models import TbEstadocuenta

class TbEstadoCuentaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbEstadocuenta

    @swagger_auto_schema(
        responses={200: TbEstadoCuentaSerializers(many=True)}
    )
    def get(self, request):
        serializer = TbEstadoCuentaSerializers(TbEstadocuenta.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbEstadoCuentaSerializers,
        responses={201: TbEstadoCuentaSerializers}
    )
    def post(self, request):
        serializer = TbEstadoCuentaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El estado de cuenta se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbEstadoCuentaSerializers,
        responses={200: TbEstadoCuentaSerializers}
    )
    def patch(self, request, pk):
        objeto_cuenta = get_object_or_404(TbEstadocuenta, idestadocuenta=pk)
        serializer = TbEstadoCuentaSerializers(objeto_cuenta, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "EL estado de cuenta se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        objeto_estado = get_object_or_404(TbEstadocuenta, idestadocuenta=pk)
        nombre_estado = objeto_estado.nombreestado

        self.check_object_permissions(request, objeto_estado)
        objeto_estado.delete()

        logger.info("Estado de cuenta deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Estado de cuenta '{nombre_estado}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )
