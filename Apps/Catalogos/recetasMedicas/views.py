from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
import logging

from .models import TbRecetamedica
from .serializer import TbRecetaMedicaSerializer
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbRecetaMedicaApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbRecetamedica

    @swagger_auto_schema(responses={200: TbRecetaMedicaSerializer(many=True)})
    def get(self, request):
        recetasmedicas = TbRecetamedica.objects.all()
        serializer = TbRecetaMedicaSerializer(recetasmedicas, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {recetasmedicas.count()} recetas medicas."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=TbRecetaMedicaSerializer, responses={201: TbRecetaMedicaSerializer})
    def post(self, request):
        serializer = TbRecetaMedicaSerializer(data=request.data)
        if serializer.is_valid():
            receta = serializer.save()
            logger.info(
                f"El usuario '{request.user}' creó una nueva receta medica con ID: {receta.id}.")
            return Response(
                {
                    "message": "La receta médica se insertó exitosamente.",
                    "data": receta.data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


    @swagger_auto_schema(
        request_body=TbRecetaMedicaSerializer,
        responses={200: TbRecetaMedicaSerializer}
    )
    def patch(self, request, pk):
        receta_medica = get_object_or_404(TbRecetamedica, id=pk)
        serializer = TbRecetaMedicaSerializer(receta_medica, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        receta = serializer.save()

        logger.info(
            f"El usuario '{request.user}' actualizó la receta medico con ID: {pk}.")

        return Response(
            {
                "message": "La receta medica se actualizo se actualizó exitosamente.",
                "data": receta.data
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        receta_medica = get_object_or_404(TbRecetamedica, id=pk)

        #Permite que se validen los permisos específicos sobre el objeto en cuestión
        self.check_object_permissions(request, receta_medica)
        receta_medica.delete()

        logger.info(
            f"El usuario '{request.user}' eliminó la receta medica con ID: {pk}.")

        return Response(
            {
                "message": f"La receta con id: {pk} a sido eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )
