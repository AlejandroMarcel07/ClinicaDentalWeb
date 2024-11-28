from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
import logging

from .models import TbCita
from .serializers import TbCitaSerializer
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbCitaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbCita

    @swagger_auto_schema(responses={200: TbCitaSerializer(many=True)})
    def get(self, request):
        citas = TbCita.objects.filter(idpaciente__isdeleted=False)
        serializer = TbCitaSerializer(citas, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {citas.count()} citas."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbCitaSerializer,
        responses={201: TbCitaSerializer}
    )
    def post(self, request):
        serializer = TbCitaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cita = serializer.save()
        logger.info(
            f"El usuario '{request.user}' creó un nueva cita con ID: {cita.id}.")
        return Response(
            {
                "message": "La cita se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbCitaSerializer,
        responses={200: TbCitaSerializer}
    )
    def patch(self, request, pk):
        cita = get_object_or_404(TbCita, id=pk)
        serializer = TbCitaSerializer(cita, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"El usuario '{request.user}' actualizó la cita con ID: {pk}.")
        return Response(
            {
                "message": "La cita se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        cita = get_object_or_404(TbCita, id=pk)
        self.check_object_permissions(request, cita)

        cita.idestadocita_id = 8 #Eliminada
        cita.save()

        nombre_paciente = cita.idpaciente.nombrecompleto if cita.idpaciente else "Desconocido"

        logger.info(
            f"El usuario '{request.user}' eliminó la cita con ID: {pk}.")

        return Response(
            {
                "message": f"La cita con ID {pk} del paciente {nombre_paciente} se marcó como eliminada."
            },
            status=status.HTTP_204_NO_CONTENT
        )


class TbCitaProximasApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbCita

    @swagger_auto_schema(responses={200: TbCitaSerializer(many=True)})
    def get(self, request):
        from django.utils.timezone import now, timedelta
        fecha_hoy = now().date()
        fecha_limite = fecha_hoy + timedelta(days=3)

        citas_proximas = TbCita.objects.filter(idpaciente__isdeleted=False,fecha__range=(fecha_hoy, fecha_limite))
        serializer = TbCitaSerializer(citas_proximas, many=True)

        logger.info(
            f"El usuario '{request.user}' recuperó {citas_proximas.count()} citas programadas en los próximos 3 días."
        )
        return Response(
            {
                "message": "Citas programadas en los próximos 3 días recuperadas exitosamente.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
