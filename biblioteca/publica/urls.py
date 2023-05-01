from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('hola_mundo', views.hola_mundo, name='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    
    path('libros/', views.libros, name='libros'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('admin', views.admin, name='admin'),
]
