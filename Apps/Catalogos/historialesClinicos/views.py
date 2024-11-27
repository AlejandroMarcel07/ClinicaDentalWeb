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
            f"El usuario '{request.user}' recuperó {historial.count()} historiales clinicos."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @swagger_auto_schema(request_body=TbHistorialClinicoCreateUpdateSerializer, responses={201: TbHistorialClinicoCreateUpdateSerializer})
    def post(self, request):
        serializer = TbHistorialClinicoCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            historialclinico = serializer.save()

            cita = historialclinico.idcita
            paciente = cita.idpaciente
            nombre_paciente = paciente.nombrecompleto

            respuesta_serializer = TbHistorialClinicoCreateUpdateSerializer(historialclinico)
            logger.info(
                f"El usuario '{request.user}' creó un nuevo historial clinico con ID: {historialclinico.id}.")
            return Response(
                {
                    "message": "El historial clinico se insertó exitosamente.",
                    "nombre_paciente" : nombre_paciente,
                    "data": respuesta_serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @swagger_auto_schema(
        request_body=TbHistorialClinicoCreateUpdateSerializer,
        responses={200: TbHistorialClinicoCreateUpdateSerializer}
    )
    def patch(self, request, pk):
        historial_clinico = get_object_or_404(TbHistorialclinico, id=pk)
        serializer = TbHistorialClinicoCreateUpdateSerializer(historial_clinico, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        cita = historial_clinico.idcita
        paciente = cita.idpaciente
        nombre_paciente = paciente.nombrecompleto

        historial = serializer.save()
        respuesta_serializer = TbHistorialClinicoCreateUpdateSerializer(historial)

        logger.info(
            f"El usuario '{request.user}' actualizó el historial clinico con ID: {pk}.")

        return Response(
            {
                "message": "La historial clinico se actualizó exitosamente.",
                "nombre_paciente": nombre_paciente,
                "data": respuesta_serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        historial_clinico = get_object_or_404(TbHistorialclinico, id=pk)

        #Permite que se validen los permisos específicos sobre el objeto en cuestión
        self.check_object_permissions(request, historial_clinico)
        historial_clinico.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó el historial clinico con ID: {pk}.")

        return Response(
            {
                "message": f"El historial clinico con id: {pk} a sido eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )