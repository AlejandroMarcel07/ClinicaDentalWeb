from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
import logging

from .models import TbCita, TbFactura
from .serializer import TbFacturaSerializer, TbFacturaGetSerializer
from ..detallesFacturas.models import TbDetalledefactura
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class CrearFactura(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbFactura

    @swagger_auto_schema(
        responses={200: TbFacturaGetSerializer(many=True)}
    )
    def get(self, request):
        factura = TbFactura.objects.all()
        serializer = TbFacturaGetSerializer(factura, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {factura.count()} facturas."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(responses={200: TbFacturaSerializer(many=True)})
    def post(self, request):
        serializer = TbFacturaSerializer(data=request.data)
        if serializer.is_valid():
            factura = serializer.save()
            logger.info(
                f"El usuario '{request.user}' creó una nueva factura con ID: {factura.idfactura}.")
            return Response(
                {
                "message": "La factura se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        factura = get_object_or_404(TbFactura, idfactura=pk)

        self.check_object_permissions(request, factura)
        TbDetalledefactura.objects.filter(idfactura=factura).delete()
        factura.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó la factura con ID: {pk}.")

        return Response(
            {
                "message": f"La factura con id: {pk} a sido eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )