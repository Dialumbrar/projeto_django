from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_estoque, name = 'index_estoque'),
    path('cadastro', views.cadastro_estoque, name = 'cadastro_estoque'),
    path('lista_produto', views.lista_produto, name = 'lista_produto'),
    path('criar/estoque', views.criar, name = 'criar_produto'),

]