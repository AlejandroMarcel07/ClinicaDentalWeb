from django.urls import path
from .views import TbCitaApiView

urlpatterns = [
    path("", TbCitaApiView.as_view(), name="citas"),
    path('citas/<int:pk>/', TbCitaApiView.as_view()),
]

