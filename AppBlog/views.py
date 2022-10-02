from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Post
from .forms import PostForm, EditarForm
from django.urls import reverse_lazy

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
