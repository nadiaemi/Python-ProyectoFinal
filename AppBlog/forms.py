from django import forms
from .models import Categoria, Post


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