"""teste URL Configuration

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
#local do view(controller) e importa o método dele
from app_teste.views import index
from app_teste.views import listar, cadastro, atualizar, deletar
#from app_teste.views import index, listar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('', listar, name='listar'),
    path('criar/', cadastro, name='novo'),
    path('atualizar/<int:pk>', atualizar, name='atualizar'),
    path('deletar/<int:pk>', deletar, name='deletar'),
]

