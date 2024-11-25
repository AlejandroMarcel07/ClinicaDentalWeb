from django.urls import path
from .views import TbPacienteApiView
from ..generos.views import TbGeneroApiView

urlpatterns = [
    path("", TbPacienteApiView.as_view(), name="pacientes"),
    path('pacientes/<int:pk>/', TbPacienteApiView.as_view()),
]