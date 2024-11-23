from django.urls import path, include

urlpatterns = [
    path('tratamientosClinicos/', include('Apps.Catalogos.tratamientosClinicos.urls')),
    path('tiposDePago/', include('Apps.Catalogos.tiposDePagos.urls')),
]
