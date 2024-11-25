from django.urls import path
from .views import TbGeneroApiView

urlpatterns = [
    path("", TbGeneroApiView.as_view(), name="generos"),
    path('generos/<int:pk>/', TbGeneroApiView.as_view()),
]