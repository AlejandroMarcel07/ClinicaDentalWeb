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

from .serializers import TbModalidaddePagoSerializers
from .models import TbModalidaddepago

class TbModalidaddePagoApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbModalidaddepago

    @swagger_auto_schema(
        responses={200: TbModalidaddePagoSerializers(many=True)}
    )
    def get(self, request):
        serializer = TbModalidaddePagoSerializers(TbModalidaddepago.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @swagger_auto_schema(
        request_body=TbModalidaddePagoSerializers,
        responses={201: TbModalidaddePagoSerializers}
    )
    def post(self, request):
        serializer = TbModalidaddePagoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbModalidaddePagoSerializers,
        responses={200: TbModalidaddePagoSerializers}
    )
    def patch(self, request, pk):
        modalidad_pago = get_object_or_404(TbModalidaddepago, idmodalidaddepago=pk)
        serializer = TbModalidaddePagoSerializers(modalidad_pago, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)



    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        modalidad_pago = get_object_or_404(TbModalidaddepago, idmodalidaddepago=pk)
        nombre_modalidad_pago = modalidad_pago.nombremodalidad

        if not modalidad_pago:
            return Response({'error': 'Modalidad de pago no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, modalidad_pago)
        modalidad_pago.delete()

        logger.info("Modalidad de pago deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Modalidad de pago '{nombre_modalidad_pago}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )