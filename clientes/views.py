from django.shortcuts import render, redirect, get_object_or_404

#importar modelo de tabela (Equipe)
from .models import Person
#importar a ferramenta do DJANGO para criar formularios automaticamente na view
#importar o modelo de formulario automatico do django
from .form import PersonForm


# Create your views here.
def read(request):
    #1º forma de passar os dados para a view
    #dado = {}   
    # --> nome da variavel é "dado"
    #dado['person'] = Person.objects.all()
    #dado['person'] = Equipe.objects.filter()

    #2º forma de passar dados
    
    persons = Equipe.objects.all()

    #forma de passar dados 
    #return render(request, 'clientes/listar.html', dado)
    return render(request, 'clientes/listar.html', {'persons':persons})

def new(request):
  #instanciar um formulario vazio e passar para a view
  #form - PersonForm()

  #instanciar um formulario preenchido
  #form - PersonForm(request.POST)
  #manda o formulario vazio ou preenchido
  #form = PersonForm(request.POST or None)
  #pegar arquivos da requisição
  #form = PersonForm(request.FILES)
  form = PersonForm(request.POST or None, request.FILES or None)

  #validação do formulario
  if form.is_valid():
    #transformar dados da requisição do formulario em objeto (salvaldo)
      form.save()
      return redirect('list')
  return render(request, 'clientes/new.html', {'form': form})

def update(request, id):
  #pegar um objeto que o usuario está mandando, senao encontrar manda um erro 404
    person = get_object_or_404(Person, pk=id)

    #passar os dados de uma pessoa que foi instanciada (instance=person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})

def delete(request, id):
    person = get_object_or_404(Person, pk=id)

    #verificação 
    #if request.method == 'POST':
    #    person.delete()
    #    return redirect('person_list')

    person.delete()
    return redirect('list')

      #verificar para outra aba
    #return render(request, 'person_delete_confirm.html', {'person': person})

    #https://github.com/Gpzim98/gestao_clientes/blob/master/clientes/views.py