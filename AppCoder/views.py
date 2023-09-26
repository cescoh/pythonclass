from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, "AppCoder/inicio.html")

def usuario(request):

    user1 = Usuario(nombre="Carlos", apellido="jua", edad=78, generoFavorito ="Terror", email="npc@gmailfornpcs.com")
    user1.save()

    return render(request, "AppCoder/usuario.html")

def book(request):

    return render(request, "AppCoder/book.html")

def autor(request):

    return render(request, "AppCoder/autor.html")

def usuarioFormulario(request):
    if request.method == "POST": #despues de dar click al boton enviar

        formulario1 = UsuarioFormulario(request.POST)

        if formulario1.is_valid():
            info = formulario1.cleaned_data

            usuario = Usuario(nombre=info["nombre"], apellido=info["apellido"], edad=info["edad"],generoFavorito=info["generoFavorito"],email=info["email"])

            usuario.save()

            return render(request, "AppCoder/inicio.html")
    else:
    
        formulario1 = UsuarioFormulario()

    return render(request, "AppCoder/usuarioFormulario.html", {"form1": formulario1})

def busquedaUsuario(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/inicio.html", {"usuarios":usuarios, "nombre":nombre})
    
    else:

        respuesta = "No enviaste datos."


    return HttpResponse(respuesta)