from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('personas/', views.persona, name = 'personas'),
    path('servicios/', views.servicio, name = 'servicios'),
    path('mascotas/', views.mascota, name = 'mascotas'),

    path('registrarPersona/', views.regPersona, name = 'registrarPersona'),
    path('eliminarPersona/<nombre>', views.eliminarPersona, name = 'eliminarPersona'),

    path('registrarServicio/', views.regServicio, name = 'registrarServicio'),
    path('eliminarServicio/<servicio>', views.eliminarServicio, name = 'eliminarServicio'),

    path('registrarMascota/', views.regMascota, name = 'registrarMascota'),
    path('eliminarMascota/<nombre>', views.eliminarMascota, name = 'eliminarMascota'),
    
    path('buscarServicio/<nombre>', views.buscarServicio, name = 'buscarServicio'),


    ]