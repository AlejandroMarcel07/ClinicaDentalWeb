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

from .serializers import TbTiposDePagosSerializes
from .models import TbTipodepago



class TbTipoDePagoApiView(APIView):

    #Nos permite antes de entrar a la clase que el usuario este permitido acceder alguna funcion
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbTipodepago  # Aquí definimos el modelo explícitamente

    @swagger_auto_schema(
        responses={200: TbTiposDePagosSerializes(many=True)}
    )
    def get(self, request):
        serializer = TbTiposDePagosSerializes(TbTipodepago.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @swagger_auto_schema(
        request_body=TbTiposDePagosSerializes,
        responses={201: TbTiposDePagosSerializes}
    )
    def post(self, request):
        serializer = TbTiposDePagosSerializes(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "La tipo de pago se inserto exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbTiposDePagosSerializes,
        responses={200: TbTiposDePagosSerializes}
    )
    def patch(self, request, pk):
        tipo_pago = get_object_or_404(TbTipodepago, idtipodepago=pk)
        serializer = TbTiposDePagosSerializes(tipo_pago, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "La tipo de pago se actualizó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        tipo_pago = get_object_or_404(TbTipodepago, idtipodepago=pk)
        nombre_tipo_pago = tipo_pago.nombretipodepago

        #Permite que se validen los permisos específicos sobre el objeto en cuestión
        self.check_object_permissions(request, tipo_pago)
        tipo_pago.delete()

        logger.info("Tipo de pago deleted successfully with ID: %s", pk)

        return Response(
            {
                "message": f"Tipo de pago '{nombre_tipo_pago}' con ID {pk} eliminado exitosamente."
            },
            status=status.HTTP_204_NO_CONTENT
        )

