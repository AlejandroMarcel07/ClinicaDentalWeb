from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import logging

from .models import TbPaciente
from .serializers import TbPacienteSerializer, TbPacienteCreateUpdateSerializer
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbPacienteApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbPaciente

    @swagger_auto_schema(responses={200: TbPacienteSerializer(many=True)})
    def get(self, request):

        serializer = TbPacienteSerializer(TbPaciente.objects.filter(isdeleted=False), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @swagger_auto_schema(
        request_body=TbPacienteCreateUpdateSerializer,
        responses={201: TbPacienteSerializer}
    )
    def post(self, request):
        serializer = TbPacienteCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El paciente se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbPacienteCreateUpdateSerializer,
        responses={200: TbPacienteSerializer}
    )
    def patch(self, request, pk):
        paciente = get_object_or_404(TbPaciente, id=pk)
        serializer = TbPacienteCreateUpdateSerializer(paciente, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El paciente se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        paciente = get_object_or_404(TbPaciente, id=pk)
        nombre_paciente = paciente.nombrecompleto

        #Verificamos permiso de objeto
        self.check_object_permissions(request, paciente)

        # no borramos si no cambiamos el valor
        paciente.isdeleted = True
        paciente.save()

        logger.info("Paciente deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Paciente {nombre_paciente} con ID {pk} eliminado de forma lógica."
            },
            status=status.HTTP_204_NO_CONTENT
        )
