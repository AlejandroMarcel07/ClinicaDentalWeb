from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
import logging

from .models import TbHistorialclinicotbTbTratamiento
from .serializer import TbHistorialTratamientoSerializer
from ..citas.models import TbCita
from ..historialesClinicos.models import TbHistorialclinico
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbHistorialTratamientoClinicaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbHistorialclinicotbTbTratamiento

    @swagger_auto_schema(responses={200: TbHistorialTratamientoSerializer(many=True)})
    def get(self, request):

        citas_no_eliminadas = TbCita.objects.filter(idpaciente__isdeleted=False)
        historiales_no_eliminados = TbHistorialclinico.objects.filter(idcita__in=citas_no_eliminadas)
        historialtratamiento = TbHistorialclinicotbTbTratamiento.objects.filter(idhistorialclinico__in=historiales_no_eliminados)

        data = []
        for historial in historiales_no_eliminados:
            tratamientos = historialtratamiento.filter(idhistorialclinico=historial.id)
            tratamientos_data = TbHistorialTratamientoSerializer(tratamientos, many=True).data
            data.append({
                'idhistorialclinico': historial.id,
                'tratamientos': tratamientos_data
            })
        logger.info(
            f"El usuario '{request.user}' recuperó {len(data)}tratamientos."
        )
        return Response(status=status.HTTP_200_OK, data=data)

    @swagger_auto_schema(
        request_body=TbHistorialTratamientoSerializer,
        responses={201: TbHistorialTratamientoSerializer}
    )
    def post(self, request):
        serializer = TbHistorialTratamientoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        historialtratamiento = serializer.save()

        logger.info(
            f"El usuario '{request.user}' creó un nuevo historial tratamiento con ID: {historialtratamiento.id}.")

        return Response(
            {
                "message": "El historial tratamiento se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbHistorialTratamientoSerializer,
        responses={200: TbHistorialTratamientoSerializer}
    )
    def patch(self, request, pk):
        historialtratamiento = get_object_or_404(TbHistorialclinicotbTbTratamiento, id=pk)
        serializer = TbHistorialTratamientoSerializer(historialtratamiento, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"El usuario '{request.user}' actualizó el historial tratamiento con ID: {pk}.")
        return Response(
            {
                "message": "El historial tratamiento se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        historialtratamiento = get_object_or_404(TbHistorialclinicotbTbTratamiento, id=pk)
        self.check_object_permissions(request, historialtratamiento)
        historialtratamiento.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó el hisotorial tratamiento con ID: {pk}.")

        return Response(
            {
                "message": f"Historial tratamiento con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )
