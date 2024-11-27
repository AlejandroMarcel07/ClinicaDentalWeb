from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import logging

from .models import TbHistorialclinico
from .serializer import TbHistorialClinicoViewSerializer, TbHistorialClinicoCreateUpdateSerializer
from ..pacientes.serializers import TbPacienteCreateUpdateSerializer
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbHistorialClinicoApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbHistorialclinico

    @swagger_auto_schema(responses={200: TbHistorialClinicoViewSerializer(many=True)})
    def get(self, request):
        historial = TbHistorialclinico.objects.all()
        serializer = TbHistorialClinicoViewSerializer(historial, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {historial.count()} de historiales clinicos."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)
