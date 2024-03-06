from django.shortcuts import render
from .models import Estoque

def index(request):
    return render(request,'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def lista_produto(request):
    lista_produto = Estoque.objects.all()
    return render(request, 'lista_produto.html', {'lista_produto': lista_produto})
