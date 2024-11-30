from django.urls import path
from .views import TbPacienteApiView, TbPacienteEstadisticaApiView


urlpatterns = [
    path("", TbPacienteApiView.as_view(), name="pacientes"),
    path("pacienteestadistica/", TbPacienteEstadisticaApiView.as_view(), name="pacientes"),
    path('pacientes/<int:pk>/', TbPacienteApiView.as_view()),
]