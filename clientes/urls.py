from django.urls import path

#importar metodos do views(controllers)
from .views import read, new, update, delete



urlpatterns = [
  path('read/', read, name = 'list'),
  path('new/', new, name="new"),
  path('update/<int:id>/', update, name="update"),
  path('delete/<int:id>/', delete, name="delete"),
] 