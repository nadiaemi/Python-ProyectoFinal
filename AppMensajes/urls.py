from django.urls import path
from AppMensajes.views import *

urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('mensajes/<username>', Directs, name='directs'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),


]