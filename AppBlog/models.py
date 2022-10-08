from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = RichTextField(blank=True, null=True)
    fecha_post = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=100, default='postres')
    imagen_post = models.ImageField(null=True, blank=True, upload_to='imagenes/')

    def __str__(self):
        return self.titulo+' | '+str(self.autor)

    def get_absolute_url(self):
        return reverse ('inicio')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse ('inicio')


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares")
