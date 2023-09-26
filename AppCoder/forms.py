from django import forms

class UsuarioFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    generoFavorito = forms.CharField()
    email = forms.EmailField()

    
