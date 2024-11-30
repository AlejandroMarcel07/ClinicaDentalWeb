from django.urls import path
from .views import TbDetalleFacturaApiView

urlpatterns = [
    path("", TbDetalleFacturaApiView.as_view(), name="detallesFacturas"),
]

