from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso , Entregable
from django.http import HttpResponse

# Create your views here.

def inicio (request):

    return render(request , "AppCoder/inicio.html")


def estudiantes (request):
    
     return render(request , "AppCoder/estudiantes.html")


def profesores (request):
    
     return render(request , "AppCoder/profesores.html")


def cursos(request):

    materia = Curso(nombre= "Disenio web", camada=12345)

    materia.save()

    return render(request , "AppCoder/cursos.html")


def entregables(request):

    ente1 = Entregable(nombre="Examen1" , fechaEntrega="2022-09-08")

    ente1.save()

    return render(request , "AppCoder/entregables.html")

