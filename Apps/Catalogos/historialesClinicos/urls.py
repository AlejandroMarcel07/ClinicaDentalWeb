from .views import TbHistorialClinicoApiView, DetalleHistorialClinicoView
from django.urls import path

urlpatterns = [
 path("", TbHistorialClinicoApiView.as_view(), name="historialesClinicos"),
 path('historialId/<int:pk>/', DetalleHistorialClinicoView.as_view(), name='detalle_historialclinico'),
 path('historiales/<int:pk>/', TbHistorialClinicoApiView.as_view()),
]
