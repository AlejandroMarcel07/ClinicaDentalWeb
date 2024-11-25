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

from .serializers import TbMontoDeDescuentoSerializers
from .models import TbMontodedescuento

class TbMontoDeDescuentoApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbMontodedescuento

    @swagger_auto_schema(
        responses={200: TbMontoDeDescuentoSerializers(many=True)}
    )

    def get(self, request):
        serializer = TbMontoDeDescuentoSerializers(TbMontodedescuento.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbMontoDeDescuentoSerializers,
        responses={201: TbMontoDeDescuentoSerializers}
    )
    def post(self, request):
        serializer = TbMontoDeDescuentoSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El monto de descuento se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbMontoDeDescuentoSerializers,
        responses={200: TbMontoDeDescuentoSerializers}
    )
    def patch(self, request, pk):
        monto_descuento = get_object_or_404(TbMontodedescuento, idmontodedescuento=pk)
        serializer = TbMontoDeDescuentoSerializers(monto_descuento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El monto de descuento se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        monto_descuento = get_object_or_404(TbMontodedescuento, idmontodedescuento=pk)
        cantidad_monto_descuento = monto_descuento.porcentajedescuento

        self.check_object_permissions(request, monto_descuento)
        monto_descuento.delete()

        logger.info("Monto de descuento deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Monto de descuento '{cantidad_monto_descuento}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )