from django import forms
from .models import Categoria, Post

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



opciones = Categoria.objects.all().values_list('nombre','nombre')
lista_opciones = []
for elemento in opciones:
    lista_opciones.append(elemento)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'autor', 'categoria', 'cuerpo', 'imagen_post')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=lista_opciones, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class EditarForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'categoria', 'cuerpo', 'imagen_post')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(choices=lista_opciones, attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
           
        }
        

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}



class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}    

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")