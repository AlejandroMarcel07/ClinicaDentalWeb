from django.urls import path, include
from Apps.Catalogos.tratamientosClinicos.views import TbTratamientoclinioApiView

urlpatterns = [
    path('tratamientosClinicos/', include('Apps.Catalogos.tratamientosClinicos.urls')),
    path('tratamientos/<int:pk>/', TbTratamientoclinioApiView.as_view()),
]
