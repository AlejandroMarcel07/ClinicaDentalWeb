from rest_framework import serializers
from decimal import Decimal
from .models import TbFactura
from ..estadosCuentas.models import TbEstadocuenta
from ..historialesClinicos.models import TbHistorialclinico
from ..historialesClinicosTratamiento.models import TbHistorialclinicotbTbTratamiento
from ..modalidadesDePagos.models import TbModalidaddepago
from ..montosDeDescuentos.models import TbMontodedescuento

class TbFacturaGetSerializer(serializers.ModelSerializer):
    nombretipdepago = serializers.CharField(source='idtipodepago.nombretipodepago', read_only=True )
    nombremontodescuento = serializers.CharField(source='idmontodedescuento.porcentajedescuento', read_only=True)
    nombremodalidadpago = serializers.CharField(source='idmodalidaddepago.nombremodalidad', read_only=True)
    nombreestado = serializers.CharField(source='idestadocuenta.nombreestado', read_only=True)

    class Meta:
        model = TbFactura
        fields = [
            "idfactura",
            "idcita",
            "costototal",
            "idtipodepago",
            "nombretipdepago",
            "descuentoaplicado",
            "idmontodedescuento",
            "nombremontodescuento",
            "totaldescuentoaplicado",
            "idmodalidaddepago",
            "nombremodalidadpago",
            "cantidadcuotas",
            "cuotaspagadas",
            "costoporcuota",
            "idestadocuenta",
            "nombreestado"
        ]


class TbFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbFactura
        fields = [
            "idcita",
            "idtipodepago",
            "idmodalidaddepago",
            "cantidadcuotas",
            "cuotaspagadas",
            "costoporcuota",
            "descuentoaplicado",
            "idmontodedescuento"
        ]

    def validate(self, data):

        historial_clinico = TbHistorialclinico.objects.filter(idcita=data['idcita']).first()
        if not historial_clinico:
            raise serializers.ValidationError("No existe un historial clínico asociado a la cita.")

        tratamientos = TbHistorialclinicotbTbTratamiento.objects.filter(idhistorialclinico=historial_clinico)
        if not tratamientos.exists():
            raise serializers.ValidationError("No existen tratamientos asociados al historial clínico.")


        costo_total = sum(tratamiento.precio for tratamiento in tratamientos)
        data['costototal'] = costo_total


        total_descuento_aplicado = None
        if data.get('descuentoaplicado'):  # Si se aplica descuento
            if not data.get('idmontodedescuento'):
                raise serializers.ValidationError("Debe proporcionar un monto de descuento si aplica descuento.")

            descuento = TbMontodedescuento.objects.filter(idmontodedescuento=data['idmontodedescuento']).first()
            if not descuento:
                raise serializers.ValidationError("El monto de descuento proporcionado no existe.")

            total_descuento_aplicado = costo_total * (Decimal(descuento.porcentajedescuento) / 100)
            costo_total -= total_descuento_aplicado  # Aplicar descuento al costo total
        else:  # Si no se aplica descuento
            data['idmontodedescuento'] = None
            total_descuento_aplicado = None

        # 4. Gestionar modalidad de pago
        modalidad = TbModalidaddepago.objects.filter(idmodalidaddepago=data['idmodalidaddepago'].idmodalidaddepago).first()

        if not modalidad:
            raise serializers.ValidationError("La modalidad de pago proporcionada no existe.")

        cantidad_cuotas = data.get('cantidadcuotas', 0)
        if modalidad.idmodalidaddepago == 1:  # Pago único
            data['cantidadcuotas'] = None
            data['cuotaspagadas'] = None
            data['costoporcuota'] = None

            estadocuenta = TbEstadocuenta.objects.filter(idestadocuenta=3).first()
            if not estadocuenta:
                raise serializers.ValidationError("El estado de cuenta no existe.")
            data['idestadocuenta'] = estadocuenta

        elif modalidad.idmodalidaddepago == 2:  # Pago en cuotas
            if cantidad_cuotas <= 0:
                raise serializers.ValidationError("La cantidad de cuotas debe ser mayor a 0 para pagos en cuotas.")

            # Dividir entre el costo total correcto
            costo_a_dividir = costo_total if not data.get(
                'descuentoaplicado') else costo_total + total_descuento_aplicado
            data['cuotaspagadas'] = 0
            data['costoporcuota'] = costo_a_dividir / cantidad_cuotas
            estadocuenta = TbEstadocuenta.objects.filter(idestadocuenta=1).first()
            if not estadocuenta:
                raise serializers.ValidationError("El estado de cuenta no existe.")
            data['idestadocuenta'] = estadocuenta
        else:
            raise serializers.ValidationError("Modalidad de pago no reconocida.")

        data['totaldescuentoaplicado'] = total_descuento_aplicado

        return data


