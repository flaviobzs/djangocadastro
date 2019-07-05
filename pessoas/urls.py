from django.urls import path

#importar metodos do views(controllers)
from .views import read, new, update, delete

urlpatterns = [
  #url que será direcionada após login
  path('read/', read, name = 'reading'),
  path('new/', new, name="creating"),
  path('update/<int:id>/', update, name="updating"),
  path('delete/<int:id>/', delete, name="deleting"),
]