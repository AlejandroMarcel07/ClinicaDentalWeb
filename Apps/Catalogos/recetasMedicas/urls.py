from django.urls import path
from .views import TbRecetaMedicaApiView


urlpatterns = [
    path("", TbRecetaMedicaApiView.as_view(), name="recetasMedicas"),
    path('recetas/<int:pk>/', TbRecetaMedicaApiView.as_view()),
]