from django.urls import path
from .views import TbMontoDeDescuentoApiView

urlpatterns = [
    path("", TbMontoDeDescuentoApiView.as_view(), name="montosDeDescuentos"),
    path('montos/<int:pk>/', TbMontoDeDescuentoApiView.as_view()),
]
