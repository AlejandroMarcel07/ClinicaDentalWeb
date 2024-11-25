from django.urls import path
from .views import TbExploracionClinicaApiView

urlpatterns = [
    path("", TbExploracionClinicaApiView.as_view(), name="exploracionesClinicas"),
    path('exploraciones/<int:pk>/', TbExploracionClinicaApiView.as_view()),
]