from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
import logging

from .models import TbDetalledefactura
from .serializer import TbDetalledefacturaSerializers
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbDetalleFacturaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbDetalledefactura

    @swagger_auto_schema(responses={200: TbDetalledefacturaSerializers(many=True)})
    def get(self, request):
        detalle = TbDetalledefactura.objects.all()
        serializer = TbDetalledefacturaSerializers(detalle, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {detalle.count()} detalles facturas."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)