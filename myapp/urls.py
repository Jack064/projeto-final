from django.urls import path 
from myapp import views
from .views import cadastro, salvar, editar, update, apagar, logout

urlpatterns = [
    path('', views.mysite, name='mysite'), 
    path('cadastro.html', cadastro),
    path('salvar/', salvar, name = "salvar"),
    path('editar/<int:id>', editar, name = "editar"),
    path('update/<int:id>', update, name = "update"),
    path('apagar/<int:id>', apagar, name = "apagar"),
    path('logout.html', logout),
]