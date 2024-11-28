from django.urls import path, include

urlpatterns = [
    path('tratamientosClinicos/', include('Apps.Catalogos.tratamientosClinicos.urls')),
    path('tiposDePago/', include('Apps.Catalogos.tiposDePagos.urls')),
    path('modalidadesdePago/', include('Apps.Catalogos.modalidadesDePagos.urls')),
    path('montosdedescuento/', include('Apps.Catalogos.montosDeDescuentos.urls')),
    path('generos/', include('Apps.Catalogos.generos.urls')),
    path('exploracionesclinicas/', include('Apps.Catalogos.exploracionesClinicas.urls')),
    path('estadoscuentas/', include('Apps.Catalogos.estadosCuentas.urls')),
    path('estadoscitas/', include('Apps.Catalogos.estadosCitas.urls')),
    path('pacientes/', include('Apps.Catalogos.pacientes.urls')),
    path('citas/', include('Apps.Catalogos.citas.urls')),
    path('recetasmedicas/', include('Apps.Catalogos.recetasMedicas.urls')),
    path('historialesclinicos/', include('Apps.Catalogos.historialesClinicos.urls')),
    path('historialesexploracion/', include('Apps.Catalogos.historialesClinicosExploracionClinica.urls')),
]
