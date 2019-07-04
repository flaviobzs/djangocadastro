"""exemplo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

#curso BASIQUINHO
from contas.views import home

#local do view(controller) e importa o método dele exemplo (PROPRIO)
from app_teste.views import index
#from app_teste.views import index, listar
from app_teste.views import listar, cadastro, atualizar, deletar


#importar URLs da APP clientes CRUD MÉDIO
from clientes import urls as clientes_urls
#from pessoas import urls as pessoas_urls


#importar função que tras urls de outro arquivo
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    #teste PROPRIO
    path('index/', index),
    path('', listar, name='listar'),
    path('criar/', cadastro, name='novo'),
    path('atualizar/<int:pk>', atualizar, name='atualizar'),
    path('deletar/<int:pk>', deletar, name='deletar'),
    
    #curso basiquinho
    path('home/', home),
    
    #CRUD médio
    path('pessoas/', include(clientes_urls)),
]
