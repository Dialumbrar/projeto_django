from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cadastro_estoque', views.cadastro, name = 'cadastro_estoque'),
    path('lista_produto', views.lista_produto, name = 'lista_produto')
       
]