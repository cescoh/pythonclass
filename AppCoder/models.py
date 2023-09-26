from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Edad = models.IntegerField()
    generoPrincipal = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fechaDePublicacion = models.DateField()
    precio = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    generoFavorito = models.CharField(max_length=50)
    email = models.EmailField()



