from django.shortcuts import render, redirect, get_object_or_404
from .models import Estoque

def index_estoque(request):
    return render(request,'index_estoque.html')

def cadastro_estoque(request):
    return render(request, 'cadastro_estoque.html')

def lista_produto(request):
    lista_produto = Estoque.objects.all()
    return render(request, 'lista_produto.html', {'lista_produto': lista_produto})

def criar(request):
    nome_produto = request.POST['nome_produto']
    descricao = request.POST['descricao']
    preco = request.POST['preco']
    max_estoque = request.POST['max_estoque']
    min_estoque = request.POST['min_estoque']
    estoque = Estoque.objects.create(nome_produto=nome_produto, descricao=descricao, preco=preco, max_estoque=max_estoque, min_estoque=min_estoque)
    estoque.save()
    return redirect('index_estoque')

def editar(request, id_estoque):
    estoque = get_object_or_404(Estoque, pk=id_estoque)
    return render(request, 'editar_estoque.html', {'dados_estoque': estoque})

def atualizar(request):
    id_estoque = request.POST['id']
    estoque = Estoque.objects.get(pk=id_estoque)
    estoque.nome_produto = request.POST['nome_produto']
    estoque.descricao = request.POST['descricao']
    estoque.max_estoque = request.POST['max_estoque']
    estoque.min_estoque = request.POST['min_estoque']
    estoque.save()
    return redirect('index_estoque')

def deletar(request, id_estoque):
    estoque = get_object_or_404(Estoque, pk=id_estoque)
    estoque.delete()
    return redirect('index_estoque')