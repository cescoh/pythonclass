from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path('usuario/', usuario, name="Usuario"),
    path('book/', book, name="Libros"),
    path('autor/', autor, name= "Autor"),
    path('usuarioFormulario/', usuarioFormulario, name= "FormularioUsuario"),
    path('buscarUsuario/', busquedaUsuario, name="BuscarUsuario"),
    path('resultados/', resultados, name="ResultadosBusqueda"),
    
    
]
