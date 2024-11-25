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

from .serializers import TbGeneroSerializers
from .models import TbGenero

class TbGeneroApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbGenero

    @swagger_auto_schema(
        responses={200: TbGeneroSerializers(many=True)}
    )
    def get(self, request):
        serializer = TbGeneroSerializers(TbGenero.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(
        request_body=TbGeneroSerializers,
        responses={201: TbGeneroSerializers}
    )
    def post(self, request):
        serializer = TbGeneroSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "El genero se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=TbGeneroSerializers,
        responses={200: TbGeneroSerializers}
    )
    def patch(self, request, pk):
        id_genero = get_object_or_404(TbGenero, id=pk)
        serializer = TbGeneroSerializers(id_genero, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "EL genero  se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        objeto_genero = get_object_or_404(TbGenero, id=pk)
        nombre_genero = objeto_genero.genero

        self.check_object_permissions(request, objeto_genero)
        objeto_genero.delete()

        logger.info("Genero deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Genero '{nombre_genero}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )

