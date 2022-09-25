from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import * 
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio (request):

    return render(request , "AppCoder/inicio.html" , {"mensaje":f"Bienvenidos!"})


def estudiantes (request):
    
     return render(request , "AppCoder/estudiantes.html")

"""
def profesores (request):
    
     return render(request , "AppCoder/profesores.html")
"""

def cursos(request):

    #materia = Curso(nombre= "Disenio web", camada=12345)

    #materia.save()

    return render(request , "AppCoder/cursos.html")

@login_required
def entregables(request):

    #ente1 = Entregable(nombre="Examen1" , fechaEntrega="2022-09-08")

    #ente1.save()

    return render(request , "AppCoder/entregables.html")


def formulario1(request):

    if request.method == "POST": #Si le doy a Enviar Informacion

        formulario1 = FormularioCurso (request.POST)

        if formulario1.is_valid(): # comprobar que no hay errores

            info = formulario1.cleaned_data

            cursoF = Curso(nombre=info["curso"], camada=info["camada"]) #lee la info de las cajas de texto

            cursoF.save() # guarda los datos en la base de datos

            return render(request, "AppCoder/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info

    else:

        formulario1=FormularioCurso() #mostrar formulario vacio
    
    return render(request, "AppCoder/form1.html", {"form1":formulario1}) # Apenas entro al URL


def formulario2(request):
    if request.method == "POST": #Si le doy a Enviar Informacion

        formulario2 = FormularioProfe (request.POST)

        if formulario2.is_valid(): # comprobar que no hay errores

            info = formulario2.cleaned_data

            profeF = Profesor(nombre=info["nombre"],apellido=info["apellido"],correo=info["correo"],profesion=info["profesion"]) #lee la info de las cajas de texto

            profeF.save() # guarda los datos en la base de datos

            return render(request, "AppCoder/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info

    else:

        formulario2=FormularioProfe() #mostrar formulario vacio
    
    return render(request, "AppCoder/form2.html", {"form2":formulario2}) # Apenas entro al URL


def busquedaCursos (request):

    return render (request, "AppCoder/busquedaCursos.html")


def buscar (request):

    if request.GET["camada"]:

        busqueda = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=busqueda)

        return render(request, "AppCoder/resultados.html" , {"cursos": cursos , "busqueda": busqueda})

    else:

        mensaje = "No enviaste datos"

    return HttpResponse(mensaje)


def leerProfesores (request):

    teachers = Profesor.objects.all()    #Leyendo todos los profesores creados

    return render (request, "AppCoder/profesores.html", {"teachers": teachers})  #Lo pasamos como conexto (dict) a la plantilla


def borrarProfesores (request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)

    profesor.delete()

    teachers = Profesor.objects.all()

    return render (request, "AppCoder/profesores.html", {"teachers": teachers}) 


def editarProfesores (request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)

    if request.method == "POST":
       
        formulario2 = FormularioProfe (request.POST)

        if formulario2.is_valid(): # comprobar que no hay errores

            info = formulario2.cleaned_data

            profesor.nombre = info["nombre"] #actualizar la info antigua por la que aparece en la caja de texto
            profesor.apellido = info["apellido"] #Entre [] corresponde al form 
            profesor.correo = info["correo"]
            profesor.profesion = info["profesion"]

            profesor.save()

            return render(request, "AppCoder/inicio.html") # vuelve a mostrar lo que le digo dps de darle enviar a la info

    else:

        formulario2=FormularioProfe(initial= {"nombre": profesor.nombre , "apellido":profesor.apellido, "correo": profesor.correo , "profesion": profesor.profesion }) #mostrar formulario con los datos (ya no vacio)
    
    return render(request, "AppCoder/editarProfes.html", {"form2":formulario2, "profeNombre": profeNombre })


#VISTAS CREADAS A PARTIR DE CLASES - CRUD

class CursoLista (ListView): #R de Crud
    model = Curso
    #template_name = "AppCoder/listaCursos.html" 
    #Si llamo al template nombremodelo_list no necesito agregar esta linea

class CursoCrear(CreateView): #C de Crud
    model = Curso
    success_url = "/AppCoder/cursos"
    fields = ["nombre" , "camada"]

class CursoDetalle(DetailView): #Detail es una especie de READ
    model = Curso

class CursoUpdate(UpdateView):
    model= Curso
    success_url = "/AppCoder/cursos"
    fields = ["nombre" , "camada"]

class CursoBorrar(DeleteView):
    model= Curso
    success_url = "/AppCoder/cursos"


#Iniciar sesion

def iniciar_sesion(request):

    if request.method == "POST": #Click al boton inciiar sesion

        form =  AuthenticationForm (request, data=request.POST)

        if form.is_valid(): # comprobar que no hay errores

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user: # usuario existe 

                login(request, user)

                return render(request, "AppCoder/inicio.html" , {"mensaje":f"Hola {user}"})

        else: #datos incorrectos

            return render(request, "AppCoder/inicio.html" , {"mensaje": f"Datos incorrectos"})

    else: 

        form = AuthenticationForm ()

    return render (request, "AppCoder/login.html", {"form": form})


def registro(request):

    if request.method == "POST":

        form = FormularioRegistro(request.POST)

        # form = UserCreationForm(request.POST) --> ANTES DE CREAR UN FORM EN froms.py

        if form.is_valid():

            nombreUsuario = form.cleaned_data["username"]

            form.save()

            return render (request, "AppCoder/inicio.html" , {"mensaje":f"Usuario {nombreUsuario} creado"})

    else:

        form = FormularioRegistro()
        # form = UserCreationForm() --> ANTES DE CREAR UN FORM EN froms.py
    
    return render(request, "AppCoder/registro.html", {"form" : form})


# contraseña123 es la contra que use en los usuarios