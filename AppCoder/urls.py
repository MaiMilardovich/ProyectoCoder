from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView   #Para logout solo creamos urls y template

urlpatterns = [
    path("", inicio , name= "Inicio"),
    #path("cursos/" , cursos, name = "Cursos"),
    path("estudiantes/" , estudiantes, name = "Estudiantes"),
    #path("profesores/" , profesores, name = "Profesores"),
    path("entregables/" , entregables , name= "Entregables"),
    path("form1/" , formulario1),
    path("form2/" , formulario2 , name= "FormularioProfe"),
    path("buscarCursos/", busquedaCursos),
    path("buscar/", buscar),
    path("leerProfes", leerProfesores, name = "LeerProfes"),
    path("borrarProfes/<profeNombre>" , borrarProfesores , name ="EliminarProfesores"),
    path("editarProfes/<profeNombre>", editarProfesores , name = "EditarProfesores"),
    path("login" , iniciar_sesion , name="Login"),
    path("registro" , registro , name="Registro"),
    path("logout" , LogoutView.as_view (template_name="AppCoder/logout.html") , name="Logout"),
    
    #Vistas basadas en clases

    path("cursos/" , CursoLista.as_view() , name ="Cursos"),
    path("cursos/nuevo" , CursoCrear.as_view(), name = "CrearCursos"),
    path("cursos/<int:pk>" , CursoDetalle.as_view(), name = "DetalleCursos"),
    path("cursos/editar/<int:pk>" , CursoUpdate.as_view(), name = "ActualizarCursos"),
    path("cursos/borrar/<int:pk>" , CursoBorrar.as_view(), name = "BorrarCursos"),



]