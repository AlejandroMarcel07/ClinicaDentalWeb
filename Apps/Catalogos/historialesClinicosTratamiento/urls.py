from django.urls import path
from .views import TbHistorialTratamientoClinicaApiView

urlpatterns = [
    path("", TbHistorialTratamientoClinicaApiView.as_view(), name="historialesClinicosTratamiento"),
    path('tratamiento/<int:pk>/', TbHistorialTratamientoClinicaApiView.as_view()),
]