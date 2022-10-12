# Bueno Food Blog - Proyecto final de Python

<h2>Acerca del proyecto</h2>
En este proyecto creamos una aplicación estilo blog programada en Python y usando Django como framework. 
Aplicamos todos los conceptos proporcionados en el curso de Python: herencia de plantillas, modelos basados en clases y funciones, formularios, vistas, urls y demás herramientas complementarias que permiten realizar el CRUD de nuestro blog. Además, incorporamos la creación de una aplicación que permite la mensajería instantánea entre los usuarios registrados. 
Se trata de un blog de cocina, donde compartimos nuestras recetas favoritas. Podemos crear, eliminar, modificar las publicaciones siempre que estemos logueados. Cualquier otro que se registre puede también publicar sus platos preferidos.

Puedes ver el vídeo explicativo: https://drive.google.com/file/d/1fkbOEdHZXgndXzxG7Ogwa9eK44YCTaG3/view?usp=sharing

<h2>Funcionalidades</h2>
Desde la url http://127.0.0.1:8000/ podrás acceder a la página de inicio de AppBlog “Bueno”.
![image](https://user-images.githubusercontent.com/112612400/195231984-75f064a6-6cef-4ebd-8f94-6c0a848a1956.png)

<h4>Registro</h4>
En la barra del menú se encuentran los accesos que creamos en la App, deberás registrarte (http://127.0.0.1:8000/register/)  para iniciar sesión (http://127.0.0.1:8000/login/). 

![image](https://user-images.githubusercontent.com/112612400/195232189-947cc7da-a953-4c9d-9b46-4f14de1c431f.png)

![image](https://user-images.githubusercontent.com/112612400/195232230-e3483200-1ce3-4b67-b8af-79ad3723c800.png)

<h4>Iniciar Sesion</h4>
Una vez que inicies sesión, te daremos la bienvenida.

![image](https://user-images.githubusercontent.com/112612400/195232558-932f649a-651c-4379-bcb7-de1b362f2959.png)

<h4>Agregar imagen  y editar tu perfil</h4>
Podrás agregar una imagen de perfil http://127.0.0.1:8000/agregarAvatar/

![image](https://user-images.githubusercontent.com/112612400/195232656-2f62fca6-cbd5-4d41-8513-1b2c43cc867f.png)

![image](https://user-images.githubusercontent.com/112612400/195235212-eb16c66e-3545-4e30-a89a-c279cbc841fd.png)



...e incluso editar tu información (http://127.0.0.1:8000/editarPerfilUsuario/):


![image](https://user-images.githubusercontent.com/112612400/195232790-7dfab953-7073-43ca-874e-d2b6da2fb156.png)

<h4>Crear Post</h4>
Luego podrás navegar por el blog y agregar contenido si lo deseas clickeando en el botón “Crear Post”. Te dirigirá a la url : http://127.0.0.1:8000/crearPost/ y tendrás la opción de seleccionar la categoría de tu contenido, luego se pulsa enviar y te redirigirá a la página de inicio. Esto indica que el contenido fue agregado correctamente a la base de datos.

![image](https://user-images.githubusercontent.com/112612400/195232884-5f05b748-9364-40f5-a326-608c874f04c7.png)

<h4>Mensajería instantánea</h4>

Desde el botón “enviar mensaje a usuario” podrás comunicarte con los usuarios registrados en el blog (http://127.0.0.1:8000/mensajes/). 
![image](https://user-images.githubusercontent.com/112612400/195232952-9b3a3082-69d6-461d-aaa3-fa46aeebbce6.png)

<h4>Salir</h4>
Podrás desloguearte de la página con un click en “Salir”, te aparecerá un mensaje que confirma que te has deslogueado correctamente (http://127.0.0.1:8000/logout/). 

![image](https://user-images.githubusercontent.com/112612400/195233584-eb2c7b4c-986e-4bc1-9af2-27a512e8a5cd.png)

![image](https://user-images.githubusercontent.com/112612400/195233851-f2aa6a4d-e2e4-4fad-bee2-8f2e62a595a3.png)

<h4>Disfrutando el contenido</h4>
Recuerda que no es necesario que te registres para navegar y disfrutar de todo el contenido. Te invitamos a que visites “Categorías” http://127.0.0.1:8000/listaCategorias/, encontraras recetas fáciles y deliciosas!


![image](https://user-images.githubusercontent.com/112612400/195233477-cad12348-9894-498f-82a3-abd73a88f336.png)

<h2>Colaboradores</h2>
<strong>Nadia Cabral (https://github.com/nadiaemi) :</strong> Tuvo a cargo la creación de la app del blog, la cual permite crear una publicación, editarla y hasta eliminarla. E implementó la app de mensajería, donde se pueden listar las conversaciones con los demás usuarios registrados y crear nuevas conversaciones.

<strong> Mónica Mosquera (https://github.com/MonicaMoss):</strong> Realizó la app de usuarios: registración, login, logout, agregar el avatar, editar el perfil. Y la sección About, donde se cuenta acerca de las colaboradoras y del proyecto.
