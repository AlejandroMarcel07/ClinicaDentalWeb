from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
import logging

from .models import TbHistorialclinicotbExploracionclinica
from .serializer import TbHistorialExploracionClinicaSerializer
from ..citas.models import TbCita
from ..historialesClinicos.models import TbHistorialclinico
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbHistorialExploracionClinicaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbHistorialclinicotbExploracionclinica

    @swagger_auto_schema(responses={200: TbHistorialExploracionClinicaSerializer(many=True)})
    def get(self, request):

        citas_no_eliminadas = TbCita.objects.filter(idpaciente__isdeleted=False)
        historiales_no_eliminados = TbHistorialclinico.objects.filter(idcita__in=citas_no_eliminadas)
        historialexploracion = TbHistorialclinicotbExploracionclinica.objects.filter(idhistorialclinico__in=historiales_no_eliminados)

        data = []
        for historial in historiales_no_eliminados:
            exploraciones = historialexploracion.filter(idhistorialclinico=historial.id)
            exploraciones_data = TbHistorialExploracionClinicaSerializer(exploraciones, many=True).data
            data.append({
                'idhistorialclinico': historial.id,
                'exploraciones': exploraciones_data
            })
        logger.info(
            f"El usuario '{request.user}' recuperó {len(data)} historiales exploraciones."
        )
        return Response(status=status.HTTP_200_OK, data=data)

    @swagger_auto_schema(
        request_body=TbHistorialExploracionClinicaSerializer,
        responses={201: TbHistorialExploracionClinicaSerializer}
    )
    def post(self, request):
        serializer = TbHistorialExploracionClinicaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        historialexploracion = serializer.save()

        logger.info(
            f"El usuario '{request.user}' creó un nuevo historial exploracion con ID: {historialexploracion.id}.")

        return Response(
            {
                "message": "El historial exploracion se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbHistorialExploracionClinicaSerializer,
        responses={200: TbHistorialExploracionClinicaSerializer}
    )
    def patch(self, request, pk):
        historialexploracion = get_object_or_404(TbHistorialclinicotbExploracionclinica, id=pk)
        serializer = TbHistorialExploracionClinicaSerializer(historialexploracion, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"El usuario '{request.user}' actualizó el historial exploracion con ID: {pk}.")
        return Response(
            {
                "message": "El historial exploracion se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        historialexploracion = get_object_or_404(TbHistorialclinicotbExploracionclinica, id=pk)
        self.check_object_permissions(request, historialexploracion)
        historialexploracion.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó el historial exploracion con ID: {pk}.")

        return Response(
            {
                "message": f"Historial exploracion  con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )