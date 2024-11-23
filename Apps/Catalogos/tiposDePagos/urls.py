from django.urls import path
from .views import TbTipoDePagoApiView

urlpatterns = [
    path("", TbTipoDePagoApiView.as_view(), name="tiposDePagos"),
    path('tipos/<int:pk>/', TbTipoDePagoApiView.as_view()),
]
