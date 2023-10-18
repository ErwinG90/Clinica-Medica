from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('lista_registro', lista_registro, name="lista_registro"),
    path('registro', registro, name="registro"),
    path('registro_medico', registro_medico, name="registro_medico"),
    path('pacientes', Pacientes, name="pacientes"),
    path('medicos', medicos, name="medicos"),






    path('vista', mi_vista, name="vista"),

]
