from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index_cliente'),
    path('cadastro', views.cadastro, name = 'cadastro_cliente'),
    path('criar/', views.criar, name = 'criar_cliente'),
    path('listar', views.listar, name = 'listar_cliente'),
    path('deletar/<int:id_cliente>', views.deletar, name='deletar_cliente'),
    path('editar/<int:id_cliente>', views.editar, name='editar_cliente'),
    path('atualizar', views.atualizar, name='atualizar_cliente')

]