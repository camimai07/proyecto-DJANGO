from django.urls import path
from . import views

urlpatterns = [
    path('Hola_mundo', views.hola_mundo, name='hola'),
]