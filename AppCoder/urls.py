from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path("", inicio , name= "Inicio"),
    path("cursos/" , cursos),
    path("estudiantes/" , estudiantes),
    path("profesores/" , profesores),
    path("entregables/" , entregables , name= "Entregables"),

    
]