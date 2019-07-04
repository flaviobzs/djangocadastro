from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
  #now = datetime.datetime.now()
  #html = "<html><body> It is now %s. </html></body>" % now
  #return HttpResponse(html)
  data = {}

  data['now'] = datetime.datetime.now()
  data['transacoes'] = ['t2', 't4', 't1', 't5']


  return render(request, 'contas/home.html', data)