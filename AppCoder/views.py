from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Curso , Entregable
from django.http import HttpResponse

# Create your views here.

def curso(request):

    materia = Curso(nombre= "Disenio web", camada=12345)

    materia.save()

    return HttpResponse(f"Estoy guardando el primer curso.{materia.nombre}")


def entregables(request):

    ente1 = Entregable(nombre="Examen1" , fechaEntrega="2022-09-08")

    ente1.save()

    return HttpResponse(f"He guardado {ente1.nombre} con fecha de entrega {ente1.fechaEntrega}")

