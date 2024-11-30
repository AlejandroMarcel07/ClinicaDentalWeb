from django.db.models import Avg, Min, Max, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
import logging

from .models import TbPaciente
from .serializers import TbPacienteSerializer, TbPacienteEstadisticasSerializer
from ...Seguridad.permissions import CustomPermission

# Configura el logger
logger = logging.getLogger(__name__)

class TbPacienteApiView(APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbPaciente

    @swagger_auto_schema(responses={200: TbPacienteSerializer(many=True)})
    def get(self, request):
        pacientes = TbPaciente.objects.filter(isdeleted=False)
        serializer = TbPacienteSerializer(pacientes, many=True)
        logger.info(
            f"El usuario '{request.user}' recuperó {pacientes.count()} pacientes."
        )
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    @swagger_auto_schema(
        request_body=TbPacienteSerializer,
        responses={201: TbPacienteSerializer}
    )
    def post(self, request):
        serializer = TbPacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        paciente = serializer.save()

        logger.info(
            f"El usuario '{request.user}' creó un nuevo paciente con ID: {paciente.id}.")

        return Response(
            {
                "message": "El paciente se creó exitosamente.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )


    @swagger_auto_schema(
        request_body=TbPacienteSerializer,
        responses={200: TbPacienteSerializer}
    )
    def patch(self, request, pk):
        paciente = get_object_or_404(TbPaciente, id=pk)
        serializer = TbPacienteSerializer(paciente, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        logger.info(
            f"El usuario '{request.user}' actualizó un paciente con ID: {pk}.")
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

        logger.info(
            f"El usuario '{request.user}' eliminó un paciente con ID: {pk}.")

        return Response(
            {
                "message": f"Paciente {nombre_paciente} con ID {pk} eliminado de forma lógica."
            },
            status=status.HTTP_204_NO_CONTENT
        )


class TbPacienteEstadisticaApiView(APIView):

    permission_classes = [IsAuthenticated, CustomPermission]
    model = TbPaciente

    @swagger_auto_schema(responses={200: TbPacienteEstadisticasSerializer})
    def get(self, request):
        pacientes_activos = TbPaciente.objects.filter(isdeleted=False)
        pacientes_borrados = TbPaciente.objects.filter(isdeleted=True)

        total_activos = pacientes_activos.count()
        total_borrados = pacientes_borrados.count()
        hombres = pacientes_activos.filter(idgenero__genero="Masculino").count()
        mujeres = pacientes_activos.filter(idgenero__genero="Femenino").count()

        edades = pacientes_activos.aggregate(
            promedio_edad=Avg('edad'),
            edad_minima=Min('edad'),
            edad_maxima=Max('edad')
        )

        # Rangos de edad
        rangos_edades = {
            "niños (0-12)": pacientes_activos.filter(edad__lte=12).count(),
            "jóvenes (13-35)": pacientes_activos.filter(edad__gte=13, edad__lte=35).count(),
            "señores (36+)": pacientes_activos.filter(edad__gte=36).count(),
        }

        # Ocupaciones comunes
        ocupaciones_comunes = (
            pacientes_activos.values('ocupacion')
            .annotate(cantidad=Count('ocupacion'))
            .order_by('-cantidad')[:3]
        )

        # Pacientes sin antecedentes
        sin_antecedentes = pacientes_activos.filter(antecedentes__isnull=True).count()

        # Construir la respuesta
        estadisticas = {
            "total_activos": total_activos,
            "total_borrados": total_borrados,
            "hombres": hombres,
            "mujeres": mujeres,
            "edades": edades,
            "rangos_edades": rangos_edades,
            "ocupaciones_comunes": list(ocupaciones_comunes),
            "sin_antecedentes": sin_antecedentes,
        }

        serializer = TbPacienteEstadisticasSerializer(estadisticas)
        return Response(serializer.data, status=status.HTTP_200_OK)
