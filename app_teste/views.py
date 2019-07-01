from django.shortcuts import render, redirect

#importar modelo de tabela (Equipe)
from .models import Equipe

#importar a ferramenta do DJANGO para criar formularios automaticamente na view
from .form import EquipeForm

# Create your views here.
def index(request):
    return render(request, 'app_teste/index.html')

def listar(request):

    dado = {}
    dado['equipes'] = Equipe.objects.all()
    #dado['equipe'] = Equipe.objects.filter()

    return render(request, 'app_teste/listar.html', dado)


def cadastro(request):
    #form = EquipeForm()

    #verificar e apresentar !!    (se tem algo preenchido no padrao de formulario pré definido do django)
    form = EquipeForm(request.POST or None)

    #se as informações do formulario na hora do cadastro for valido, será salva no BD e redirecionado para a listagem
    if form.is_valid():
        form.save()
        return redirect('listar')
    #senão será apresentado o formulario novamente 
    return render(request, 'app_teste/criar.html', {'form': form})


def atualizar(request, pk):
    #localizar o ID do objeto as ser modificado
    equipe = Equipe.objects.get(pk=pk)

    #apresentação do modelo de formulario passando os dados do objeto buscado para ser atualizado
    form = EquipeForm(request.POST or None, instance=equipe)

    #se as informações do formulario na hora da atualização for valido, será salva no BD e redirecionado para a listagem
    if form.is_valid():
        form.save()
        return redirect('listar')

    #senão será apresentado o formulario novamente 
    return render(request, 'app_teste/criar.html', {'form': form})

def deletar(request, pk):
    #localizar o ID do objeto as ser deletado
    equipe = Equipe.objects.get(pk=pk)
    #deletar objeto
    equipe.delete()
    return redirect('listar')
    
    

