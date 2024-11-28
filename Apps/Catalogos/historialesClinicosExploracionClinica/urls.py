from django.urls import path
from .views import TbHistorialExploracionClinicaApiView

urlpatterns = [
    path("", TbHistorialExploracionClinicaApiView.as_view(), name="historialesClinicosExploracionClinica"),
    path('exploraciones/<int:pk>/', TbHistorialExploracionClinicaApiView.as_view()),
]