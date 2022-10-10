"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from AppBlog.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('mensajes/', include('AppMensajes.urls')),

    path('', Home.as_view(), name='inicio'),
    path('articulos/<int:pk>', Articulo.as_view(), name='articulo'),
    path('crearPost/', CrearPost.as_view(), name='crearPost'),
    path('articulos/editar/<int:pk>', EditarPost.as_view(), name='editarPost'),
    path('articulos/<int:pk>/eliminar', EliminarPost.as_view(), name='eliminarPost'),
    path('categorias/<str:opciones>/', VerCategoria, name='categoria'),
    path('listaCategorias/', ListaCategoria, name='listaCategorias'),

    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarPerfilUsuario/', editarPerfilUsuario, name='editarPerfilUsuario'),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

