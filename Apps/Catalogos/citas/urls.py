from django.urls import path
from .views import TbCitaApiView,TbCitaProximasApiView

urlpatterns = [
    path("", TbCitaApiView.as_view(), name="citas"),
    path('citas/<int:pk>/', TbCitaApiView.as_view()),
    path('citasproximas/', TbCitaProximasApiView.as_view(), name='citas-proximas')
]

