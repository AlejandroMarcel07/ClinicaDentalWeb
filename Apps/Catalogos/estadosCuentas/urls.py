from django.urls import path
from .views import TbEstadoCuentaApiView

urlpatterns = [
    path("", TbEstadoCuentaApiView.as_view(), name="estadosCuentas"),
    path('estados/<int:pk>/', TbEstadoCuentaApiView.as_view()),
]