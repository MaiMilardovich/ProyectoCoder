from django.db import models

# Create your models here.


class Curso (models.Model):

    def __str__(self):
        return f"El curso es de {self.nombre}"

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

 
class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()


class Profesor(models.Model):

    def __str__(self):
        return f"Profesor {self.nombre} {self.apellido}"
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    profesion = models.CharField(max_length=60)


class Entregable(models.Model):
    
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()


