from .views import TbTratamientoclinioApiView
from django.urls import path

urlpatterns = [
 path("", TbTratamientoclinioApiView.as_view(), name="tratamientosClinicos")
]
