from .views import TbHistorialClinicoApiView
from django.urls import path

urlpatterns = [
 path("", TbHistorialClinicoApiView.as_view(), name="historialesClinicos"),
 path('historiales/<int:pk>/', TbHistorialClinicoApiView.as_view()),
]
