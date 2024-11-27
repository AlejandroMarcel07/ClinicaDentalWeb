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

from .serializers import TbExploracionClinicaSerializers
from .models import TbExploracionclinica

class TbExploracionClinicaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbExploracionclinica

    @swagger_auto_schema(
        responses={200: TbExploracionClinicaSerializers(many=True)}
    )
    def get(self, request):
        exploracionclinica = TbExploracionclinica.objects.all()
        serializer = TbExploracionClinicaSerializers(exploracionclinica, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {exploracionclinica.count()} exploraciones clinicas."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbExploracionClinicaSerializers,
        responses={201: TbExploracionClinicaSerializers}
    )
    def post(self, request):
        serializer = TbExploracionClinicaSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        exploracionclinica = serializer.save()
        logger.info(
            f"El usuario '{request.user}' creó una nueva exploracion clinia con ID: {exploracionclinica.id}.")
        return Response(
            {
                "message": "La exploracion clinica se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbExploracionClinicaSerializers,
        responses={200: TbExploracionClinicaSerializers}
    )
    def patch(self, request, pk):
        objeto_exploracion = get_object_or_404(TbExploracionclinica, id=pk)
        serializer = TbExploracionClinicaSerializers(objeto_exploracion, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"El usuario '{request.user}' actualizó la exploracion clinica con ID: {pk}.")
        return Response(
            {
                "message": "La exploracion clinica se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        objeto_exploracion = get_object_or_404(TbExploracionclinica, id=pk)
        nombre_exploracion = objeto_exploracion.tipo

        self.check_object_permissions(request, objeto_exploracion)
        objeto_exploracion.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó la exploracion clinica con ID: {pk}.")

        return Response(
            {
                "message": f"Exploracion clinica '{nombre_exploracion}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )