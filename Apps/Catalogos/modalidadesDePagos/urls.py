from django.urls import path
from .views import TbModalidaddePagoApiView

urlpatterns = [
    path("", TbModalidaddePagoApiView.as_view(), name="modalidadesDePagos"),
    path('modalidades/<int:pk>/', TbModalidaddePagoApiView.as_view()),
]
