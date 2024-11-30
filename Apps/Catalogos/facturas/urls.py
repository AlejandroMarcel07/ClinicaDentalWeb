from django.urls import path
from .views import CrearFactura

urlpatterns = [
    path("", CrearFactura.as_view(), name="factura"),
    path('facturaeliminar/<int:pk>/', CrearFactura.as_view()),
]

