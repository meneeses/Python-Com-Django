from django.urls import path
from . import views

urlpatterns = [
    path('ver_formulario/', views.ver_formulario, name="ver_formulario")
]


