from django.shortcuts import render
from .models import Estoque

def index(request):
    return render(request,'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def lista_produto(request):
    return render(request, 'lista_produto.html')
