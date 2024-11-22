from django.urls import path, include

urlpatterns = [
    path('tratamientosClinicos/', include('Apps.Catalogos.tratamientosClinicos.urls')),
]
