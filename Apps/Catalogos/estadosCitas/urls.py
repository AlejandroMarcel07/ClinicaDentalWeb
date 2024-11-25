from django.urls import path
from .views import TbEstadoCitaApiView

urlpatterns = [
    path("", TbEstadoCitaApiView.as_view(), name="estadosCitas"),
    path('estados/<int:pk>/', TbEstadoCitaApiView.as_view()),
]