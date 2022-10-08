from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Post, Avatar
from .forms import PostForm, EditarForm, UserRegisterForm
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

#def inicio(request):
	#return render(request, 'index.html')

class Home(ListView):
	model = Post
	template_name = 'inicio.html'
	ordering = ['-fecha_post']

	def get_context_data(self, *args, **kwargs):
		categoria_menu = Categoria.objects.all()
		contexto = super(Home, self).get_context_data(*args, **kwargs)
		contexto['categoria_menu'] = categoria_menu
		return contexto

class Articulo(DetailView):
	model = Post
	template_name = 'articulos.html'

class CrearPost(LoginRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'crearPost.html'
	#fields = '__all__'

class EditarPost(LoginRequiredMixin, UpdateView):
	model = Post
	form_class = EditarForm
	template_name = 'editarPost.html'

class EliminarPost(DeleteView):
	model = Post
	template_name = 'eliminarPost.html'
	success_url = reverse_lazy('inicio')
	
def VerCategoria(request, opciones):
	categorias_posts = Post.objects.filter(categoria=opciones)
	return render (request, 'categorias.html', {'opciones': opciones.title(), 'categorias_posts': categorias_posts})

def ListaCategoria(request):
	lista_categoria = Categoria.objects.all()
	return render (request, 'listaCategorias.html', {'lista_categoria': lista_categoria})

def login_request(request):
	if request.method=="POST":
		form=AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			usu=request.POST["username"]
			clave=request.POST["password"]

			usuario=authenticate(username=usu, password=clave)#si esxiste me trae usuario, si no existe, no trae nada
			if usuario is not None:
				login(request, usuario)#si el usuario es correcto#
				return render(request, "inicio.html", {"mensaje":f"Hola {usuario} "})
			else:#si el usuario no es correcto
				return render(request, "login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
		else:
			return render(request, "login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
	else:
		form=AuthenticationForm()
		return render(request, "login.html", {"formulario":form})



def register(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get("username")
			form.save()
			return render(request, "inicio.html", {"mensaje":f"El Usuario {username} se ha creado correctamente"})
		else:
			return render(request, "register.html", {"formulario":form, "mensaje":"Formulario Inválido"})
	else:
		form=UserRegisterForm()
		return render(request, "register.html", {"formulario":form})


@login_required
def editarPerfilUsuario(request):
	usuario=request.user
	if request.method=="POST":
		form=UserEditForm(request.POST)
		if form.is_valid():
			info=form.cleaned_data
			usuario.email=info["email"]
			usuario.password1=info["password1"]
			usuario.password2=info["password2"]
			usuario.first_name=info["first_name"]
			usuario.first_name=info["first_name"]
			usuario.save()
			return render(request, "inicio.html", {"mensaje":"Tu perfil se ha editado correctamente"})
		else:
			return render(request, "editarPerfilUsuario.html", {"formulario":form, "usuario":usuario, "mensaje":"Datos incorrectos"})
	else:
		form= UserEditForm(instance=usuario)
	return render(request, "editarPerfilUsuario.html", {"formulario":form, "usuario":usuario})

