from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Post
from .forms import PostForm, EditarForm
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


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

class CrearPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'crearPost.html'
	#fields = '__all__'

class EditarPost(UpdateView):
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

			usuario=authenticate(username=usu, password=clave)
			if usuario is not None:
				login(request, usuario)
				return render(request, "inicio.html", {"mensaje":f"Estamos felices {usuario} que hagas parte de nuestro Blog"})
			else:
				return render (request, "login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
		else:
			return render (request, "login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
	else:
		form=AuthenticationForm()
		return render (request, "login.html", {"formulario":form})
